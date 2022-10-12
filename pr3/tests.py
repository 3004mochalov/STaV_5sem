import unittest
import matrix
import numpy as np


A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

res_add = np.array([[10, 10, 10],
                    [10, 10, 10],
                    [10, 10, 10]])

res_mul = np.array([[30, 24, 18],
                    [84, 69, 54],
                    [138, 114, 90]])

A_1 = np.array([[1, 2],
               [3, 4]])

res_A_1 = np.array([[-2, 1],
                    [1.5, 0.5]])

res_sv = np.array([-0.3722813232690143, 5.372281323269014])


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(matrix.add(A, B).all(), res_add.all())

    def test_mul(self):
        self.assertEqual(matrix.mul(A, B).all(), res_mul.all())

    def test_inv(self):
        self.assertEqual(matrix.inverse(A_1).all(), res_A_1.all())

    def test_sv(self):
        self.assertEqual(matrix.eigen_values(A_1).all(), res_sv.all())


if __name__ == "__main__":
    unittest.main()