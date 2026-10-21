from character import Character

class Magician(Character):
    def __init__(self):
        super().__init__(
            hp = 50,
            max_hp = 50,
            name = "Magician",
            dice_num = 3
        )

    def attack(self, other):
        dice_result = self.roll()
        print(self.name, "님이 주사위", dice_result, "을 굴렸습니다.")

        # 공격01
        if dice_result == [6, 6, 6]:
            damage = 1000
            print("궁극의 마법! 데미지", damage, "적용~!")

        # 공격02
        elif dice_result == [1, 1, 1]:
            self.hp = 0
            print("마법의 역류;;; 체력이", self.hp, "가 되었습니다ㅠㅠ")
            return # 게임종료
        # 공격03
        elif (all(idx % 2 == 0 for idx in dice_result)  # 짝수
              or all(n % 2 == 1 for n in dice_result)): # 홀수
            damage = sum(dice_result) * 2
            print("세 주사위의 홀짝이 모두 같습니다! 데미지 2배 적용~!")

        # 공격04
        elif (dice_result == [1, 2, 3]
              or dice_result == [2, 3, 4]
              or dice_result == [3, 4, 5]
              or dice_result == [4, 5, 6]):
            damage = 45
            print("연속 수!! 데미지 45 적용~!")

        # 공격05
        else:
            damage = max(dice_result)

    def heal(self):
        dice_result = self.roll()
        
        # 회복01
        if (dice_result == [1, 1, 1]
              or dice_result == [2, 2, 2]
              or dice_result == [3, 3, 3]
              or dice_result == [4, 4, 4]
              or dice_result == [5, 5, 5]
              or dice_result == [6, 6, 6]):
            self.hp = 50
            print("체력이 전체 회복되었습니다~!")
            print("현재 체력: ", self.hp)

        # 회복02
        elif (all(idx % 2 == 0 for idx in dice_result)  # 짝수
              or all(n % 2 == 1 for n in dice_result)): # 홀수
            if (self.hp <= 20):
                self.hp += 30
            print("체력이 ", self.hp, "만큼 회복되었습니다~!")
            print("현재 체력: ", self.hp)
