import unittest
from add_up_to_k import find_sums


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
        k = 0
        expected_output = "This list is empty."
        output = find_sums(my_list, k)
        self.assertEqual(expected_output, output)

    def test_noInput(self):
        my_list = None
        k = None
        expected_output = "Please provide a list of numbers and a target value."
        output = find_sums(my_list, k)
        self.assertEqual(expected_output, output)

    def test_mixedTypes(self):
        my_list = [2, 'k', '?', 2, 3.4, 3, 10]
        k = 13
        with self.assertRaises(TypeError) as error:
            find_sums(my_list, k)
        self.assertEqual("Please use integers or floats.", str(error.exception))


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