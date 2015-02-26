__author__ = 'Michael'
import sys


def find_longest(input):
    """
    this method finds the longest drainage route (max decreasing distance)
    """
    for thing in input:
        print thing
    dist_array = [[0 for x in range(rows)] for x in range(cols)]  # rows and cols are static variables in main method
    for x in xrange(0, len(input), 1):
        for y in xrange(0, len(input[x]), 1):
            dist_array[x][y] = calculate_longest(dist_array, input, x, y)
    for item in dist_array:
        print item
    return max(max(dist_array))


def calculate_longest(max_dist_array, input, x, y):
    if max_dist_array[x][y] != 0:
        return max_dist_array[x][y]
    num_list = []
    try:
        if input[x][y] > input[x][y + 1]:
            num_list.append(calculate_longest(max_dist_array, input, x, y + 1))
    except IndexError:
        pass

    try:
        if input[x][y] > input[x][y - 1]:
            num_list.append(calculate_longest(max_dist_array, input, x, y - 1))
    except IndexError:
        pass

    try:
        if input[x][y] > input[x + 1][y]:
            num_list.append(calculate_longest(max_dist_array, input, x + 1, y))
    except IndexError:
        pass

    try:
        if input[x][y] > input[x - 1][y]:
            num_list.append(calculate_longest(max_dist_array, input, x - 1, y))
    except IndexError:
        pass
    # base case of when no neighbors are lower - set and return
    if len(num_list) == 0:
        max_dist_array[x][y] = 1
        return max_dist_array[x][y]
    # otherwise we take the max of the returned values of all neighbors, then set and return
    else:
        max_dist_array[x][y] = 1 + max(num_list)
        return max_dist_array[x][y]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        cases = f.readline().strip()
        rows = 0
        cols = 0
        count = -1
        name = ""
        for line in f:
            words = line.strip().split(" ")
            if words[0].isalpha():
                name = words[0]
                rows = int(words[1])
                cols = int(words[2])
                matrix = []
            else:
                row = []
                i = 0
                for amount in words:
                    row.append(int(words[i]))
                    i += 1
                i = 0
                matrix.append(row)
            count += 1
            if count == rows:
                count = -1
                print name + ": " + str(find_longest(matrix))