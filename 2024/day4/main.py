def parse_input(filename):

    data = []
    size = 0
    with open('2024/day4/' + filename, 'r') as f:
        for line in f.readlines():
            data.append(['Z', 'Z', 'Z', 'Z'] + [i for i in line if i != '\n'] + ['Z', 'Z', 'Z', 'Z']) #remove the \n, but edge case with the last.
            size += len(line)

    return data, size #matrix with each line = a line of the input.

def expand_matrix(mat):
    """Expand matrix with 4 rows of "Z" to be able to test for each XMAS without bothering about borders. Cols of 'Z' were already added when reading the file.

    Args:
        mat (list): list of lists (matrix), must contain at least an empty list.

    Returns:
        Expanded matrix.
    """

    m = len(mat[0])

    line = ['Z' for _ in range(m)]

    return 4*[line] + data + 4*[line]



def part1(data):

    # version gloutonne: a chake 'X', check les lettres suivantes, les lettres en-dessous, les lettres au-dessus, les lettres a gauche, 
    # les lettres en diagonale a droite, les lettres en diagonale a gauche.
    # ce ki va etre le + embetant, c'est de gerer les bords. C'est fait grace a expand_matrix.

    # pas compris dans la consigne: "it allows words to overlap other words"

    n,m = len(data), len(data[0]) #n by m matrix.

    count = 0 #nb of XMAS

    for i in range(4,n-4):
        for j in range(4,m-4):

            if data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3] == 'XMAS': #a droite
                count += 1

            if data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] == 'XMAS': #diagonale bas droite
                count += 1

            if data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j] == 'XMAS': #en bas
                count += 1
            
            if data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] == 'XMAS': #diagonale bas gauche
                count += 1

            if data[i][j] + data[i][j-1] + data[i][j-2] + data[i][j-3] == 'XMAS': #a gauche
                count += 1

            if data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3] == 'XMAS': #diagonale haut gauche
                count += 1

            if data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j] == 'XMAS': #en haut
                count += 1

            if data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3] == 'XMAS': #diagonale haut droite
                count += 1

        
    return count

#autre idees rigolotes: transformer le truc en matrice d'entiers, et trouver un produit matriciel ki fait le bidule?




def part2(data):

    # version gloutonne: a chaque 'X', check les lettres suivantes, les lettres en-dessous, les lettres au-dessus, les lettres a gauche, 
    # les lettres en diagonale a droite, les lettres en diagonale a gauche.
    # ce ki va etre le + embetant, c'est de gerer les bords. C'est fait grace a expand_matrix.

    # pas compris dans la consigne: "it allows words to overlap other words"

    n,m = len(data), len(data[0]) #n by m matrix.

    count = 0 #nb of XMAS

    for i in range(4,n-4):
        for j in range(4,m-4):

            if (data[i][j] + data[i+1][j+1] + data[i+2][j+2], data[i][j+2] + data[i+1][j+1] + data[i+2][j]) in [('MAS', 'MAS'), ('SAM', 'SAM'), ('SAM', 'MAS'), ('MAS', 'SAM')]:
                count+=1

        
    return count


if __name__ == "__main__":

    filename = "input.txt"
    # filename = "min_test.txt"

    data, size = parse_input(filename)

    data = expand_matrix(data)


    count1 = part1(data)
    print(f'Result for part 1: count = {count1}')

    count2 = part2(data)
    print(f'Result for part 2: count = {count2}')