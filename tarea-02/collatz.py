print("input a number: ")
number = input()
number = int(number)

hs = open("attemps.txt","a")
hs.write(str(number) + '\n')
hs.close() 

def collatz(number):
    if number %2 == 0:
        return number//2
    else:
        return (3*number+1)//2

while number != 1:
    number = collatz(number)
    print(number)