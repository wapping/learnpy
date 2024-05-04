"""
定义了一个装饰器 log_decorator，用于在函数调用前后打印函数名以及函数返回值。

示例中的accumulate函数@log_decorator装饰器。

在主程序中，调用 accumulate 函数，将会打印以下内容
    accumulate was called
    accumulate returned: 5050
"""
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
