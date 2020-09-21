import unittest
import mayusculas

class TestMayusculas(unittest.TestCase):
    
    def test_one_word(self):
        texto = 'python'
        resultado = mayusculas.mayusculasTexto(texto)
        self.assertEqual(resultado,'Python')
    
    def test_multiple_words(self):
        texto = 'python es super facil'
        resultado = mayusculas.mayusculasTexto(texto)
        self.assertEqual(resultado,'Python Es Super Facil')

if __name__ == "__main__":
    unittest.main()