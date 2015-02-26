<<<<<<< HEAD
__author__ = 'Michael'

import unittest
from Queue import Queue


class test_queue(unittest.TestCase):
    def setUp(self):
        self.emptyQueue = Queue()
        self.list1 = [1, 2, 3, 4]
        self.q1 = Queue(self.list1)

    def test_remove1(self):
        item = self.q1.remove()
        self.assertEquals(item, 1, "item remove not equal to 1")
        self.assertEquals(3, len(self.q1))

if __name__ == '__main__':
=======
__author__ = 'Michael'

import unittest
from Queue import Queue


class test_queue(unittest.TestCase):
    def setUp(self):
        self.emptyQueue = Queue()
        self.list1 = [1, 2, 3, 4]
        self.q1 = Queue(self.list1)

    def test_remove1(self):
        item = self.q1.remove()
        self.assertEquals(item, 1, "item remove not equal to 1")
        self.assertEquals(3, len(self.q1))

if __name__ == '__main__':
>>>>>>> origin/master
    unittest.main()