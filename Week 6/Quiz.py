#1
'''
def skip_letter(word):
  #data cleaning
  word = word.replace(' ','')   #string.replace('old', 'new') notice to use parentheses
  letter = []
  for x in word[::2]:   #[]
    letter.append(x)
  return letter

word = input('Enter word: ')
print(skip_letter(word))
'''




#2
'''
def skip_letter(word):
  letter = []
  for x in word[1::2]:
    letter.append(x)
  return letter

word = input('Enter word: ')
print(skip_letter(word))
'''




#3
'''
def output_even(smaller_num,larger_num):
  start = smaller_num + (smaller_num%2)   # guaranteed always even
  return list(range(start,larger_num+1,2))

smaller_num = int(input('Enter smaller number: '))
larger_num = int(input('Enter larger number: '))
print(output_even(smaller_num,larger_num))
'''




#4
'''
def output_odd(smaller_num,larger_num):
  start = smaller_num + (1 - smaller_num%2)   # guaranteed always odd
  return list(range(start,larger_num+1,2))

smaller_num = int(input('Enter smaller number: '))
larger_num = int(input('Enter larger number: '))
print(output_odd(smaller_num,larger_num))
'''




#5
'''
def hailstone_seq(number):
  result = [number]
  while number != 1:
    number = number/2 if number%2==0 else (3*number)+1
    result.append(number)
  return result

number = int(input('Enter number: '))
print(hailstone_seq(number))
'''





#7
'''
def ascending_ording(num_1,num_2,num_3):
  if num_3 > num_2:
    num_2,num_3 = num_3,num_2
  if num_3 > num_1:
    num_1,num_3 = num_3,num_1
  if num_2 > num_1:
    num_1,num_2 = num_2,num_1
  
  return [num_3,num_2,num_1]

num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))
num_3 = int(input('Enter number: '))

print(ascending_ording(num_1,num_2,num_3))
'''




#8
'''
def descending_ording(num_1,num_2,num_3):
  if num_3 > num_2:
    num_2,num_3 = num_3,num_2
  if num_3 > num_1:
    num_1,num_3 = num_3,num_1
  if num_2 > num_1:
    num_1,num_2 = num_2,num_1
  
  return [num_1,num_2,num_3]

num_1 = int(input('Enter number: '))
num_2 = int(input('Enter number: '))
num_3 = int(input('Enter number: '))

print(descending_ording(num_1,num_2,num_3))
'''




#9
'''
def count(cards):
  result = 0
  
  x = [2,3,4,5,6]
  z = [10,'j','q','k','a']

  for n in cards:
    if n in x:
      result += 1
    elif n in z:
      result -= 1
  return result

cards = ['a',5,5,2,6,2,3,8,9,7]
print(count(cards))
'''

#10
'''
def war_of_number(number):
  odd = 0
  even = 0
  for x in number:
    if x%2==1:
      odd += x
    else:
      even += x
  return 'odds' if odd > even else 'evens'

number=[2,8,7,5]
print(war_of_number(number))
'''




#13
def largest_even(number):
  largest = 0
  for x in number:
    if x % 2 == 0 and x > largest:
      largest = x
  return -1 if largest == '' else {largest}

number = [3,7,2,1,7,9,10,13]

print(largest_even(number))




#19
'''
def is_acronym(s,word):
  if len(s) != len(word):
    return False

  for i in range(0,len(s)):    # get the index max amount
    if s[i] != word[i][0]:
       #compare one by one
      return False  
  return True 
s = input('Enter the acronym: ')
word = ['apple','pear','cat']
print(is_acronym(s,word))
'''