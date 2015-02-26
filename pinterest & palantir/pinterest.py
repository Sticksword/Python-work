__author__ = 'Michael'


def pretty_print():
    tuple_list = []
    while True:
        try:
            function_call = raw_input().split(',')
            if len(function_call) <= 1:
                break
            tuple_list.append(function_call)
        except EOFError:
            break
    tuple_list = sorted(tuple_list, key=lambda x: x[1])
    tab = '    '
    for i in xrange(0, len(tuple_list)):
        count = 0
        for j in xrange(0, i):
            if tuple_list[i][1] < tuple_list[j][2]:
                count += 1
        print tuple_list[i][1], tab[:5]*count, "[" + str(float(tuple_list[i][2])-float(tuple_list[i][1])).strip() + "]", tuple_list[i][0]


if __name__ == '__main__':
    pretty_print()