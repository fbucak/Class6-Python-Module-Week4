import random
import array as arr


dice=arr.array("i",[0,0,0,0,0,0])
for _ in range(5000):
    value=random.randint(1,6)
    dice[value-1]=dice[value-1]+1

for i in range(len(dice)):
    print("Percentage of throws of value {}= {}%".format(i+1,(dice[i]*100)/5000))