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

def multiply_everyone(matches):

    res = 0

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
    
    for mul in matches:

        if re.search(pattern1, mul):
            A = int( mul[4:5] )
            B = int( mul[6:7] )
            res += A * B

        if re.search(pattern2, mul):
            A = int( mul[4:6] )
            B = int( mul[7:9] )
            res += A * B

        if re.search(pattern2_1, mul):
            A = int( mul[4:6] )
            B = int( mul[7:8] )
            res += A * B

        if re.search(pattern1_2, mul):
            A = int( mul[4:5] )
            B = int( mul[6:8] )
            res += A * B

        if re.search(pattern3, mul):
            A = int( mul[4:7] )
            B = int( mul[8:11] )
            res += A * B

        if re.search(pattern3_1, mul):
            A = int( mul[4:7] )
            B = int( mul[8:9] )
            res += A * B

        if re.search(pattern1_3, mul):
            A = int( mul[4:5] )
            B = int( mul[6:9] )
            res += A * B

        if re.search(pattern3_2, mul):
            A = int( mul[4:7] )
            B = int( mul[8:10] )
            res += A * B

        if re.search(pattern2_3, mul):
            A = int( mul[4:6] )
            B = int( mul[7:10] )
            res += A * B

    return res




if __name__ == "__main__":

    filename = "input.txt"
    data = parse_input(filename)

    matches = remove_noise(data)

    # print(matches)

    res = multiply_everyone(matches)

    print(f'Final result for part 1: {res}')