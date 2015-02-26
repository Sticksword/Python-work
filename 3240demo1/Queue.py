<<<<<<< HEAD
__author__ = 'Michael'


class Queue:

    def __init__(self, init_values = []):

        self.values = init_values or []
    #using 'or []' avoids having the same value being pointed to by multiple instances of Queue
    #cannot overload constructors

    def __str__(self):
        return "Q: " + str(self.values)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)
    #__contains__

    def add(self, item):
        self.values.append(item)

    def front(self):
        if len(self.values) == 0:
            return None
        return self.values(0)

    def remove(self):
        if len(self.values) == 0:
            return None
        result = self.values[0]
        del self.values[0]
        return result

def test_front_empty():
    """ test calling front on empty queue"""
    q1 = Queue()
    res = q1.front()
    assert res == None

def test_remove_empty():
    """ test calling remove on empty queue"""
    q1 = Queue()
    res = q1.remove()
    assert res == None

def test_remove_size1():
    """ test calling remove on queue of size 1"""
    q1 = Queue()
    res = q1.remove()
    assert len(q1) == 0

if __name__ == '__main__':
    test_front_empty()
    test_remove_empty()
    test_remove_size1()
    # q2 = Queue()
    # q2.add("one")
    # q2.add("two")
    # q2.add("three")
    # print q2.remove()
    # print q2
    #
    # q3 = Queue()
    # print q3.remove()
    # print q3
    # l1 = [1, 2, 3]
    # for item in l1:
    #     print item
    # x = 3
    # if x in l1:
=======
__author__ = 'Michael'


class Queue:

    def __init__(self, init_values = []):

        self.values = init_values or []
    #using 'or []' avoids having the same value being pointed to by multiple instances of Queue
    #cannot overload constructors

    def __str__(self):
        return "Q: " + str(self.values)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)
    #__contains__

    def add(self, item):
        self.values.append(item)

    def front(self):
        if len(self.values) == 0:
            return None
        return self.values(0)

    def remove(self):
        if len(self.values) == 0:
            return None
        result = self.values[0]
        del self.values[0]
        return result

def test_front_empty():
    """ test calling front on empty queue"""
    q1 = Queue()
    res = q1.front()
    assert res == None

def test_remove_empty():
    """ test calling remove on empty queue"""
    q1 = Queue()
    res = q1.remove()
    assert res == None

def test_remove_size1():
    """ test calling remove on queue of size 1"""
    q1 = Queue()
    res = q1.remove()
    assert len(q1) == 0

if __name__ == '__main__':
    test_front_empty()
    test_remove_empty()
    test_remove_size1()
    # q2 = Queue()
    # q2.add("one")
    # q2.add("two")
    # q2.add("three")
    # print q2.remove()
    # print q2
    #
    # q3 = Queue()
    # print q3.remove()
    # print q3
    # l1 = [1, 2, 3]
    # for item in l1:
    #     print item
    # x = 3
    # if x in l1:
>>>>>>> origin/master
    #     print x, " is there"