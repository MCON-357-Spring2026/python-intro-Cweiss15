"""
TODO:
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table of 5

"""
for i in range(1,11):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

sum = 0
for i in range(1,101):
    sum += i
print("sum:", sum)

for i in range(1, 11):
    print("5 *", i, "=", 5 * i)
