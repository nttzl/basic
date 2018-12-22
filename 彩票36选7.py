import random,time

#号码池
pool = []           
pool.extend([i for i in range(1,37)])
#选择的号码
code = []
#结果的号码
result = []

#在号码池里随机选7个不重复的号码，放入result里
#同时让玩家选择自己的号码，放入code里
for i in range(1,8):
    x = random.choice(pool)
    pool.remove(x)
    result.append(x)
    num = int(input("please enter your number {}:".format(i)))
    code.append(num)
print("-"*50)
print("your codes are:{}".format(code))
for i in range(5):
    time.sleep(1)
    print(5-i)

print("the resules are:{}".format(result))
print("-"*50)

count = 0
for i in range(7):
    if code[i] in result:
        count += 1
print("you have {} right numbers".format(count))
