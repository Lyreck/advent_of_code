def parse_input(filename):

    rules = {}
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

            else:
                updates.append(parse_update(line))

    return rules, updates



def parse_rule(line):
    """Parse a rule 'X|Y' and return ints X and Y. Made this to be more general than only 2-digits.

    Args:
        line (str): line of input.txt

    Returns:
        X (int)
        Y (int)
    """
    X,Y=-1,-1

    for i,char in enumerate(line):

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
        for j,num in enumerate(upd): #go through each element of the update to see if it respects rules

            for predecessor in upd[:j]: #to check if rule is respected: look at predecessors and check that they are not in a rule num|predecessor
                if predecessor in rules.get(num, []): 
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

            

def part2(rules, updates, correct_updates):
    
    incorrect_updates = filter_only_incorrect(updates, correct_updates)

    

def filter_only_incorrect(updates, correct_updates):

    incorrect_updates = []

    for bool, upd in zip(correct_updates, updates):
        if bool: incorrect_updates.append(upd)

    return incorrect_updates


if __name__ == "__main__":

    filename = "input.txt"
    # filename = "test.txt"

    rules, updates = parse_input(filename)

    correct_updates, sum = part1(rules, updates)

    print(f'Result for part 1: sum = {sum}')

    part2(rules, updates, correct_updates):
