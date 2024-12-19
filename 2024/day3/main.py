## day 3
import re

def parse_input(filename):

    data = ''
    with open('2024/day3/' + filename, 'r') as f:
        for line in f.readlines():
            data += line

    return data

def remove_noise(data):

    i = 0
    n = len(data)

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    matches = re.findall(pattern, data)
    
    return matches


def get_mul_numbers(mul):

    #J'essaie de couvrir tous les pattern possibles pour avoir un premier truc fonctionnel. A voir dans le futur pur un truc plus souple / lisible / propre.
    
    pattern1 = r"mul\(\d{1},\d{1}\)"
    pattern2 = r"mul\(\d{2},\d{2}\)"
    pattern2_1 = r"mul\(\d{2},\d{1}\)"
    pattern1_2 = r"mul\(\d{1},\d{2}\)"

    pattern3 = r"mul\(\d{3},\d{3}\)"
    pattern3_1 = r"mul\(\d{3},\d{1}\)"
    pattern1_3 = r"mul\(\d{1},\d{3}\)"
    pattern3_2 = r"mul\(\d{3},\d{2}\)"
    pattern2_3 = r"mul\(\d{2},\d{3}\)"

    #approche gloutonne ne fonctionne que parce que l'on sait que les nombres concernes ont max 3 chifres.


    if re.search(pattern1, mul):
        A = int( mul[4:5] )
        B = int( mul[6:7] )

    if re.search(pattern2, mul):
        A = int( mul[4:6] )
        B = int( mul[7:9] )

    if re.search(pattern2_1, mul):
        A = int( mul[4:6] )
        B = int( mul[7:8] )

    if re.search(pattern1_2, mul):
        A = int( mul[4:5] )
        B = int( mul[6:8] )

    if re.search(pattern3, mul):
        A = int( mul[4:7] )
        B = int( mul[8:11] )

    if re.search(pattern3_1, mul):
        A = int( mul[4:7] )
        B = int( mul[8:9] )

    if re.search(pattern1_3, mul):
        A = int( mul[4:5] )
        B = int( mul[6:9] )

    if re.search(pattern3_2, mul):
        A = int( mul[4:7] )
        B = int( mul[8:10] )

    if re.search(pattern2_3, mul):
        A = int( mul[4:6] )
        B = int( mul[7:10] )

    return(A,B)

def part1(data):

    res = 0
    matches = remove_noise(data)
    
    for mul in matches:
        A,B = get_mul_numbers(mul)
        res += A * B

    return res


def part2(data):

    ## en gros:
    # - au debut, j'attend sl epremier don't 
    # - une fois le premir don't rencontre, j'attends le prochain do
    # - a chaue fois ke je rnecontre un do, j'attends le prochain don't 

    # possible: un bool do, ki me dit si le dernier rencontre est un do ou un don't. 
    # 0je parcours chake string en gardant en mem l'indice du do 
    # des ke je rencontre un don't ET ke j'ai do = True, je lance un scan j:i+

    res = 0

    do = True
    last_do = 0
    for i,_ in enumerate(data):

        if data[i:i+4] == 'do()' and (not do): #second case to filter out when there are multiple do() between don't() s 
            do = True
            last_do = i

        if data[i:i+7] == "don't()" and do: # scan the last indices between last_do and newly found "don't"
            sub_data = data[last_do:i+7]

            # print("\n")
            # print(sub_data)
            
            sub_matches = remove_noise(sub_data)

            # print(sub_matches)

            for mul in sub_matches:
                A,B = get_mul_numbers(mul)
                res += A * B

            do = False
    
    if do: #end of loop: if not don't was detected then add up all the last multiplications
        sub_data = data[last_do:]
        sub_matches = remove_noise(sub_data)

        for mul in sub_matches:
            A,B = get_mul_numbers(mul)
            res += A * B


    return res










if __name__ == "__main__":

    filename = "input.txt"
    data = parse_input(filename)

    res1 = part1(data)

    print(f'Result for part 1: {res1}')

    res2 = part2(data)
    print(f'Result for part 2: {res2}')


    # petit_test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    # restest = part2(petit_test)
    # print(restest)

