# Fonction qui permet d'ajouter deux nombres
def add(a, b):
    return a + b


# Condition qui permet d'exécuter le code uniquement si le fichier addition.py est exécuté comme fichier principal
# Quand on fait python addition.py, ce code s'exécute
# Sinon cela voudra dire que le fichier est importé depuis un autre fichier python
if __name__ == "__main__":
    print(__name__)
    num1 = float(input("Saisir le premier nombre: "))
    num2 = float(input("Saisir le second nombre: "))
    resultat = add(num1, num2)
    print(f"Le résultat de l'addition de {num1} par {num2} est de: {resultat}")
else:
    # Lorsque le fichier est importé comme un module
    # Il ne porte pas le nom __main__ mais addition (le nom du fichier)
    print(__name__)
