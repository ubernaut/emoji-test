import random
import time

def Fibonacci(n):
    if n<0:
        print("sub zero input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

non_emoji_times=[]

def race_fib():
    start = time.time()
    fib = Fibonacci(35)
    end = time.time()
    this_run=end-start
    non_emoji_times.append(this_run)

def run_all(times=100):
    print("")
    print("NEW RUN")
    for i in range(0,times):
        race_fib()
    print("########################")
    print("RESULTS")
    print("########################")
    print("non io: ")
    print(sum(non_emoji_times))
    print("########################")

run_all()
