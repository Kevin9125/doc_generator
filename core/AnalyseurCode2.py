from tree_sitter import Parser, Language, Query, QueryCursor
from . import Result
import tree_sitter_python
import tree_sitter_c
import tree_sitter_rust

class FormatFichier:
    def __init__(self, extension : str, modele_parser : Language):
        self.extension = extension
        self.modele_parser = modele_parser

class AnalyseurCode2:
    def __init__(self):

        self.PYTHON = FormatFichier("py", Language(tree_sitter_python.language()))
        self.C = FormatFichier("c",  Language(tree_sitter_c.language()))
        self.RUST = FormatFichier("rs", Language(tree_sitter_rust.language()))
        
        self.formats = {
            "Python" : self.PYTHON,
            "C" : self.C,
            "Rust": self.RUST
            }

    #Filtre les fichiers en fonction de si ils existent et si ils sont dans le bon format
    def VerificationFichiers(self, fichiers: list[str], result: Result.Result) -> Result.Result:  
        
        #Initialisation
        files_not_found = []
        liste_mauvais_format = []
        
        if fichiers != None and len(fichiers) > 0:

            #on utilise une copy de la liste afin de pouvoir supprimer des elements dans la liste sans affecter la liste parcouru
            for fichier in fichiers.copy():

                #Verifie si le fichier existe et peut être ouvert
                try:
                    open(fichier)

                except FileNotFoundError:
                    result.result_code = -1
                    files_not_found.append(fichier)
                    fichiers.remove(fichier)

                except:
                    result.result_code = -1
                    result.msg = f"an unregister exception as been raise, try to join the creator of the product"
                    break
                
                else:
                    #verifie si le type de fichier est accepté
                    index = fichier.rfind('.')
                    is_accepted = False

                    for key in self.formats:
                        if key.extension == fichier[index+1:]:
                            is_accepted = True
                            break

                    if is_accepted == False:
                            liste_mauvais_format.append(fichier)
                            fichiers.remove(fichier)

            if len(files_not_found) > 0 or len(liste_mauvais_format) > 0:
                result.msg = f"{files_not_found} as not been found, please check the path of those files and retry. {liste_mauvais_format} are not code files, please put code file in this function"
            
            return result

        elif fichiers == None:
           raise ValueError("la variable ne peut pas être None")

        else:
           raise ValueError("La liste est vide")

    #Analyse les fichiers passer en paramètre et resort les principales classes avec leurs attributs et méthodes
    def AnalyseFichiers(self, fichiers : list[str]) -> tuple[Result.Result, str]:

        for fichier in fichiers:
            index = fichier.rfind('.')
            file_extension = fichier[index+1:]
            format_fichier = None
            parser = None
            query = None
            contenu = ""
            
            for key in self.formats:
                if self.formats[key].extension == file_extension:
                      format_fichier = self.formats[key]
                      parser = Parser(format_fichier.modele_parser)
                      break

            with open(fichier) as file:
                contenu = file.read()

            tree = parser.parse(bytes(contenu, "utf8"))
            query = Query(format_fichier.modele_parser, "(function_definition name: (identifier) @function.name)")
            cursor = QueryCursor(query)
            matches = cursor.matches(tree.root_node)
            print(matches[0][1]["function.name"][0].text)
        




