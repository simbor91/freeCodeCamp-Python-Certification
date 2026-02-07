# 06 Objects-Oriented Programming (OOP)
    # OOP and Encapsulation
# Lab: Build a Game Character Stats Tracker

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    # name getter
    @property
    def name(self):
        return self._name

    # health getter and setter
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, new_health):
        if new_health < 0 or new_health > 100:
            print('Health should be a value between 0 and 100')
        if new_health < 0: new_health = 0
        if new_health > 100: new_health = 100
        self._health = new_health
    
    # mana getter and setter
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0 or new_mana > 50:
            print('Mana should be a value between 0 and 50')
        if new_mana < 0: new_mana = 0
        if new_mana > 50: new_mana = 50
        self._mana = new_mana

    # level getter
    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self._name} leveled up to {self._level}!')

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

character1 = GameCharacter('Zelda')
print(character1)
character1.health = 70
character1.mana = 30
print(character1)
character1.level_up()