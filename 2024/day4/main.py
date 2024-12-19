def parse_input(filename):

    data = []
    size = 0
    with open('2024/day4/' + filename, 'r') as f:
        for line in f.readlines():
            data += [line[:-1] if line[-1:] == "\n" else line] #remove the \n, but edge case with the last.
            size += len(line)

    return data, size #matrix with each line = a line of the input.


def part1(data, size):

    # version gloutonne: a chake 'X', check les lettres suivantes, les lettres en-dessous, les lettres au-dessus, les lettres a gauche, 
    # les lettres en diagonale a droite, les lettres en diagonale a gauche.
    # ce ki va etre le + embetant, c'est de gerer les bords.

    # pas compris dans la consigne: "it allows words to overlap other words"

    count = 0 #nb of XMAS

    for i in range(size):
        try: #a droite
            if data[i:i+4] == 'XMAS':
                count += 1
        except:
            pass # a voir si je perosnnalise pour rendre ca plus propre en ne filtrant ke les index out of bound.


#autre idees rigolotes: transformer le truc en matrice d'entiers, et trouver un produit matriciel ki fait le bidule?




if __name__ == "__main__":

    filename = "input.txt"

    data, size = parse_input(filename)

    print(data)