class FicheProduit:
    def run(self):
        nom = input("Nom du produit : ")
        prix = float(input("Prix (€) : "))
        stock = int(input("Stock : "))
        remise = float(input("Remise (%) : "))
        prix_final = prix * (1 - remise/100)
        print(f"{nom} – Prix final : {prix_final:.2f}€, Stock restant : {stock}")

