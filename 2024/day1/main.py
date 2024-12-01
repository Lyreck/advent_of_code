

def read_input(filename):

    l1,l2 = [],[]

    with open('2024/day1/' + filename, 'r') as f:
        for line in f.readlines():
            l1.append(int(line[:5]))
            l2.append(int(line[8:]))

    l1.sort()
    l2.sort()

    return l1, l2


def find_pairs(l1,l2): # and compute distance in the mean time to avoid a third go-through the list

    distance = 0
    print(l1)

    for i,j in zip(l1,l2):
        distance += abs(i-j)

    return distance





if __name__ == "__main__":


    l1,l2 = read_input("input.txt")

    distance = find_pairs(l1,l2)

    print(distance)