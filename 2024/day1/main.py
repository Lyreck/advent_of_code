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

    for i,j in zip(l1,l2):
        distance += abs(i-j)

    return distance

def compute_similarity(l1,l2):
    n=len(l1)

    similarity_score=0

    #since both lists are sorted, we have to begin searching in l2 at the last element that is < l1[0]:
    el1 = l1[0]
    j=0
    while el1 > l2[j]:
        j+=1    

    nb_occ=0
    for i in range(n):
        if (i > 0) and (l1[i] == l1[i-1]):
            similarity_score += l1[i] *  nb_occ

        else:
            nb_occ=0 #nb of similar occurences

            if l1[i] >= l2[j] and l1[i] <= l2[-1]: #else we won't find anyone
                while l1[i] > l2[j] and j < n-1:
                    j += 1 #parcours de la liste 2

                while l1[i] == l2[j] and j < n:

                    if l1[j] == 7:
                        print("wesh?")

                    j += 1 #parcours de la liste 2
                    nb_occ += 1

                    if j==n: 
                        j=n-1
                        break # moche mais pas le tps de faire + propre

            similarity_score += l1[i] *  nb_occ

    return similarity_score



if __name__ == "__main__":
    ## Part One 
    l1,l2 = read_input("input.txt")
    distance = find_pairs(l1,l2)
    print(distance)

    ## Part Two

    # l1 = [1,2,3,3,3,4]
    # l2 = [3,3,3,4,5,9]

    # l1 = [4,5,7,9,10]
    # l2 = [1,2,4,6,7]

    similarity_score = compute_similarity(l1,l2)

    print(similarity_score)