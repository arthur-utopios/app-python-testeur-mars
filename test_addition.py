import unittest
from addition import add

class TestAddition(unittest.TestCase):
    def test_add_integers(self):
        # assertEquals(fonction à tester, résultat qu'on est sensé obtenir)
        self.assertEqual(add(1, 2), 3)
    
    def test_add_floats(self):
        self.assertEqual(add(1.5, 2.5), 4.0)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

# Si mon fichier est exécute comme fichier principal "python test_addition.py"
# le code ci-dessous sera exécuté
if __name__ == '__main__':
    unittest.main()