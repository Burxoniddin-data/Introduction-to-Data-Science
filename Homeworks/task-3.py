import time
import random

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")

    return wrapper

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [i**2 for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()
