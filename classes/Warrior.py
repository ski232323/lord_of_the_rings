class Warrior:
    def __init__(self, nom):
        self.inventory = Inventory()
        self.nom = nom
        self.pv = 1000
        self.is_alive = True

    def add_weapon(self, name, quantity=1):
        self.inventory.weapon[name] = quantity
    
    def show_pv(self):
        print(f"J'ai {self.pv} pv!")

    def punch(self, victim):
        damage = 5
        victim.pv -= damage
        print(f"{self.nom} attaque {victim.nom} et inflige {damage} dégâts !")

    def verify_if_alive(self):
        if self.pv > 0:
            return True
        else:
            self.is_alive = False
            return False


