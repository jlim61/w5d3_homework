from unittest import TestCase, main
from whiteboard import check_surv

class TestCheckSurv(TestCase):

    def test_all_defenders_win(self):
        self.assertTrue(check_surv([1, 3, 5, 7], [2, 4, 6, 8]))

    def test_unequal_array_length(self):
        self.assertFalse(check_surv([1, 3, 5, 7], [2, 4]))

    def test_some_defenders_win(self):
        self.assertTrue(check_surv([1, 3, 5, 7], [2, 4, 0, 8]))

    def test_tie_with_attack_power(self):
        self.assertTrue(check_surv([1, 3], [3, 1]))

    def test_tie_attackers_win(self):
        self.assertFalse(check_surv([2, 4], [1, 3]))

if __name__ == '__main__':
    main()