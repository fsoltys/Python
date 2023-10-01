from Matrix import Matrix
import numpy.linalg
import numpy
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrixA = Matrix(2, 2)  # przykladowa poprawna macierz
        self.matrixA.fill_matrix(2, 4, 1, 6)

    def testValue(self):
        with self.assertRaises(ValueError):
            self.matrixB = Matrix(-3, -2)

    def testType(self):
        with self.assertRaises(TypeError):
            self.matrixB = Matrix('a', 'z')

    def test_if_det_not_0(self):
        self.assertNotEqual(numpy.linalg.det(self.matrixA.A), 0)

    def test_if_square_matrix(self):
        self.assertEqual(self.matrixA.n, self.matrixA.m)


if __name__ == "__main__":
    unittest.main()
