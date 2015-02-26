__author__ = 'Michael'


def compare(word, word2):
    char_list = list(word)
    char_list2 = list(word2)
    length = len(char_list)
    equal = 0
    opposite = 0
    for a in range(0, length):
        if char_list[a] == char_list2[a]:
            equal += 1
        else:
            opposite += 1
    if equal == length or opposite == length:
        return True
    return False


first_line = raw_input()
options = first_line.split(' ')
M = options[0]
N = options[1]
list_of_lines = []
for x in range(0, int(M)):
    list_of_lines.append(raw_input())

permlist = [0] * int(M)

for x in range(0, int(M)):
    for y in range(x + 1, int(M)):
        if compare(list_of_lines[x], list_of_lines[y]):
            permlist[x] += 1

sorted(permlist, reverse=True)
if permlist[0] == 0:
    print 0
else:
    print permlist[0]+1
