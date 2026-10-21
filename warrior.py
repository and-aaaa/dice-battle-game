from character import Character

class warrior(Character):
    def __init__ (self):
        super().__init__(self, hp =100, max_hp = 100, name="Warrior", dice_num = 2) # 자식 속성 추가
    
    # 오버라이딩
    def attack(self, other):
        damage = 0
    # 주사위 굴리기
        dice_result = self.roll()
        dice1 = int(dice_result[0])
        dice2 = int(dice_result[1])
    # 주사위값 판정후 데미지 결정
    # 주사위값이 같으면 합산후 2배 대미지
        if dice1 == dice2:
            damage = dice1 * 4
            print("주사위 값이 같습니다! 2배 대미지!")
        else:
            damage = sum(dice_result)

    #데미지 적용
        other.hp -= damage
        #오버라이딩
    def heal(self):
        heal = 0
      # 주사위 값 받아오기
        dice_result = self.roll()
        dice1 = int(dice_result[0])
        dice2 = int(dice_result[1])
        # 주사위 판정후 힐량 결정
        # 주사위값이 같으면 50추가 힐
        if dice1 == dice2:
            heal += 50
            print("주사위 값이 같습니다! 50 추가 힐!")
        else:
            heal = heal + dice1 + dice2
        # 힐 적용
        if hp + heal > max_hp:
            self.hp = max_hp
        else:
            self.hp += heal
