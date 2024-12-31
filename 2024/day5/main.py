import functools #to avoid re-implementing topological sort

def parse_input(filename):

    rules = {} # for part1
    order = [] #{} # for part2
    updates = []
    with open('2024/day5/' + filename, 'r') as f:

        rules_parse = True
        for line in f.readlines():

            if rules_parse:
                if line == '\n':
                    rules_parse = False
                else: 
                    X,Y = parse_rule(line)
                    rules[X] = rules.get(X, []) + [Y]

                    order.append([X,Y])

                    ### The following section is not working. For it to work, I would need an implementation of something resembling a topological sort. 
                    ### I use functools.cmp_to_key instead.

                    # if X in order and Y in order.keys():
                    #     if order[X] > order[Y]:
                    #         order = place_Y_after_X(X,Y,order)

                    #         if (X,Y) == (45, 97): print(order[45], order[97], order[64])

                    # elif (X in order) and (Y not in order):
                    #     order = place_Y_after_X(X,Y,order)

                    # elif (X not in order) and (Y in order):
                    #     order = place_X_before_Y(X,Y,order) 

                    # else:
                    #     n = len(order)
                    #     order[X], order[Y] = n + 1, n + 2


 

            else:
                updates.append(parse_update(line))

    return rules, order, updates

def place_Y_after_X(X,Y, order): #not efficient, should only run on the part after X
    n = order[X]
                            
    for k,v in order.items():
        if v > n: order[k] += 1

    order[Y] = n + 1 #put Y right after X, to respect eventual other orders

    return order

def place_X_before_Y(X,Y, order): #not efficient, should only run on the part after Y
    n = order[Y]
                            
    for k,v in order.items():
        if v >= n: order[k] += 1

    order[X] = n #put X right before Y, to respect eventual other orders

    return order


def parse_rule(line):
    """Parse a rule 'X|Y' and return ints X and Y. Made this to be more general than only 2-digits.

    Args:
        line (str): line of input.txt

    Returns:
        X (int)
        Y (int)
    """
    X,Y=-1,-1

    for i,char in enumerate(line): #possible to use file.read().strip().split('|') , and use a mapping to an int: list(map(lambda l: list(map(int, l.split('|')))

        if char == '|':
            X, Y = int( line[:i] ), int( line[i+1:] )
            break

    return(X,Y)

def parse_update(line):
    upd = []
    last_i = 0
    for i,char in enumerate(line):
        if char == ',':
            upd.append(int( line[last_i:i] ))
            last_i = i + 1

    upd.append(int( line[last_i:i] )) #last update. -1 because of '\n'.

    return upd



def part1(rules, updates):
    # Instructions:
    # Determine which updates are already in the correct order. 
    # What do you get if you add up the middle page number from those correctly-ordered updates?

    correct_updates = [True for _ in updates] # all updates initially set to True

    for i,upd in enumerate(updates): # go through each update, and see which ones are Falsely ordered
        for j,page in enumerate(upd): #go through each element of the update to see if it respects rules

            for predecessor in upd[:j]: #to check if rule is respected: look at predecessors and check that they are not in a rule num|predecessor
                if predecessor in rules.get(page, []): 
                    correct_updates[i] = False # set to False
                    break #first rule broken = whole update is False
                
            if not correct_updates[i]:
                break #a voir, c ptet un peu moche.

    return correct_updates, add_middle_page_numbers(updates,correct_updates)

    

def add_middle_page_numbers(updates, correct_updates):
    sum = 0

    for i,upd in enumerate(updates):
        if correct_updates[i]:
            n = len(upd)
            sum += upd[n//2]

    return sum

def part2(order, updates, correct_updates):

    corrected_updates = []
    to_sum = []

    for bool, upd in zip(correct_updates, updates):
        if not bool: 
            corrected_updates.append(sorted(upd, key=functools.cmp_to_key(lambda X,Y: -1 if [X,Y] in order else (1 if [Y,X] in order else 0)))) #nice
            to_sum.append(True)

    sum = add_middle_page_numbers(corrected_updates, to_sum)

    return corrected_updates, sum


def part2_old(order, updates, correct_updates): #kept just for the record, in case I want to implement the topological sort and use the commented section of parse_input
    
    incorrect_updates = filter_only_incorrect(updates, correct_updates)

    corrected_updates = []
    for upd in incorrect_updates:
        
        new = sorted(upd,key= lambda x: order[x])
        corrected_updates.append(new)

    sum = add_middle_page_numbers(corrected_updates, [True for _ in corrected_updates])

    return corrected_updates, sum

def filter_only_incorrect(updates, correct_updates):

    incorrect_updates = []

    for bool, upd in zip(correct_updates, updates):
        if bool: incorrect_updates.append(upd)

    return incorrect_updates


if __name__ == "__main__":

    filename = "input.txt"
    # filename = "test.txt"

    rules, order, updates = parse_input(filename)

    correct_updates, sum1 = part1(rules, updates)

    print(f'Result for part 1: sum = {sum1}')

    corrected_updates, sum2 = part2(order, updates, correct_updates)

    print(f'Result for part 2: sum = {sum2}')