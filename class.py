#+вероятность рождения мальчика 0.55, девочки 0.45
#+рожать могут только девочки
#+вероятность смерти мальчика до 20 лет 0.02 в год
#+вероятность смерти девочки до 20 лет 0.01 в год
#+малчик может стать отцом с 18 лет, оплодотворять до 40
#+девочка может стать матерью с 18 лет
#девочка выбирает равновероятно любого мальчика для оплодотворения, но не полнокровного брата
#+беременность длится один год в этот год и в следующий женщина не может снова забеременеть
#+женщина может родить с 18 до 35
#+вероятность смерти мальчика после 45 лет повышается до 0.05
#+вероятность смерти девочки после 45 повышается до 0.02
import random
class Human:
    birthdate = 0
    dad = 0
    mom = 0
    gender = 0
    pregnant = False
    alive = True
    def __init__(self, currentdate, refdad, refmom):
        self.birthdate = currentdate
        self.dad = refdad
        self.mom = refmom
        alive = True
        if 0 <= random.randint (0, 99) <=44 :
            self.gender = "f"
        else:
            self.gender = "m"
    def kill (self):
        self.alive = False
    def age (self, currentdate):
        return currentdate - self.birthdate
    def nextYear (self, currentdate, hum):
        if not self.alive: return
        if self.pregnant:
            hum.append (self.pregnant)
            self.pregnant = False
            return
        
        if self.gender == "f" and 18 <= self.age(currentdate) <= 35:
            no = 0
            for x in hum:
                if x.alive and x.gender == "m" and 18 <= x.age(currentdate) <= 40 and not (self.dad is x.dad and self.mom is x.mom):
                    no = x
                    break
            if no and not random.randint (0, 6):
                 self.pregnant = Human(currentdate + 1, no, self)
        if 0 <= self.age(currentdate) < 20:
            if "f" == self.gender:
                if not random.randint (0, 99): self.kill()
            else: 
                if not random.randint (0, 49): self.kill()
        elif 20 <= self.age(currentdate) <= 45:
            #?вопрос к аналитику
            pass
        else:
            if "f" == self.gender:
                if not random.randint (0, 49): self.kill()
            else:
                if not random.randint (0, 19): self.kill()
    def __str__ (self):
        return ("%s, birth=%d, alive=%d, preg=%d" % (self.gender, self.birthdate, self.alive, self.pregnant))

        

humans = []
for i in range (100):
    h = Human(0, i, -i)
    humans.append (h)
curdate = 0
while True:
    print ("=========год №", curdate)
    AliveCount = 0
    FemCount = 0
    Average = 0
    for x in humans:
        x.nextYear(curdate, humans)
        if x.alive:
            AliveCount += 1
            #print (x)
            if x.gender == "f":
                FemCount += 1
            Average += x.age(curdate)
    print ("Alive=%d, Fem=%d, Male=%d, Age=%d" % (AliveCount, FemCount, AliveCount - FemCount, Average / AliveCount if AliveCount else 0))
    curdate += 1
    if AliveCount == 0: break