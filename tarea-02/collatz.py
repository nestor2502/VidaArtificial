print("input a number: ")
number = input()
number = int(number)

def collatz(number):
    if number %2 == 0:
        return number//2
    else:
        return (3*number+1)//2

while number != 1:
    number = collatz(number)
    print(number)