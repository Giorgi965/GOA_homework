#1)
while True:
    word = input("შეიყვანეთ სიტყვა: ")
    if word == "Guram":
        break

#2)
while True:
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number < 0:
        break





#3)
while True:
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number == 5:
        print("Guram teacher")
        break


#boss level
attempts = 0
while True:
    pin = input("შეიყვანეთ პინკოდი: ")
    attempts += 1
    if pin == "9877":
        print("attemps * 2 =", attempts * 2)
        break


