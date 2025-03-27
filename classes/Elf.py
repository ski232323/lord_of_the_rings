class Elf(Warrior):
    def __init__(self, nom):
        super().__init__(nom)
        """
         Remplacer bow_type par un dictionnaire avec comme clé l'arme et comme valeur un random.radint() adapté à l'arme pour éviter les 3 conditions en ajoutant l'arme"
         """
        bow_type = random.choice(["leather bow", "wood bow", "iron bow"])
        if bow_type == "leather bow":
            self.add_weapon("leather bow", random.randint(15, 25))
        elif bow_type == "wood bow":
            self.add_weapon("wood bow", random.randint(30, 35))
        elif bow_type == "iron bow":
            self.add_weapon("iron bow", random.randint(40, 45))
        
    def __repr__(self):
        return f"Je suis un elf appelé {self.nom} j'ai {self.pv}pv et et voici ce que je possède{self.inventory}"

    def arrow(self, victim):
        for bow, damage in self.inventory.weapon.items():
            victim.pv -= damage
            print(f"{self.nom} attaque {victim.nom} avec un {bow} et inflige {damage} dégâts !")
            break  # Sortir de la boucle après avoir utilisé la première arme
