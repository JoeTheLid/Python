import random

#gender
randgend = (random.randint(1,2))
if randgend == 1:
    gender = 'Male'
else: 
    gender = 'Female'

#age
randage = (random.randint(1,3))
if randage == 1:
    age = 'Young'
elif randage == 2:
    age = 'Middle Aged'
else:
    age = 'Old'

#Nationality
randnationality = (random.randint(1,10))
if randnationality < 6:
    nationality = 'Local'
elif randnationality < 10:
    nationality = 'Foreign neighbour'
else: 
    nationality = 'From distant lands'

#features
randfeature = (random.randint(1,10))
featureslist ={1: 'Unremarkable',
2: 'Attractive',
3: 'Stoop backed',
4: 'Noticeable limp',
5: 'Freckles',
6: 'Extremely tanned',
7: 'Strong accent',
8: 'Broken nose',
9: 'Wild hair',
10:'Untrustworthy smile'}

#attitude
randattitude = (random.randint(1,10))
attitudelist = {
1: 'Friendly (Seeking stories)',
2: 'Indifferent (Busy)',
3: 'Hostile (Bad attitude)',
4: 'Friendly (Seeking companionship)',
5: 'Hostile (Looking for a fight)',
6: 'Indifferent (Selling something)',
7: 'Friendly\Hostile (Mistakes you for an old acquaintance)',
8: 'Indifferent (Bored)',
9: 'Friendly (Needs help with something minor)',
10: 'Hostile (Prejudiced against someone)'
}


print(gender)
print(age) 
print (nationality)
print(featureslist[randfeature])
print(attitudelist[randattitude])