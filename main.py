def nombre_de_voitures():
    compteur = 0

    for lettre1 in range(ord('K'), ord('Z') + 1):
        for lettre2 in range(ord('A'), ord('Z') + 1):
            for chiffre1 in range(10):
                for chiffre2 in range(10):
                    for chiffre3 in range(10):
                        for chiffre4 in range(1, 10000):
                            plaque = f"{chr(lettre1)}{chr(lettre2)} {chiffre1:04d}{chiffre2}{chiffre3}{chiffre4:04d}"
                            compteur += 1

    return compteur

resultat = nombre_de_voitures()
print(f"Le nombre de voitures possibles est : {resultat}")
