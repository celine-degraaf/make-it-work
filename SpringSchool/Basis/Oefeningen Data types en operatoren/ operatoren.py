"""
Dit programma oefent met data types en operatoren in Python.

Naam: Celine de Graaf
"""

# 1. Twee integers optellen
getal1 = 15
getal2 = 27
som = getal1 + getal2
print(f"De som van {getal1} en {getal2} is: {som}")

# 2. Twee strings aan elkaar plakken
voornaam = "Emma"
achternaam = "Jansen"
volledige_naam = voornaam + " " + achternaam
print(f"De volledige naam is: {volledige_naam}")

# 3. Drie floats vermenigvuldigen en delen
getalA = 3.0
getalB = 1.5
getalC = 2.0
resultaat = (getalA * getalB) / getalC
print(f"Het resultaat van ({getalA} * {getalB}) / {getalC} is: {resultaat}")

# 4. Twee floats delen en converteren naar een integer
waarde1 = 7.5
waarde2 = 1.0
deling = waarde1 / waarde2
deling_als_integer = int(deling)
print(f"{waarde1} gedeeld door {waarde2} als integer is: {deling_als_integer}")