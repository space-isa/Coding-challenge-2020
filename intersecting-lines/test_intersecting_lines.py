#-------------------------------------------------------------------------------
#    Unit Tests
#-------------------------------------------------------------------------------

import unittest
from intersecting_lines import check_elements, find_intersection, main

class TestCheckElements(unittest.TestCase):

    def test_check_elements(self):
        p = [1, 3, 2, 0]
        N = 4
        expected_output = [0, 0, 1, 1, 1, 1]
        output = check_elements(p, N)
        self.assertEqual(output, expected_output)

    def test_len_binary_check(self):
        p = [1, 3, 2, 0]
        N = 4
        expected_len = int((N ** 2 - N) / 2)
        output_len = len(check_elements(p, N))
        self.assertEqual(output_len, expected_len)

    def test_empty_input(self):
        q = []
        N = 0
        expected_q = []
        self.assertEqual(check_elements(q, N), expected_q)

class TestFindIntersection(unittest.TestCase):

    def test_find_intersection(self):
        binary_p = [0, 0, 1, 1, 1, 1]
        binary_q = [1, 1, 1, 0, 1, 1]
        len_binary = len(binary_q)
        num_intersections = 3
        output = find_intersection(binary_p, binary_q, len_binary)
        self.assertEqual(output, num_intersections)

class TestMain(unittest.TestCase):

    def test_validate_input(self):
        p = [1,2,3]
        q = [1,2,3,4,5]
        expected_output = "Your array lengths do not match."
        output = main(p,q)
        self.assertEqual(output, expected_output)

def runTests():
    test_classes = [TestCheckElements, TestFindIntersection, TestMain]
    load_tests = unittest.TestLoader()

    test_list = []
    for test in test_classes:
        load_test_cases = load_tests.loadTestsFromTestCase(test)
        test_list.append(load_test_cases)

    test_suite = unittest.TestSuite(test_list)
    run_test = unittest.TextTestRunner()
    run_test.run(test_suite)

if __name__=='__main__':
    runTests()
