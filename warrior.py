from character import Character

class warrior(Character):
    def __init__ (self, hp, max_hp = 100, name, dice_num = 2):
        super().__init__(max_hp, dice_num) # 자식 속성 추가
    
    # 오버라이딩
   def attack(self, other):
    # 주사위 값 받아오기
    damage = 0
    dice_result = self.roll()
    dice1 = int(dice_result[0])
    dice2 = int(dice_result[1])
    # 주사위값 판정후 데미지 결정
    if dice1 == dice2:
        damage = dice1 * 4
    else:
        damage = sum(dice_result)
      # Line 21 나중에 수정 필요 (damage = sum(dice_result))
    #데미지 적용
        other.hp -= damage
        #오버라이딩
    def heal(self):
        heal = 0
      # 주사위 값 받아오기
        dice_result = self.roll()
        dice1 = int(dice_result[0])
        dice2 = int(dice_result[1])
        #주사위 판정후 힐 결정
        if dice1 == dice2:
            heal += 50
        else:
            heal = heal + dice1 + dice2
        # 힐 적용
        if hp + heal > max_hp:
            hp = max_hp
        else:
            hp += heal
