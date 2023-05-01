from Unit import Unit, TankerUnit, ADUnit
    
# 메모리에 구현 : 틀(설계도)에 맞춰서 유닛(인스턴스 변수)을 찍어낸다.
print("========= 생성! =========")
worrior1 = Unit("전사1", 40, 5)
worrior2 = Unit("전사2", 40, 5)
archer1  = Unit("궁수1", 25, 10)

# 공격 메서드
print("========= 공격! =========")
worrior1.attack(worrior2)
print()
archer1.attack(worrior1)
print()

for _ in range(5):
    archer1.attack(worrior1)
    print()

print()
# ======== Unit 클래스의 속성과 기능을 물려받아 전직한 TankerUnit ======== #
tanker1 = TankerUnit("탱커", 80, 7)
print(tanker1) # 왜 __str__을 재정의 하지 않아도 잘 동작할까요?

tanker1.attack(archer1) # attack 기능 그대로 사용
print()
archer1.attack(tanker1)


print()
# ======== Unit 클래스의 속성과 기능을 물려받아 전직한 ADUnit ======== #
ad_unit1 = ADUnit("원딜", 200, 100)

ad_unit1.attack(archer1)
print()
# ad_unit1.skill(tanker1)
print()

# ======== 직렬화 ======== #
import json

j = json.dumps(ad_unit1)
print(j)