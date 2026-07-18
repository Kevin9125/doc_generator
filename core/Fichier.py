from core.Result import Result

import magic

class Fichier():

    def __init__(self, fichier: str):
        self.fichier = fichier
    
    #ouvre le fichier passer en paramètre avec le mode de lecture passé en paramètre et retourne son contenu
    def read_file(self, mode_lecture: str) -> tuple[str, int]:
        result = Result.Successfull    
        try:
            with open(self.fichier, mode_lecture) as fichier:
                texte = fichier.read()
    
        except FileNotFoundError : 
            texte = "ce fichier n'existe pas essayer de voir si il n'y a pas d'erreur dans le nom et réessayer"
            result = Result.Error

        except PermissionError:
            texte = "vous n'avez par les permissions pour ouvrir ce fichier"
            result = Result.Error

        except Exception as e:
            texte = "erreur inatendu : {e}"
            result = Result.Error

        return (texte, result)
    
    #ecrit dans le fichier passer en paramètre et retourne le resultat de l'opération
    def write_file(self, write_texte : str) -> tuple[str, int]:

        texte = "ecriture dans le fichier réussit"
        result = Result.Successfull

        try:
            with open(self.fichier, 'w') as write_fichier:
                write_fichier.write(write_texte)
                
        except FileNotFoundError : 
            texte = "ce fichier n'existe pas essayer de voir si il n'y a pas d'erreur dans le nom et réessayer"
            result = Result.Error

        except PermissionError:
            texte = "vous n'avez par les permissions pour ouvrir ce fichier"
            result = Result.Error

        except Exception as e:
            texte = "erreur inatendu : {e}"
            result = Result.Error

        return (texte, result)
    
    def identifie_file(self) -> str:
        return str(magic.from_file("Result.py"))
