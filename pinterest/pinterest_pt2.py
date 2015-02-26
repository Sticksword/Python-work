__author__ = 'Michael'
import itertools


def x_src_2nd_connection():
    first_line = raw_input()
    options = first_line.split(',')
    person1 = options[0]
    person2 = options[1]
    # print person1, person2
    connection_dict = dict()
    while True:
        try:
            function_call = raw_input().split(',')
            if len(function_call) <= 1:
                break
            if not function_call[1] in connection_dict: # if the connection is not in our dict of connections
                connection_dict[function_call[1]] = dict() # add new connection as key and assign another dict as value

            if not function_call[0] in connection_dict[function_call[1]]: # if the person not in our connection's dict
                connection_dict[function_call[1]][function_call[0]] = [function_call[2]] # add person as key and connection path as value
            else:
                connection_dict[function_call[1]][function_call[0]].append(function_call[2]) # otherwise add connection path to person

        except EOFError:
            break
    for x in connection_dict.keys():
        a = sorted(connection_dict[x][person1])
        b = sorted(connection_dict[x][person2])
        for r in itertools.product(a, b):
            if not r[0] == r[1]:
                print x + ": [" + r[0] + ", " + r[1] + "]"


if __name__ == '__main__':
    x_src_2nd_connection()