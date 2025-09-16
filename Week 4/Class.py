#loops
'''
num = 1
while num <= 10:
    print(num)
    num += 1
'''

#even number
'''
num = 1
while num <= 10:
    if num %2 == 0:
        print(num)
    num += 1
'''

#odd number from 5 to user give:
'''
max_num = int(input('Enter a number: '))
num = 5
while num <= max_num:
    if num %2 == 1:
        print(num)
    num += 1
'''
    
#(continue) even number not%3=0
'''
num = 0
while num < 50:
    if num % 2 == 0:
        if num % 3 == 0:
            num += 1 #prevent an infinite loop
            continue
        else:
            print(num)
    num += 1
'''


#stop when input is q
'''
total = 0

while True:
    user = input("Enter a number or type q to end: ")
    
    if user != 'q':      
        total += int(user)
    else:                
        break

print("Total =", total)
'''