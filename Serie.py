sum = 0
num1 = 0
num2 = 1

while num2 < 400000:
    temp = num1
    num1 = num2
    num2 = temp
    sum+= num1
    print(num1)
     
