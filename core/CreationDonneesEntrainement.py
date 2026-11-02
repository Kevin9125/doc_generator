import requests
import json
import time

def ParseResponse(str_a_parse: str) -> tuple[str, str]:
    list_type_fichier = [("python", 6), ("rust", 5), ("C", 2)]
    rtn_type = ""
    for type_fichier in list_type_fichier :
        (lang, decalage) = type_fichier
        if str_a_parse.find(lang) != -1:
            start_code = str_a_parse.find(lang) + decalage
            rtn_type = lang
            break

    end_code = str_a_parse.rfind("```") - 1
    new_str = str_a_parse[start_code:end_code]
    return (new_str, rtn_type)

def CreationDonneesEntrainement(nb_recurence: int):

    #Initialisation
    API_KEY = ""
    API = ""

    #analyseur = AnalyseurCode(["py"])
    dict_fichier = {
        "python" : "py",
        "C" : "c",
        "rust" : "rs"
        }

    #Creation de la requête à envoyer à l'IA
    header = {
        "Authorization" : f"Bearer {API_KEY}",
        "Content-Type" : "application/json"
        }

    body = {
        "model" : "recursive/flint-v1.0:free",
        "messages" : [
            {
                "role":"user", 
                "content": "Salut, Je souhaite copier ta reponse directement dans un fichire de code. Peux-tu me créer un fichier de code d'exemple contenant au moins une classe et deux methodes dans l'un de ces trois langages : C, Python, Rust sans commentaire et qui soit assez complexe stp ? Essaye d'être original c'est pour entrainer un modele ?"
             }
            ],
        "temperature" : 0.7
        }

    #Envoie de la requete
    reponse = requests.post(API, headers=header, data=json.dumps(body))

    if reponse.status_code == 200:
        result = reponse.json()
        (code, type_fichier) = ParseResponse(result["choices"][0]["message"]["content"])
        extension = dict_fichier[type_fichier]
        f = open(f"./core/fichiers_code_entrainement/fichier_entrainement{nb_recurence}.{extension}", "w+")
        f.write(code)
        nb_recurence = nb_recurence + 1
   
    else:
        print("Erreur :", reponse.status_code)
        print(reponse.text)
        time.sleep(10)

    if nb_recurence < 10:
        CreationDonneesEntrainement(nb_recurence)

    #Enregistrement de la réponse dans un fichier
