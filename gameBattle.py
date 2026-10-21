from dice_game.gameCharacter import Character, Magician

class Game():
    player = ""
    enemy = ""

    def display(self):
        player_hp = self.player.hp
        player_max_hp = self.player.max_hp 
        enemy_hp = self.player.hp
        enemy_max_hp = self.player.max_hp 
        
        print (f"player         enemy\n{player_hp} / {player_max_hp}         {enemy_hp} / {enemy_max_hp}")

test = Magician()
test.heal()
print(test.roll())
