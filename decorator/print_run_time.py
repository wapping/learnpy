import time

def print_run_time(func):
    """
    计算并打印函数运行时间
    """
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"函数{func.__name__} 耗时 {elapsed_time:.4f} 毫秒.")
    return wrapper

def print_run_time_v2(func):
    """
    计算并打印函数运行时间。支持func存在返回值
    """
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"函数{func.__name__} 耗时 {elapsed_time:.4f} 毫秒.")
        return res
    return wrapper

def print_run_time_v3(func):
    """
    计算并打印函数运行时间。支持func存在返回值。支持func传参
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"函数{func.__name__} 耗时 {elapsed_time:.4f} 毫秒.")
        return res
    return wrapper


def accumulate():
    """
    计算0到n的累加和，并输出所花费的时间（单位为毫秒）。
    """
    start_time = time.time()
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
    print(f"函数{accumulate.__name__} 耗时 {elapsed_time:.4f} 毫秒.")

@print_run_time
def accumulate_v2():
    """
    计算从0到n的所有整数的累加和。通过@print_run_time装饰器打印程序运行时间。
    """
    n = 100
    res = 0
    for i in range(n + 1):
        res += i

@print_run_time_v2
def accumulate_v3():
    """
    计算从0到n的所有整数的累加和。通过@print_run_time_v2装饰器打印程序运行时间。返回计算结果。
    """
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
    return res

@print_run_time_v3
def accumulate_v4(n):
    """
    计算从0到n的所有整数的累加和。通过@print_run_time_v3装饰器打印程序运行时间。返回计算结果。n由参数指定
    """
    res = 0
    for i in range(n + 1):
        res += i
    return res

if __name__ == '__main__':
    # accumulate()
    accumulate_v2()
    # print(f"累加结果={accumulate_v3()}")
    # print(f"累加结果={accumulate_v4(100)}")

