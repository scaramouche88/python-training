# generates Fibonacci's sequences with a specific lenght

def fibonacci(fib):
 fib.append(fib[-1]+fib[-2])
 return fib

a=int(input("How long do you want the Fibonacci\'s sequence: "))

fib=[0,1]

while len(fib) < a:
 fib=fibonacci(fib)

print(fib)

