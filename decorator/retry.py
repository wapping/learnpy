import random


def retry(times=3):
    """
    重试装饰器，如果函数执行结果为None，则自动重试指定次数。

    Args:
        times (int, optional): 重试次数，默认为3。

    Returns:
        function: 返回被装饰的函数。

    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                res = func(*args, **kwargs)
                if res is None:
                    print('retry', i + 1, 'times')
                    continue
                else:
                    return res
        return wrapper
    return decorator

@retry(1)
def random_even(min, max):
    """
    生成指定范围内的随机偶数

    Args:
        min (int): 生成随机数的最小值（包含）
        max (int): 生成随机数的最大值（包含）

    Returns:
        int: 生成的随机偶数，若指定范围内不存在偶数则返回None

    """
    num = random.randint(min, max)
    if num % 2 == 0:
        return num
    else:
        return None


if __name__ == '__main__':
    print(random_even(0, 10))
