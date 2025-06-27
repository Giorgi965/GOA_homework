#1)შექმენით ფუნქცია რომელიც იღებს 2 არგუმენტს. ინტეჯერს და ერთ სტრინგს, შემდეგ ეს სტრინგი დაპრინტეთ იმდენჯერ რა ინტეჯერიც გადმოგეცათ(მითითება:სტრინგი შეგიძლიათ გაამრავლოს სტრინგზე)
#მაგ:
#my_func("hello", 5)
#output:"hellohellohellohellohello"

#2)შექმენით ფუნქცია რომელიც იღებს ერთ ბულეანს და ერთ სტრინგს, შემდეგ თუ ეს ბულეანი არის True დაპრინტეთ ეს სტრინგი, თუ იქნება False არ დაპრინტოთ
#მაგ:
#my_func(True, "GOA")
#output:"GOA"
#ან
#my_func(False, "GOA")
#output:

#3)შექმენით ფუნქცია რომელიც იღებს 2 არგუმენტს, სიას და ინტეჯერს, შემდეგ ამ სიაში 0 ინდექსიდან ამ ინტეჯერ ინდექსამდე დაპრინტოს ელემენტები
#მაგ:
#my_func([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
#output:[1, 2, 3, 4, 5])

#4)შექმენით ფუნქცია რომელიც იღებს ინტეჯერსს არგუმენტად და შემდეგ დაპრინტეთ ამ ინტეჯერის კუბი(რიცხვის კუბი არის ეს რიცხვი გამრავლებული თავის თავზე სამჯერ)
#მაგ:
#my_func(5)
#output:125

# Boss level
#5)შექმენით ფუნქცოა. რომელიც ამოწმებს არის თუ არა რიცხვი მარტივი(მარტივი რიცხვი არის ისეთი რიცხვი რომელიც იყოფა მარტო 1 ზე და თავის თავზე, მეტზე არაფერზე) თუ მარტივია დაპრინტეთ True თუარა დაპრინტეთ False
#მაგ:
#my_func(7)
#output:True(7 მარტივია)


#ან
#my_func(8)
#output:False(8 არ არის მარტივი)





def goa(n, text):
    print(text * n)
goa(3, "გამარჯობა ")



bool=input(bool("enter True or False"))
str=input(str("enter any string"))
def my_function(boolean,str):
    if boolean:
        print(str)



#3)


my_list = [10, 20, 30, 40, 50]
def print(my_list, index):
    print(my_list[0:index])

#4)
def print_cube(n):
    print(n ** 3)


#boss level

def is_prime(n):
    if n < 2:
        print(False)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(False)
    print(True)