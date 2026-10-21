import random

dice_result = []

class Character():
  def __init__(self):
    self.hp = hp
    self.max_hp = max_hp
    self.name = name
    self.dice_num = dice_num

  def roll(self):
      dice_num = self.dice_num
      for i in range (dice_num):
          dice_result.append(random.randint(1, 6))
      return dice_result

    
  def attack(self):
    damage = sum(
    other
  def heal(self):
      
