def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number:')

try:
    number = int(input())
except ValueError:
    print('Must enter a integer')
    number = int(input())

while number != 1:
    print(number * '|')
    number = collatz(number)
