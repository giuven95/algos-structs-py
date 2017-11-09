'''
for all numbers from 1 to 100,
    print Fizz if they are divisible by 3,
    else print Buzz if they are divisible by 5,
    else print both if both conditions apply,
    else print the number itself
'''


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(100)
    # it's as simple as that, ladies and gentlemen
    # it's as simple as that
