#1
'''
def pyramid_volume (b,h):
  return round(((b**2)*h)/3 , 2)    #round(expression, 2) -> Round to two decimal places

print(pyramid_volume(1,2))
'''




#2
'''
import math
def cone_volume(r,h):
  return round((math.pi)*(((r**2)*h)/3),2)

print(cone_volume(1,2))
'''




#3
'''
def total_score(two,three):
  return((two*2)+(three*3))
print(total_score(5,7))
'''




#4
'''
def total_score(ace,win):
  return((ace*2)+(win*1))
print(total_score(2,3))
'''




#5
'''
def leg_counter(chickens,cows,pigs):
  return((chickens*2)+(cows*4)+(pigs*4))
print(leg_counter(4,3,2))
'''




#6
'''
def battery_counter(dolls,cars,dogs):
  return((dolls*2)+(cars*4)+(dogs*6))
print(battery_counter(4,3,2))
'''




#15
'''
def count_duplicates (num_1,num_2,num_3):
  if num_1==num_2 or num_2==num_3 or num_1==num_3:
    count=2
  elif num_1==num2==num3:
    count=3
  else:
    count=0
  return count

num_1 = float(input('Enter your number: '))
num_2 = float(input('Enter your number: '))
num_3 = float(input('Enter your number: '))

result = count_duplicates (num_1,num_2,num_3)

if result == 0:
  print('Each number is unique.')
else:
  print(f'You entered the same number {result} times.')
'''