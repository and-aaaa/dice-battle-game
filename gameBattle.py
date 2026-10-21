import random
import time


from gameCharacter import Character, Magician, Rogue, Warrior

class Game():
    player = "player"
    player_class = 0
    enemy = "enemy"
    enemy_class = 0
    player = "player"

    def display(self):
        player_hp = self.player.hp
        player_max_hp = self.player.max_hp 
        enemy_hp = self.enemy.hp
        enemy_max_hp = self.enemy.max_hp 
        
        print (f"player         enemy\n{player_hp} / {player_max_hp}         {enemy_hp} / {enemy_max_hp}")

    def run(self):
        print("===== ROUND 1 =====")
        player_class = int(input("캐릭터의 직업을 선택해주세요 : 1 (전사) 2 (도적) 3 (마법사)"))
        self.player_class = player_class
        if player_class == 1:
            self.player = Warrior()
        elif player_class == 2:
            self.player = Rogue()
        elif player_class == 3:
            self.player = Magician()
        
        self.enemy_class = random.randint(1,3)
        if self.enemy_class == 1:
            self.enemy = Warrior()
        elif self.enemy_class == 2:
            self.enemy = Rogue()
        elif self.enemy_class == 3:
            self.enemy = Magician()
        self.display()
