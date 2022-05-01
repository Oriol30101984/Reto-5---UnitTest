from model import Geometria
import unittest


class MyTestCase(unittest.TestCase):

    def test_areaCuadrado(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(1)
        self.assertEqual(result, 16)

    def test_areaCirculo(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(2)
        self.assertEqual(result, 3.1416 * pow(4.00, 2))

    def test_areaTiangulo(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(3)
        self.assertEqual(result, 10)

    def test_areaRectangulo(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(4)
        self.assertEqual(result, 20)

    def test_areaPentagono(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(5)
        self.assertEqual(result, 10)

    def test_areaRombo(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(6)
        self.assertEqual(result, 10)

    def test_areaRomboide(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(7)
        self.assertEqual(result, 20)

    def test_areaTrapecio(self):
        geo = Geometria.Geometria(4.00, 5.00, 6.00)
        result = geo.switch(8)
        self.assertEqual(result, ((4.00 + 5.00)/2)*6.00)


if __name__ == '__main__':
    unittest.main()
