# Count to 100
# Every number divisible by 3, say "Fizz"
# Every number divisible by 5, say "Buzz"
# Every number divisible by both 3 and 5, say "Fizz Buzz"

# modulo gives remainder
# print(10 % 3) # should give 1
# print(9 % 3) # should give 0

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)