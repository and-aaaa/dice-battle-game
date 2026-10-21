import random

dice_result = []

class Character():
  def __init__(self, hp, max_hp, name, dice_num):
    self.hp = hp
    self.max_hp = max_hp
    self.name = name
    self.dice_num = dice_num

  def roll(self):
      dice_num = self.dice_num
      for i in range (dice_num):
          dice_result.append(random.randint(1, 6))
      return dice_result

    
  def attack(self, other):
      dice_result = self.roll()
      damage = sum(dice_result)
      other.hp -= damage

  def heal(self):
      
