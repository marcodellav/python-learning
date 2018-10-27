# for loops

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    if num == 3:
        print('Found!')
        break               # the break statement breaks out of the loop when the condition evaluates to True
    print(num)


for num in nums:
    if num == 3:
        print('Found!')
        continue               # the continue statement skips the value when the condition evaluates to True
    print(num)

for num in nums:
    for letter in 'ABCDEF':           # loop within a loop
        print(num, letter)

for i in range(1, 11):               # range can
    print(i)

# while loops

print('__')

x = 0

while x < 10:
    print(x ** 2)
    x += 1

print('__')

x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1
