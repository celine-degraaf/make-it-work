"""
Dit programma oefent met ingebouwde functies in Python.

Naam: Celine de Graaf
"""

"""
Dit programma oefent met het formatteren van strings in Python.

Naam: Celine de Graaf
"""

# 1. Printen op 3 regels op 3 manieren
print("Methode:\nVoornaam:\nAchternaam:")
print("Methode:")
print("Voornaam:")
print("Achternaam:")
print("""Methode:
Voornaam:
Achternaam:""")

# 2. f-string met naam en leeftijd
naam = "Celine"
leeftijd = 22
print(f"Mijn naam is {naam} en ik ben {leeftijd} jaar.")

# 3. Afgeronde waarde van pi
pi = 3.14159
print(f"De waarde van pi is ongeveer {pi:.2f}.")
# Andere manier van afronden:
print("Met round():", round(pi, 2))

# 4. Print dubbele aanhalingstekens mee
print('Jan zegt: "Hallo!"')

# 5. format()-methode
stad = "Amsterdam"
temperatuur = 20
print("Het is {} graden in {}.".format(temperatuur, stad))

# 6. Gecentreerde f-string
fruit = "Appel"
groente = "Broccoli"
print(f"{groente:^40}")
print(f"{fruit:^40}")

# 7. String in verschillende hoofdlettervormen
zin = "Python is leuk"
print(zin.title())      # Elk woord begint met een hoofdletter
print(zin.upper())      # Alles in hoofdletters
print(zin.lower())      # Alles in kleine letters

# 8. Tijdstip in f-string
dag = "vrijdag"
tijd = "16:00"
print(f"Onze afspraak is op {dag} om {tijd}.")

# 9. Tabeluitlijning met f-strings
print(f"{'Voornaam':<10} {'Achternaam':<10} {'Titel'}")
print(f"{'Arjen':<10} {'Lubach':<10} {'De Avondshow'}")