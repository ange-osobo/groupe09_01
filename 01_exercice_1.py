class MiniProfil:
    def run(self):
        prenom = input("Prénom : ")
        age = int(input("Âge : "))
        ville = input("Ville : ")
        metier = input("Métier : ")
        jours = age * 365
        print(f"Profil : {prenom}, {age} ans ({jours} jours), habite à {ville}, exerce {metier}.")
