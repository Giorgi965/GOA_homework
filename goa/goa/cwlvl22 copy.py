#1) 
num1=print(input("enter any number"))
for num1 in range(1,num1):
    print(num1)

#2)
n = int(input("შეიყვანეთ რიცხვი: "))
total = 0
for i in range(n + 1):
    print(n+total)
    total += i

#3)
number = int(input("შეიყვანე რიცხვი: "))
for i in range(1,number,3):
    print(number)

#4)
number = int(input("შეიყვანე რიცხვი: "))
product = 1
for i in range(1, number):
    product *= i
    print(number)

#5)
start = int(input("შეიყვანე პირველი რიცხვი: "))
end = int(input("შეიყვანე მეორე რიცხვი: "))
for i in range(start, end + 1):
    sum_even += i
print(i+sum_even)




