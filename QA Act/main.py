import unittest

def sum(n1, n2):
    return n1 + n2

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(10, 9), 19)
        self.assertEqual(sum(-1, 5), 4)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(8, -8), 0)

if __name__ == '__main__':
    unittest.main()
