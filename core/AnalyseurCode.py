import json
import os
import ast
from . import Result
from . import ast_visiteur

class AnalyseurCode:

    def __init__(self, formats_accepter : list[str]) -> None:
        self.formats_accepter = formats_accepter
    
    #Filtre les fichiers en fonction de si ils existent et si ils sont dans le bon format
    def VerificationFichiers(self, fichiers : list[str], result: Result.Result) -> Result.Result:  
        
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

                    for var in self.formats_accepter:
                        if var == fichier[index+1:]:
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

        #Initialisation
        contenu = ""
        visiteur = ast_visiteur.AST_Visiteur()
        result = Result.Result()
        data = {}
        last_index = 0

        result = self.VerificationFichiers(fichiers, result)

        for i in range(0, len(fichiers)):
            contenu = open(fichiers[i]).read()

            #Retire le chemin du fichier dans son nom
            last_occurence = fichiers[i].rfind('/')
            nom_fichier = fichiers[i][last_occurence + 1:]

            #Analyse des fichiers
            tree = ast.parse(contenu, filename=fichiers[i])
            visiteur.visit(tree)
            data[nom_fichier] = visiteur.info_fichier
            visiteur.reset_visiteur()
        
        #Construction du JSON
        json_data = json.dumps(data, indent=4)
        result.data = json_data
        return result
        