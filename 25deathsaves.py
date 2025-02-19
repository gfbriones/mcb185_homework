# 25deathsaves.py by Gennie Fae Briones
#
#
import random

trial = 10000

die = 0
stable = 0
revive = 0 

# 1 = 2 fail
# 2 - 9 = 1 fail 


for i in range(trial):
    fail = 0
    succ = 0
    print('trial', i)
    for i in range(trial):
        roll = random.randint(1, 20)
        if roll == 1: fail += 2
        elif roll <= 9: fail += 1
        elif roll <= 19: succ += 1
        else: 
            revive += 1
            break
        if succ == 3:
            stable += 1
            break
        if fail >= 3:
            die += 1
            break
        print(roll)

print ('Probability of one dies:', (die/trial))
print('Probabilty of one stablizes:', stable/trial)
print('Probaility of one revives:', revive/trial)