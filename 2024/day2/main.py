def read_input_tentative_opti(filename): # je garde une trace de cette fonction comme ma tentative de faire O(n) du premier coup (un peu optimiste)

    matrix = []
    nb_of_safe_reports = 0
    with open('2024/day2/' + filename, 'r') as f:
        for line in f.readlines():
            line_is_safe = True
            is_decreasing = True
            monotony_has_changed = False #peut etre pas besoin
            

            n = len(line)
            l=[] #the line converted to a list


            for carac in line:
                new_el = ''
                while carac != ' ' or carac != '\n':
                    new_el += carac


            for i in range(0,n,3):

                #determine the length of the next number:
                j=i+1
                print(line[0])
                while (line[j] != ' ' or line[j] != '\n') and j < n-2:
                    print(n,j)
                    j+=1

                print(line[i:j])

                if i==0:
                    new_el = int(line[i:i+2])
                else:
                    new_el, last_el = int(line[i:i+2]), new_el

                if i > 0: #time to check the consistency of the list in-place
                    if new_el == last_el:
                        line_is_safe = False
                    if new_el - last_el > 3:
                        line_is_safe = False

                    elif last_el < new_el and is_decreasing:
                        if i==1: #then monotony becomes "increasing" until contrary is proven
                            monotony_has_changed = True
                            is_decreasing=False
                        else:
                            line_is_safe = False
                    
                    elif last_el > new_el and monotony_has_changed: #si on trouve deux elts consecutifs decroissants alors ue on decrease: pas bon
                        line_is_safe = False
                
                l.append(new_el)

            nb_of_safe_reports += int(line_is_safe)

            matrix.append(l)

    return matrix, nb_of_safe_reports




## faisons deja une solution ui marche, on verra en suite pour faire ch d'opti. (correction avant complexite)

def read_input(filename): # je garde une trace de cette fonction comme ma tentative de faire O(n) du premier coup (un peu optimiste)

    matrix = []
    nb_of_safe_reports = 0
    with open('2024/day2/' + filename, 'r') as f:
        for line in f.readlines():
            
            n = len(line)
            l=[] #the line converted to a list
            i,j = 0,0
            while j < n-1:

                new_elt, new_j = find_next_elt(line,n,i,j)
                l.append(new_elt)
                i,j = new_j+1, new_j+1

            matrix.append(l)

    return matrix, nb_of_safe_reports



def find_next_elt(line,n, i,j):
    while line[j] != ' ' and j<n-1:  #la deuxieme condition pour pas depasser, car le dernier caractere est un retour a la ligne.
        j+=1

    return int(line[i:j]), j


def part1(matrix):
        
    nb_of_safe_reports = 0

    for l in matrix:
        n = len(l)
        last_elt, new_elt = l[0], l[1]
        safe=True
        is_decreasing = True
        monotony_has_changed = False
        count=1
        while safe and count < n:
            
            #tous les cas de figure ui peuvent faire ue ca n'est plus safe:
            # 1- 2 elts successifs sont egaux
            # 2- on est decroissants au debut mais a un moment on devient croissant
            # 3- on est croissants au debut mais a un moment on devient decroissant
            # 4- le saut entre deux gusses est > 3


            if last_elt == new_elt: safe = False

            if abs(last_elt  - new_elt) > 3: safe = False

            elif last_elt < new_elt: #increasing
                if count == 1:
                    monotony_has_changed = True

                elif not monotony_has_changed: # decreases then increases
                    safe = False #passe le premier coup, si monotony has not changed et ue on est croissants, alors c pas bon.

            elif last_elt > new_elt: #increases then decreases
                if monotony_has_changed: 
                    safe = False


            count += 1

            if count < n - 1:
                new_elt, last_elt = l[count], new_elt
            else:
                new_elt, last_elt = l[-1], new_elt # cas de bordure a deux balles !!!! berk.

        
        if safe:
            nb_of_safe_reports += 1

    return nb_of_safe_reports


def part2(matrix):

    nb_of_safe_reports = 0

    for l in matrix:
        safe1,safe2, safe3=False, False, False
        
        safe,ind = check_report_safety(l)


        if not safe:
            safe1,_ = check_report_safety(l[:ind] + l[ind+1:])
            safe2,_ = check_report_safety(l[:ind-1] + l[ind:]) #ca peut etre le premier elt qui pose pb.
            if ind >= 2:
                safe3,_ = check_report_safety(l[:ind-2] + l[ind-1:]) #si courbe en cloche

            if not (safe1 or safe2 or safe3):
                print(l)
                print(l[:ind] + l[ind+1:])
                print(l[:ind-1] + l[ind:])
                print(ind)
            
        
        
        if safe or (safe1 or safe2 or safe3):
            nb_of_safe_reports += 1

    return nb_of_safe_reports

def check_report_safety(report):
    n = len(report)

    last_elt, new_elt = report[0], report[1]
    safe=True
    monotony_has_changed = False
    count=1

    while safe and count < n:
            
            #tous les cas de figure qui peuvent faire ue ca n'est plus safe:
            # 1- 2 elts successifs sont egaux
            # 2- on est decroissants au debut mais a un moment on devient croissant
            # 3- on est croissants au debut mais a un moment on devient decroissant
            # 4- le saut entre deux gusses est > 3


            if last_elt == new_elt: safe = False

            if abs(last_elt  - new_elt) > 3: safe = False

            elif last_elt < new_elt: #increasing
                if count == 1:
                    monotony_has_changed = True

                elif not monotony_has_changed: # decreases then increases
                    safe = False #passe le premier coup, si monotony has not changed et ue on est croissants, alors c pas bon.

            elif last_elt > new_elt: #increases then decreases
                if monotony_has_changed: 
                    safe = False


            count += 1

            if count < n - 1:
                new_elt, last_elt = report[count], new_elt
            else:
                new_elt, last_elt = report[-1], new_elt # cas de bordure a deux balles !!!! berk.

    return safe, count-1 #renvoyer l'indice de l'element probematique pour le pop



if __name__ == "__main__":
    matrix, _ = read_input('input.txt') #j'ai trafique le fichier txt en ajoutant un retour a la ligne a la toute fin pour eviter un cas particulier ennuyant. 


    nb_of_safe_reports1 = part1(matrix)
    print(nb_of_safe_reports1)


    nb_of_safe_reports2 = part2(matrix)
    print(nb_of_safe_reports2)