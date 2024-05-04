import time

# 定义一个装饰器函数，用于缓存函数的结果
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            # 如果结果未缓存，则计算结果并存储到缓存中
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# 使用装饰器来修饰需要缓存结果的函数
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print("第一次调用 fibonacci 函数时会计算结果，并将结果缓存")
    start_time = time.time()
    fibonacci(100)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"{elapsed_time:.4f} ms.")

    print("后续再次调用相同的 fibonacci 函数时，直接返回缓存的结果")
    start_time = time.time()
    fibonacci(100)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"{elapsed_time:.4f} ms.")
