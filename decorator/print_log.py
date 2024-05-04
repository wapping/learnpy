
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_decorator
def accumulate(n):
    """
    计算从0到n的所有整数的累加和。通过@log_decorator装饰器，打印函数调用过程和结果
    """
    res = 0
    for i in range(n + 1):
        res += i
    return res


if __name__ == "__main__":
    accumulate(100)
