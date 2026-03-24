def fizz_buzz(n):
    # Using 1 as the starting point,
    for i in range(1, n + 1): 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Calling the function here
fizz_buzz(50)