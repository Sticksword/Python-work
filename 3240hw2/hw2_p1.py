<<<<<<< HEAD
__author__ = 'Michael'


def maxmin(list):
    """
    this returns a tuple that has the max and the min of a given list
    """
    if len(list) == 0:
        return None

    max = min = list[0]
    for item in list:
        if max < item:
            max = item
        if min > item:
            min = item
    return max, min


def common_items(list1, list2):
    """
    this returns a list of all the items that are shared (in both) between list1 and list2
    """
    common_list = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_list.append(item1)
    return common_list


def notcommon_items(list1, list2):
    """
    this returns a list of all the items that are unique to either list1 or list2
    """
    notcommon_list = []
    #adds all unique items from list1
    for item1 in list1:
        flag = False
        for item2 in list2:
            if item1 == item2:
                flag = True
        if not flag:
            notcommon_list.append(item1)
    #adds all unique items from list2
    for item2 in list2:
        flag = False
        for item1 in list1:
            if item2 == item1:
                flag = True
        if not flag:
            notcommon_list.append(item2)
    return notcommon_list


def count_list_items(list):
    """
    this counts the number of items in a given list
    """
    d = dict()
    for item in list:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

#testing stuff
if __name__ == '__main__':
    print maxmin([1, 2, 3, 4])
    print maxmin([])
    print maxmin(['A', 'B', 'C', 'F'])
    print common_items([1, 2, 3], [2, 3, 4, 5])
    print notcommon_items([1, 2, 3, 4], [1, 3, 5, 7, 9])
=======
__author__ = 'Michael'


def maxmin(list):
    """
    this returns a tuple that has the max and the min of a given list
    """
    if len(list) == 0:
        return None

    max = min = list[0]
    for item in list:
        if max < item:
            max = item
        if min > item:
            min = item
    return max, min


def common_items(list1, list2):
    """
    this returns a list of all the items that are shared (in both) between list1 and list2
    """
    common_list = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_list.append(item1)
    return common_list


def notcommon_items(list1, list2):
    """
    this returns a list of all the items that are unique to either list1 or list2
    """
    notcommon_list = []
    #adds all unique items from list1
    for item1 in list1:
        flag = False
        for item2 in list2:
            if item1 == item2:
                flag = True
        if not flag:
            notcommon_list.append(item1)
    #adds all unique items from list2
    for item2 in list2:
        flag = False
        for item1 in list1:
            if item2 == item1:
                flag = True
        if not flag:
            notcommon_list.append(item2)
    return notcommon_list


def count_list_items(list):
    """
    this counts the number of items in a given list
    """
    d = dict()
    for item in list:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

#testing stuff
if __name__ == '__main__':
    print maxmin([1, 2, 3, 4])
    print maxmin([])
    print maxmin(['A', 'B', 'C', 'F'])
    print common_items([1, 2, 3], [2, 3, 4, 5])
    print notcommon_items([1, 2, 3, 4], [1, 3, 5, 7, 9])
>>>>>>> origin/master
    print count_list_items([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])