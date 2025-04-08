"""
Dit programma oefent met ingebouwde functies zoals input(), print(), int() en f-strings.

Naam: Celine de Graaf
"""

# Opdracht 1: Vraag de naam van de gebruiker en begroet
naam = input('Wat is je naam? ')
print(f'Hallo, {naam}')
print()

# Opdracht 2: Vraag de leeftijd en bereken leeftijd over 10 jaar
leeftijd = int(input('Hoe oud ben je? '))
leeftijd_na_decennium = leeftijd + 10
print(f'Over 10 jaar ben je {leeftijd_na_decennium} jaar oud.')
print()

# Opdracht 3: Vraag drie getallen en print ze met ... ertussen
print('Voer drie getallen in')
getal1 = int(input('Eerste getal: '))
getal2 = int(input('Tweede getal: '))
getal3 = int(input('Derde getal: '))
print(getal1, getal2, getal3, sep='...')  # sep betekent "scheidingsteken"