def parse_input(filename):
    with open('2024/day6/' + filename, 'r') as f:
        map = f.read().strip().split('\n') #way more efficient and clean than my previous approaches ! Thanks https://github.com/tom-favereau/advent_of_code/blob/main/2024/day5/5.py

    return map


def find_guard(map): #pas bo?

    for i,line in enumerate(map):
        for j,el in enumerate(line):
            if el != '.' and el != "#" and el != "X":
                return i,j


def find_next_obstacle(map, pos, direction, num_positions_visited, i_range, j_range): #what about the case where we go off bounds ?
    # technically I don't return the obstacle's position, but rather the position of the guard next to the obstacle.
    i,j = pos
    visited=[]
    in_bounds = (i in i_range and j in j_range)
    map, num_positions_visited = update_count(map, i, j, num_positions_visited, visited)

    if direction == '^':
        line=i
        while map[line][j] != '#' and in_bounds:
            line -= 1
            map, num_positions_visited = update_count(map, line+1, j, num_positions_visited, visited)
            in_bounds = (line in i_range and j in j_range)
        
        if in_bounds:
            return line+1, j, map, num_positions_visited

    if direction == '>':
        column=j
        while map[i][column] != '#' and in_bounds:
            column += 1
            map, num_positions_visited = update_count(map, i, column-1, num_positions_visited, visited)
            in_bounds = (i in i_range and column in j_range)

        if in_bounds:
            return i, column-1, map, num_positions_visited

    if direction == 'v':
        line=i
        #while in_bounds and map[line][j] != '#':
        while map[line][j] != '#':
            line += 1
            map, num_positions_visited = update_count(map, line-1, j, num_positions_visited, visited)
            in_bounds = (line in i_range and j in j_range)
            if not in_bounds:
                break

        if in_bounds:
            return line-1, j, map, num_positions_visited

    if direction == '<':
        column=j
        while map[i][column] != '#' and in_bounds:
            column -= 1
            map, num_positions_visited = update_count(map, i, column+1, num_positions_visited, visited)
            in_bounds = (i in i_range and column in j_range)
        
        if in_bounds:
            return i, column+1, map, num_positions_visited

    if not in_bounds:
        return -1,-1,map,num_positions_visited


def update_count(map, i, j, num_positions_visited, visited):

    if (i,j) not in visited: 
        map[i] = map[i][:j] + 'X' + map[i][j+1:] #to get visual feedback. Could do something with this instead of searching a list, would be more efficient but more mind-breaking to write.
        visited.append((i,j))
        num_positions_visited+=1

    return map, num_positions_visited


def part1(map):
    num_positions_visited = 0 #counter for result

    n,m = len(map), len(map[0])
    i,j = find_guard(map)

    i_range, j_range = [k for k in range(n)], [k for k in range(m)]
    while i in i_range and j in j_range: #while guard is still in the room
        if map[i][j] == '^':
            i,_,map,num_positions_visited = find_next_obstacle(map, (i, j), '^', num_positions_visited, i_range, j_range)
            if (i,j) != (-1,-1): map[i] = map[i][:j] + '>' + map[i][j+1:] #bricolage le -1,-1...

        if map[i][j] == '>':
            _,j,map,num_positions_visited = find_next_obstacle(map, (i, j), '>', num_positions_visited, i_range, j_range)
            if (i,j) != (-1,-1): map[i] = map[i][:j] + 'v' + map[i][j+1:]

        if map[i][j] == 'v':
            i,_,map,num_positions_visited = find_next_obstacle(map, (i, j), 'v', num_positions_visited, i_range, j_range)
            if (i,j) != (-1,-1): map[i] = map[i][:j] + '<' + map[i][j+1:]

        if map[i][j] == '<':
            _,j,map,num_positions_visited = find_next_obstacle(map, (i, j), '<', num_positions_visited, i_range, j_range)
            if (i,j) != (-1,-1): map[i] = map[i][:j] + '^' + map[i][j+1:]

    numbis = 0
    for line in map:
        for char in line:
            if char == 'X': numbis +=1

    return map, num_positions_visited, numbis




if __name__ == '__main__':
    filename = "input.txt"
    #filename = 'mini-test.txt'

    map = parse_input(filename)

    print(map)

    updated_map, num1, numbis = part1(map)

    print(updated_map)
    print(num1)
    print(numbis) #numbis is correct. The "in-line" number incrementor doesn't work (don't have time to figure out why)