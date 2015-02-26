<<<<<<< HEAD
__author__ = 'Michael Chen - mzc2fd'


class OurSet:
    """
    This OurSet class implements a simple set ADT.
    I used a list as the underlying data storage for my class.
    It has many of the common functions that a set would have, such as union, intersection, and so on.
    """
    def __init__(self, init_values=[]):
        """
        this is the constructor
        """
        self.list = init_values or []

    def __str__(self):
        """
        this returns the string form of the list of OurSet and is unique in that it has triangle brackets.
        """
        string = "<"
        for x in xrange(0, len(self.list) - 1):
            string += str(self.list[x]) + ", "
        string += str(self.list[len(self.list) - 1]) + ">"
        return string

    def __len__(self):
        """
        this gives us the length of the list
        """
        return len(self.list)

    def __iter__(self):
        """
        this returns an iterator of the list
        """
        return iter(self.list)

    def add(self, item):
        """
        this adds an item to the list if it isn't already in the list and returns true if the item is added
        """
        if not item in self.list:
            self.list.append(item)
            return True
        return False

    def addList(self, list):
        """
        this attempts to add the items of a list to the current list if the items aren't in the list
        if anything is added, it will return true
        """
        flag = False
        for item in list:
            if not item in self.list:
                self.list.append(item)
                flag = True
        return flag

    def union(self, set2):
        """
        this performs a set union on the current list and another set
        """
        unionSet = []
        for item in self.list:
            unionSet.append(item)
        for item2 in set2:
            if not item2 in self.list:
                unionSet.append(item2)
        return unionSet

    def intersection(self, set2):
        """
        this returns a set intersection on the current list and another set
        """
        intersectionSet = []
        for item in self.list:
            if item in set2:
                intersectionSet.append(item)
        return intersectionSet

#my __main__ for testing stuff
if __name__ == '__main__':
    print 'hai'
    s1 = OurSet()
    s1.add(5)
    s1.add(6)
    print s1
    print s1.union([6, 7, 8, 10])
    print s1.intersection([1, 2, 3, 4, 5])
=======
__author__ = 'Michael Chen - mzc2fd'


class OurSet:
    """
    This OurSet class implements a simple set ADT.
    I used a list as the underlying data storage for my class.
    It has many of the common functions that a set would have, such as union, intersection, and so on.
    """
    def __init__(self, init_values=[]):
        """
        this is the constructor
        """
        self.list = init_values or []

    def __str__(self):
        """
        this returns the string form of the list of OurSet and is unique in that it has triangle brackets.
        """
        string = "<"
        for x in xrange(0, len(self.list) - 1):
            string += str(self.list[x]) + ", "
        string += str(self.list[len(self.list) - 1]) + ">"
        return string

    def __len__(self):
        """
        this gives us the length of the list
        """
        return len(self.list)

    def __iter__(self):
        """
        this returns an iterator of the list
        """
        return iter(self.list)

    def add(self, item):
        """
        this adds an item to the list if it isn't already in the list and returns true if the item is added
        """
        if not item in self.list:
            self.list.append(item)
            return True
        return False

    def addList(self, list):
        """
        this attempts to add the items of a list to the current list if the items aren't in the list
        if anything is added, it will return true
        """
        flag = False
        for item in list:
            if not item in self.list:
                self.list.append(item)
                flag = True
        return flag

    def union(self, set2):
        """
        this performs a set union on the current list and another set
        """
        unionSet = []
        for item in self.list:
            unionSet.append(item)
        for item2 in set2:
            if not item2 in self.list:
                unionSet.append(item2)
        return unionSet

    def intersection(self, set2):
        """
        this returns a set intersection on the current list and another set
        """
        intersectionSet = []
        for item in self.list:
            if item in set2:
                intersectionSet.append(item)
        return intersectionSet

#my __main__ for testing stuff
if __name__ == '__main__':
    print 'hai'
    s1 = OurSet()
    s1.add(5)
    s1.add(6)
    print s1
    print s1.union([6, 7, 8, 10])
    print s1.intersection([1, 2, 3, 4, 5])
>>>>>>> origin/master
