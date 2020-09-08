from random import randint

print("开始游戏，你只有三次机会。。。")
i = 0
num = randint(1, 10)
while i < 3:
    input_num = input("随机输入一个数字：")
    guess = int(input_num)
    if guess == num:
        print("恭喜你猜对了！")
        break
    else:
        if guess > num:
            print("大了。。。")
            i += 1
        if guess < num:
            print("小了。。。")
            i += 1
print("不玩了。。。")
