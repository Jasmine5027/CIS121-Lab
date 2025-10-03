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