"""Programme qui détermine si une chaîne de caractères est un palindrome."""


def ispalindrome(p:str)->bool: # Fonction secondaire
    """Détermine si p est un palindrome."""

    phrase=p.lower() # Remplace les majuscules par des minuscules
    table = str.maketrans("éèêëàïîçùüûôö", "eeeeaiicuuuoo", " '-_.?!:;,&") # Table des changements
    txt=phrase.translate(table)
    if txt[:]==txt[::-1]: #Compare si le mot est un palindrome
        return True # p est un palindrome
    return False # p n'est pas un palindrome


def main(): # Fonction principale
    """Test si les mots de la liste sont des palindromes."""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
