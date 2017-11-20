#coding: utf-8

import unittest
import nome_modulo
#from nome_modulo import Classe1, Classe2, funcao1, funcao2

'''
METHOD                      CHECKS THAT
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)
assertRaises(e, f, p1, p2)  f(p1, p2) raises exception e
'''

class TestExemploDeTeste(unittest.TestCase):

    def setUp(self):
        self.objeto1 = nome_modulo.Classe1()

    def tearDown(self):
        del self.objeto1

    def test_executar_um_metodo(self):
        param1 = 'um texto'
        param2 = 42
        self.assertEqual(self.objeto1.funcao1(param1, param2), 'valor previsto')

if __name__=='__main__':
    unittest.main()