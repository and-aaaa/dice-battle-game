import random
import time

from character import Character

class Rogue (Character):
    def __init__(self, name):
        self.hp = 75
        self.max_hp = 75
        self.name = name
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
