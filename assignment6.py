# 1
def max_number(a, b):
    return a if a > b else b

# 2
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# 3
def check_speed(speed):
    if speed < 70:
        print("Ok")
    else:
        points = (speed - 70) // 5
        if points > 12:
            print("License suspended")
        else:
            print(f"Points: {points}")

# 4
def show_numbers(limit):
    for num in range(limit + 1):
        label = "EVEN" if num % 2 == 0 else "ODD"
        print(num, label)

# 5
def sum_of_multiples(limit):
    return sum(num for num in range(limit + 1) if num % 3 == 0 or num % 5 == 0)

# 6
def show_stars(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# 7
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def show_primes(limit):
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    print(", ".join(map(str, primes)))

# Example usage:
# print(max_number(10, 20))
# print(fizz_buzz(15))
# check_speed(85)
# show_numbers(3)
# print(sum_of_multiples(20))
# show_stars(5)
# show_primes(20)