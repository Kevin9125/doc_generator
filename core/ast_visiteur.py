import ast

#les methodes surchargées de la classe NodeVisitor de type visit_<typeNoeud> sont appelées 
#à chaque rencontre de ce type de noeux dans l'AST(Abstract Syntax Tree)
class AST_Visiteur(ast.NodeVisitor):

    def __init__(self):
        self.info_fichier = {}
        self.compteur_class = None
        self.list_nom_class = []
    
    def reset_visiteur(self):
        self.info_fichier = {}

    def setup_new_class(self, nom_class : str):
        if self.compteur_class == None:
            self.compteur_class = 0
        else:
            self.compteur_class = self.compteur_class + 1
        
        dictionnaire = {}
        self.info_fichier[nom_class] = dictionnaire
        self.list_nom_class.append(nom_class)
    
    def visit_ClassDef(self, node):
        self.setup_new_class(node.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        classe_actuelle = self.list_nom_class[self.compteur_class]
        parametres = {
            "arguments" : []
            }

        #defini une entrée "methodes" dans le dictionnaire si elle n'existe pas déjà
        if not "methodes" in self.info_fichier[classe_actuelle]:
            self.info_fichier[classe_actuelle]["methodes"] = {}
        
        for arg in node.args.args:
            parametres["arguments"].append(arg.arg)

        if node.returns is None:
            parametres["retour"] = "None"

        elif hasattr(node.returns, "value"):
            parametres["retour"] = str(node.returns.value)

        else:
            parametres["retour"] = str(node.returns.id)

        self.info_fichier[classe_actuelle]["methodes"][node.name] = parametres

    def visit_Assign(self, node):

        classe_actuelle = self.list_nom_class[self.compteur_class]

        #defini une entrée "attributs" dans le dictionnaire si elle n'existe pas déjà
        if not "attributs" in self.info_fichier[classe_actuelle]:
            self.info_fichier[classe_actuelle]["attributs"] = {}

        self.info_fichier[classe_actuelle]["attributs"][node.targets[0].id] = node.value.value






