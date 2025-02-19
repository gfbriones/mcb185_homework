# 24savingthrows.py by Gennie Fae Briones
# 
import random

trials = 100000
dc = 5
sides = 20

for dc in range(5, 16, 5):
    nor = 0
    adv = 0
    dis = 0
    for i in range(trials):
        roll1 = random.randint(1,sides)
        roll2 = random.randint(1,sides)
        if roll1 >= dc: nor += 1
        if roll1 >= dc and roll2 >= dc: dis += 1
        if roll1 >= dc or roll2 >= dc: adv += 1
    print(dc, 'normal:', nor/trials, 'disadvantage:',dis/trials, 'advantage:', adv/trials)