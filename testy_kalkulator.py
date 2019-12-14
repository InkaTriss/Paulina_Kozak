import unittest
import prKalkulator

class testy_kalkulator(unittest.TestCase):
    def test_dodawanie(self):
        wynik = prKalkulator.dodaj(2,3)
        self.assertEqual(wynik,5)
        self.assertNotEqual(wynik,2)

    def test_odejmowanie(self):
        wynik = prKalkulator.odejmij(5,3)
        self.assertEqual(wynik,2)
        self.assertNotEqual(wynik,3)

    def test_mnozenia(self):
        wynik = prKalkulator.iloczyn(2,3)
        self.assertEqual(wynik,6)
        self.assertNotEqual(wynik,4)

    def test_dzielenia(self):
        wynik = prKalkulator.iloraz(6,3)
        self.assertEqual(wynik,2)
        self.assertNotEqual(wynik,4)

if __name__ == '__main__':
    unittest.main()
