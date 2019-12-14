import unittest
import HelloWorld

class testy_Hello(unittest.TestCase):
    def testy_Hello(self):
        wynik = HelloWorld.zwroc("HelloWorld")
        self.assertEqual(wynik,("HelloWorld"))

if __name__ == '__main__':
          unittest.main()
