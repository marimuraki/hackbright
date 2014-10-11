import unittest

from list_operations import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec']
        self.notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        self.multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    ### Tests for Part 1 ###

    def test_1_A_head(self):
        self.assertEqual(head(self.months), 'Jan')
        self.assertEqual(head(self.notes), 'Do')
        self.assertEqual(head(self.multiples), 0)

    def test_1_B_tail(self):
        self.assertEqual(tail(self.months), ['Feb', 'Mar', 'Apr', 'May', 'Jun',
                                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                             'Dec'])
        self.assertEqual(tail(self.notes), ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                            'Do'])
        self.assertEqual(tail(self.multiples), [3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_1_C_last(self):
        self.assertEqual(last(self.months), 'Dec')
        self.assertEqual(last(self.notes), 'Do')
        self.assertEqual(last(self.multiples), 27)

    def test_1_D_init(self):
        self.assertEqual(init(self.months), ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                                             'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                             'Nov'])
        self.assertEqual(init(self.notes), ['Do', 'Re', 'Mi', 'Fa', 'So', 'La',
                                            'Ti'])
        self.assertEqual(init(self.multiples), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_1_E_first_three(self):
        self.assertEqual(first_three(self.months), ['Jan', 'Feb', 'Mar'])
        self.assertEqual(first_three(self.notes), ['Do', 'Re', 'Mi'])
        self.assertEqual(first_three(self.multiples), [0, 3, 6])

    def test_1_F_last_five(self):
        self.assertEqual(last_five(self.months), ['Aug', 'Sep', 'Oct', 'Nov',
                                                  'Dec'])
        self.assertEqual(last_five(self.notes), ['Fa', 'So', 'La', 'Ti', 'Do'])
        self.assertEqual(last_five(self.multiples), [15, 18, 21, 24, 27])

    def test_1_G_middle(self):
        self.assertEqual(middle(self.months), ['Mar', 'Apr', 'May', 'Jun', 'Jul',
                                               'Aug', 'Sep', 'Oct'])
        self.assertEqual(middle(self.notes), ['Mi', 'Fa', 'So', 'La'])
        self.assertEqual(middle(self.multiples), [6, 9, 12, 15, 18, 21])

    def test_1_H_inner_four(self):
        self.assertEqual(inner_four(self.months), ['Mar', 'Apr', 'May', 'Jun'])
        self.assertEqual(inner_four(self.notes), ['Mi', 'Fa', 'So', 'La'])
        self.assertEqual(inner_four(self.multiples), [6, 9, 12, 15])

    def test_1_I_inner_four_end(self):
        self.assertEqual(inner_four_end(self.months), ['Jul', 'Aug', 'Sep',
                                                        'Oct'])
        self.assertEqual(inner_four_end(self.notes), ['Mi', 'Fa', 'So', 'La'])
        self.assertEqual(inner_four_end(self.multiples), [12, 15, 18, 21])

    def test_1_J_replace_head(self):
        replace_head(self.months)
        replace_head(self.notes)
        replace_head(self.multiples)

        self.assertEqual(self.months, [42, 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, [42, 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti',
                                      'Do'])
        self.assertEqual(self.multiples, [42, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_1_K_replace_third_and_last(self):
        replace_third_and_last(self.months)
        replace_third_and_last(self.notes)
        replace_third_and_last(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 37, 'Apr', 'May', 'Jun',
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 37])
        self.assertEqual(self.notes, ['Do', 'Re', 37, 'Fa', 'So', 'La', 'Ti', 37])
        self.assertEqual(self.multiples, [0, 3, 37, 9, 12, 15, 18, 21, 24, 37])

    def test_1_L_replace_middle(self):
        replace_middle(self.months)
        replace_middle(self.notes)
        replace_middle(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 42, 37, 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 42, 37, 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 42, 37, 24, 27])

    def test_1_M_delete_third_and_seventh(self):
        delete_third_and_seventh(self.months)
        delete_third_and_seventh(self.notes)
        delete_third_and_seventh(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Apr', 'May', 'Jun', 'Aug',
                                       'Sep', 'Oct', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Fa', 'So', 'La', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 9, 12, 15, 21, 24, 27])

    def test_1_N_delete_middle(self):
        delete_middle(self.months)
        delete_middle(self.notes)
        delete_middle(self.multiples)

        self.assertEqual(self.months, ['Jan', 'Feb', 'Nov', 'Dec'])
        self.assertEqual(self.notes, ['Do', 'Re', 'Ti', 'Do'])
        self.assertEqual(self.multiples, [0, 3, 24, 27])

if __name__ == '__main__':
    unittest.main()
