class Troll(Warrior):
    def __init__(self, nom):
        super().__init__(nom)
        self.shield = random.choice(["wood", "iron"])

    def pickaxe(self, victim):
        if self.shield == "wood":
            if self.pv <= 100:
                self.pv += 5
            damage = random.randint(10, 20)
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
        if self.shield == "iron":
            if self.pv <= 100:
                self.pv += 10
            damage = random.randint(10, 20)
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")
