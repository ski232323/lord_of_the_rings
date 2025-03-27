class Inventory:
    def __init__(self):
        self.weapon = dict()
        self.epic_weapon = set()

    def add_weapon(self, name, quantity=1):
        self.weapon[name] = self.weapon.get(name, 0) + quantity
    
    def del_weapon(self, name, quantity):
        if name in self.weapon:
            self.weapon[name] -= quantity
            if self.weapon[name] <= 0:
                del self.weapon[name]
        else:
            print(f"{name} n'existe pas dans l'inventaire.")
    def __str__(self):
        contenu=f"\nInventaire\n"
        for bow,damage in self.weapon.items() :
            contenu+=f"{bow} qui inflige {damage} dégâts"
        return contenu


    def add_epic_object(self, name):
        self.epic_weapon.add(name)

