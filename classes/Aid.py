class Aid(Warrior):
    def __init__(self, nom):
        super().__init__(nom)

    def aid(self, victim):
        heal_amount = random.randint(1, 15)
        victim.pv += heal_amount
        print(f'{self.nom} a guéri {victim.nom} de {heal_amount}pv')
