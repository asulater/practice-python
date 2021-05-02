import random
import os

def input_check(msg, casting=int):
    while True:
        try:
            user_input = int(input("숫자는 몇 일까요?"))
            return user_input
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system("cls")
print("1부터 99까지의 숫자를 10번 안에 맞춰 보자!")

while count < chance:
    count += 1
    user_input = input_check("몇 일까요?")
    
    if number == int(user_input):
        print("정답! {} 이 맞습니다. " .format(number))
        break
    elif int(user_input) < number:
        print("{} 보다 큰 숫자 입니다." .format(user_input))
    elif int(user_input) > number:
        print("{} 보다 작은 숫자 입니다." .format(user_input))
        
