class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20

    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}!")
        enemy.health -= self.damage
        print(f"{enemy.name} осталось здоровья: {enemy.health}")

    def is_alive(self):
        return self.health > 0