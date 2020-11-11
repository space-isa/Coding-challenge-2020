import unittest
from find_duplicate_elements import findDuplicates


class Testduplicates(unittest.TestCase):
    """
    TEST CASES
    ----------

    1. Test an empty list as an input.
    2. Test function given no input. 
    3. Test fuction given an input list with mixed dtypes. 
    """

    def test_emptyArray(self):
        my_list = []
        expected_output = None
        self.assertEqual(expected_output, findDuplicates(my_list))

    def test_noInput(self):
        with self.assertRaises(SystemExit) as check_assert:
            findDuplicates()
            self.assertRaises(check_assert.exception.code, 1)

    def test_mixedTypes(self):
        my_list = ["?", "!", "?", 1, 3, 4.56]
        is_equal = findDuplicates(my_list)
        expected_output = False
        self.assertEqual(expected_output, is_equal)


def runTests():
    test_classes = [Testduplicates]
    load_tests = unittest.TestLoader()

    test_list = []
    for test in test_classes:
        load_test_cases = load_tests.loadTestsFromTestCase(test)
        test_list.append(load_test_cases)

    test_suite = unittest.TestSuite(test_list)
    run_test = unittest.TextTestRunner()
    run_test.run(test_suite)


if __name__ == "__main__":
    runTests()