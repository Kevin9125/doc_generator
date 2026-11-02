import unittest
import filecmp
import os
import json
from core.AnalyseurCode import AnalyseurCode
from core.exceptions import MauvaisFormatFichierException

class test_AnalyseurCode(unittest.TestCase):

    def setUp(self):
        self.list_fichier = []
        self.analyseur = AnalyseurCode(["py"])

    def test_passage_fichiers_valide(self):
        verif_data = ""
        self.list_fichier.append("test1.py")

        result = self.analyseur.AnalyseFichiers(self.list_fichier)
        with open("tests/verif_json_solo.json", "r") as file:
            verif_data = file.read()

        verif_data_json = json.dumps(verif_data, indent=4)

        stripped_verif_data = verif_data_json.strip()
        stripped_result_data = result.data.strip()
        self.assertEqual(stripped_verif_data, stripped_result_data, "verif_data is not equal to data")
        

    def test_passage_liste_vide(self):
        with self.assertRaises(ValueError):
            self.analyseur.AnalyseFichiers(self.list_fichier)
        
    def test_passage_plusieurs_fichiers_valide(self):
        verif_data = ""
        self.list_fichier.append("test1.py")

        result = self.analyseur.AnalyseFichiers(self.list_fichier)
        with open("tests/verif_json_plusieurs.json", "r") as file:
            verif_data = file.read()

        verif_data_json = json.dumps(verif_data, indent=4)

        self.assertEqual(verif_data_json, result.data, "verif_data is not equal to data")

    def test_passage_fichier_inexistant(self):
        self.list_fichier.append("test1.py")
        self.list_fichier.append("fichier_inexistant.py")
        with self.assertRaises(FileNotFoundError):
            self.analyseur.AnalyseFichiers(self.list_fichier)

    def test_passage_fichier_texte(self):
        self.list_fichier.append("test1.py")
        self.list_fichier.append("test3.txt")
        with self.assertRaises(MauvaisFormatFichierException):
           self.analyseur.AnalyseFichiers(self.list_fichier)

    def test_passage_liste_null(self):
        with self.assertRaises(ValueError):
           self.analyseur.AnalyseFichiers(None)

if __name__ == '__test_AnalyseurCode__':
    unittest.main()
