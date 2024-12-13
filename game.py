class gamecharacter:
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def display_info(self):
        print(f"character:{self.name}, health:{self.health}")
class warrior(gamecharacter):
    def __init__(self,name,health,weapon):
        super().__init__(name,health)
        self.weapon=weapon
    def attackpower(self):
        print(f"{self.name},the warrior,attacks with {self.weapon}")
class mage(gamecharacter):
    def __init__(self,name,health,spell):
        super().__init__(name,health)
        self.spell=spell
    def cast_spell(self):
        print(f"{self.name},the mage,casts {self.spell}")
warrior=warrior("aragon",100,"sword")
mage=mage("gandalf",80,"fireball")
print("game character & actions:")
warrior.display_info()
warrior.attackpower()
mage.display_info()
mage.cast_spell()