import random

# 클래스를 정의한다.
class Superhero():
 
    # 객체가 만들어질 때 속성을 초기화한다.
    def __init__(self):
        self.superName = superName
        self.power = power
        self.braun = braun
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

# 변수에  1부터 20사이의 값을 무작위로 선택한다.
braun = random.randint(1,20)
brains = random.randint(1,20)
stamina = random.randint(1,20)
wisdom = random.randint(1,20)
constitution = random.randint(1,20)
dexterity = random.randint(1,20)
speed = random.randint(1,20)

#  슈퍼 파워를 리스트로 만들어서 변수에 할당한다. 
superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 
               'Can Eat a Lot of Hot Dogs', 'Good At Skipping Rope']
# 임의로 하나의 슈퍼 파워를 리스트에서 선택한다.
power = random.choice(superPowers)

# 슈퍼 영웅의 이름과 성을 리스트로 만든다. 
superFirstName = ['Wonder','Whatta','Rabid','Incredible', 'Astonishing', 
                   'Decent', 'Stupendous', 'Above-average', 'That Guy', 'Improbably']
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy', 
                'Hero', 'Max', 'Dream', 'Macho Man','Stallion']
# 슈퍼 영우의 이름과 성을 임의적으로 선택해서 하나를 만든다.
superName = random.choice(superFirstName)+ " " +random.choice(superLastName)

# 슈퍼영웅 클래스를 상속하는 돌연변이 클래스를 하나 만든다.
class Mutate(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a Mutate!")
        self.speed = self.speed + 10
        
# 슈퍼영웅 클래스를 상속하는 로봇 클래스를 만든다. 
class Robot(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a robot!")
        self.braun = self.braun + 10
        


# 객체를 하나 만든다
hero = Superhero()

print(" 슈퍼 영웅의 이름은  %s." % (hero.superName))
print(" 슈퍼 파워는 : ", hero.power)
print(" 슈퍼 영웅의 상태 :")
print("")
print(" 지능 : ",hero. brains)
print(" 용맹함 : ", hero.braun)
print(" 체력: ", hero.stamina)
print(" 지혜 : ", hero.wisdom)
print(" 체질 : ", hero.constitution)
print(" 재치 : ", hero.dexterity)
print(" 속도 : ", hero.speed)
print("")

# Creating a Mutate object
hero2 = Mutate()
print(" 슈퍼 영웅의 이름은  %s." % (hero2.superName))
print(" 슈퍼 파워는 : ", hero2.power)
print(" 슈퍼 영웅의 상태 :")
print("")
print(" 지능 : ", hero2.brains)
print(" 용맹함 : ", hero2.braun)
print(" 체력: ", hero2.stamina)
print(" 지혜 : ", hero2.wisdom)
print(" 체질 : ", hero2.constitution)
print(" 재치 : ", hero2.dexterity)
print(" 속도 : ", hero2.speed)
print("")

# Create a Robot character
hero3 = Robot()
print(" 슈퍼 영웅의 이름은  %s." % (hero3.superName))
print(" 슈퍼 파워는 : ", hero3.power)
print(" 슈퍼 영웅의 상태 :")
print("")
print(" 지능 : ", hero3.brains)
print(" 용맹함: ", hero3.braun)
print(" 체력 : ", hero3.stamina)
print(" 지혜 : ", hero3.wisdom)
print(" 체질 : ", hero3.constitution)
print(" 재치 : ", hero3.dexterity)
print(" 속도 : ", hero3.speed)
print("")
