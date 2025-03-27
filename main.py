 
 from time import sleep
 # Création des personnages
Legolas = Elf('Legolas')
Sauron = Troll('Sauron')
Elisabeth = Aid('Elisabeth')

# Combat

while Legolas.verify_if_alive() and Sauron.verify_if_alive():
    action = random.choice(["punch", "pickaxe"])
    if action == "punch":
        Sauron.punch(Legolas)
    else:
        Sauron.pickaxe(Legolas)

    action = random.choice(["punch", "arrow"])
    if action == "punch":
        Legolas.punch(Sauron)
    else:
        Legolas.arrow(Sauron)

    Elisabeth.aid(Legolas)

print(Legolas)
# Déclaration du vainqueur
if Legolas.verify_if_alive():
    print("Legolas a gagné")
else:
    print("Sauron a gagné")
sleep(5)