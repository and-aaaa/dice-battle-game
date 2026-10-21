import random
import time

class Character():
  def __init__(self, hp, max_hp, name, dice_num):
    self.hp = hp
    self.max_hp = max_hp
    self.name = name
    self.dice_num = dice_num

  def roll(self):      
      dice_num = self.dice_num
      dice_result = []
      for i in range (dice_num):                    # 캐릭터에 따라 주사위 추가 굴림이 발생할 수 있음. 
          d = random.randint(1, 6)
          dice_result.append(d)
          print(f"{d}가 나왔습니다!")
          time.sleep(0.5)
      return dice_result
    
  def attack(self, other):
      dice_result = self.roll()
      damage = sum(dice_result)
      # Line 21 나중에 수정 필요 (damage = sum(dice_result))
      other.hp -= damage

  def heal(self):
      pass
  
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
            temp_hp = self.hp
            if (self.hp <= 20):
                self.hp += 30
            else:
                self.hp = 50
            print("체력이 ", self.hp - temp_hp, "만큼 회복되었습니다~!")
            print("현재 체력: ", self.hp)

        # 회복03
        else:
            temp_hp = self.hp
            self.hp += sum(dice_result)

            if self.hp > self.max_hp:
                self.hp = self.max_hp

            print("체력이", self.hp - temp_hp, "만큼 회복되었습니다~!")
            print("현재 체력: ", self.hp)


class Rogue (Character):
    def __init__(self):
        self.name = "Rogue"
        self.hp = 75
        self.max_hp = 75
        self.dice_num = 2            
# 기존 로직과 완전히 동일
#    def roll(self):

    def attack(self, other):
        dice_result = self.roll()
        # 두 눈의 홀짝이 같은 경우, 두 눈 중 큰 것을 데미지로 + 주사위 1번 더 굴려 데미지 추가 
        if dice_result[0]%2 == dice_result[1]%2: 
            damage = max(dice_result)
            print(f"두 눈의 홀짝이 같습니다! 연타!\n1차 대미지 : {damage}!")
            time.sleep(0.5)
            print("주사위를 한 번 더 굴립니다")
            time.sleep(0.5)
            d = random.randint(1, 6) 
            damage += d
            print(f"{d}가 나왔습니다!\n2차 대미지 : {d}!" )
            time.sleep(0.5)
        else : 
            max_d = max(dice_result)
            damage = max_d
            print(f"일반공격!\n1차 대미지 : {max_d}!")
            time.sleep(0.5)
        other.hp -= damage            
        return damage

    def heal(self):
        dice_result = self.roll()
        # 두 눈의 홀짝이 같은 경우, 20 회복
        if dice_result[0]%2 == dice_result[1]%2: 
            self.hp += 20 
            if self.hp > self.max_hp:
                self.hp = self.max_hp  
            print(f"두 눈의 홀짝이 같습니다! 슈퍼 회복!\n회복량 : + 20\nHP : {self.hp}")       
            time.sleep(0.5)
            return self.hp
        else: 
            heal_amount = sum(dice_result)
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            print(f"회복!\n회복량 : {heal_amount}\nHP : {self.hp}")       
            time.sleep(0.5)
            return self.hp


class Warrior(Character):
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
        if dice1 == dice2:
            damage = dice1 * 4
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
        #주사위 판정후 힐 결정
        if dice1 == dice2:
            heal += 50
        else:
            heal = heal + dice1 + dice2
        # 힐 적용
        if self.hp + heal > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal
