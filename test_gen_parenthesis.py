from unittest import TestCase

from GenerateParenthesis import gen_parenthesis_recur, gen_parenthesis_naive, gen_parenthesis_iter


class TestGenParenthesis(TestCase):
    def test_gen_parenthesis_recur(self):
        for n in (range(1, 6)):
            self.assertEqual(gen_parenthesis_recur(n), gen_parenthesis_naive(n))

    def test_gen_parenthesis_iter(self):
        for n in (range(1, 6)):
            self.assertEqual(gen_parenthesis_iter(n), gen_parenthesis_naive(n))

    def test_gen_parenthesis_recur_iter(self):
        for n in (range(1, 12)):
            self.assertEqual(gen_parenthesis_recur(n), gen_parenthesis_iter(n))
