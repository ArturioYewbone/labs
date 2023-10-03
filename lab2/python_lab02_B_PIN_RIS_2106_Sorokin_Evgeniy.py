import random
from mclass import Warrior


# Создаем двух воинов
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.is_alive() or warrior2.is_alive():
    # Выбираем случайного воина для атаки
    attacker = random.choice([warrior1, warrior2])
    enemy = warrior1 if attacker == warrior2 else warrior2
    
    # Воин атакует
    attacker.attack(enemy)

# Проверяем, кто победил
if warrior1.is_alive():
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")
