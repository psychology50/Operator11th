class Unit:
    def __init__(self, name, hp, damage): # 유닛의 이름, 체력, 공격력
        self.name = name
        self.hp = hp
        self.damage = damage

        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"HP: {self.hp}, 공격력: {self.damage}")

    # 유닛의 공격 기능
    def attack(self, unit:object):
        print(f"{self.name}: {unit}을 공격합니다. [공격력: {self.damage}]")
        unit.__damaged(self.damage)
    
    # 유닛의 피해 기능
    def __damaged(self, damage): # 외부에서 접근할 수 없다.
        print(f"{self.name}: {damage}만큼의 데미지를 입었습니다.")
        self.hp -= damage # 해당 유닛의 체력 감소
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0: # 체력이 0 이하라면 die
            print(f"{self.name}: 적의 공격에 의해 사망하였습니다!")
            
    def __str__(self):
        return self.name + "[hp: " + str(self.hp) + ", damage: " + str(self.damage) + "]"
    

class TankerUnit(Unit): # Unit을 상속받는 SuperUnit
    def __init__(self, name, hp, damage, defense=20): # SuperUnit은 방어력이라는 속성이 추가됨 // 디폴트 매개변수로 defense 값을 따로 주지 않으면 기본 20이 저장됨
        super().__init__(name, hp, damage)
        self.defense = defense

    def __damaged(self, damaged): # SuperUnit은 데미지를 받아도 방어력만큼 피해가 감소한다. (오버라이딩 = '재정의')
        print(f"{self.name}: {damaged - self.defense}만큼의 데미지를 입었습니다.")
        self.hp = self.hp - damaged + self.defense # 해당 유닛의 체력 감소
        print(f"{self.name}: 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0: # 체력이 0 이하라면 die
            print(f"{self.name}: 적의 공격에 의해 사망하였습니다!")

class ADUnit(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

    def skill(self, unit:TankerUnit): # 다른 것은 다 같지만 ADUnit은 스킬을 쓸 수 있게 되었다.
        if not isinstance(unit, TankerUnit):
            print("스킬을 사용할 수 없는 유닛입니다.")
            return
        
        print(f"{self.name}: 스킬을 사용하였습니다.")
        print(f"{unit}에게 {self.damage * 5}만큼의 피해를 입혔습니다.")
        unit.__damaged(self.damage * 5) # 이렇게 하면 안됩니다. 왜일까요?

        






ad_unit1 = ADUnit("원딜", 200, 100)

ad_unit1.attack(archer1)
print()
ad_unit1.skill(tanker1)
print()





    
# 메모리에 구현 : 틀(설계도)에 맞춰서 유닛(인스턴스 변수)을 찍어낸다.
print("========= 생성! =========")
worrior1 = Unit("전사1", 40, 5)
worrior2 = Unit("전사2", 40, 5)
archer1  = Unit("궁수1", 25, 10)

# 공격 메서드
print("========= 공격! =========")
worrior1.attack(worrior2)
print("")
archer1.attack(worrior1)
print("")

for _ in range(5):
    archer1.attack(worrior1)
    print("")