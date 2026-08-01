from core.Fichier import Fichier

def main() -> None:
    fichier_test = Fichier("test.txt")

    #test lecture
    #result_texte, result_code = fichier_test.read_file('r')
    #print(result_texte)
    #print(result_code)

    #test ecriture 
    #result_msg, result_int = fichier_test.write_file("texte ecrit avec le code")
    #print(result_int)
    #print(result_msg)

    #test identification fichier
    print(fichier_test.identifie_file())

if __name__ == "__main__":
    main()