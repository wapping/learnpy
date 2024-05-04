# 1 简介

这里介绍python的装饰器（decorator）。

个人理解，装饰器就是给一个函数套一个壳，在执行函数前或者执行函数后做点其它的操作，比如记录函数运算时间。

下面会介绍几个用了装饰器的例子，通过这些弄明白例子，对装饰器的用法会有更广的认识，而不只是用来计时。

# 2 使用场景

## 2.1 记录程序运行时间

还是从简单的计时开始介绍。

假设有以下函数，计算0到n的累加和

```
def accumulate():
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
```

如果要记录程序运行时间并且打印，可以把函数改成这样

```
def accumulate():
    start_time = time.time()
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
    print(f"函数{accumulate.__name__} 耗时 {elapsed_time:.4f} 毫秒.")
```

这样做有几点不足：

- 计时的代码和原来的代码交叉在一起了，代码变复杂了。
- 另外，如果哪天不需要计时了，还得删掉前后的代码。
- 如果有另外一个函数也要计时，这段计时的代码还得写一次。

考虑到这些，装饰器就体现它的优势了。

用了装饰器，以上的代码可以修改成这样

```
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
    
@print_run_time
def accumulate_v2():
    """
    计算从0到n的所有整数的累加和。通过@print_run_time装饰器打印程序运行时间。
    """
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
```

执行`accumulate_v2()`就可以计算累计并且打印时间，结果如下

```
函数accumulate_v2 耗时 0.0038 毫秒.
```

这样`accumulate_v2()`函数就不会被计时的代码污染，并且如果其它函数也要计时，@print_run_time就可以了。

在accumulate_v2()函数前@print_run_time就相当于把这个函数作为参数传递给print_run_time函数，print_run_time函数的入参func就是一个函数，print_run_time函数给func套壳，wrapper就是套壳后的函数，在func前后各加入点操作，print_run_time最后return wrapper，这就是装饰后的func。这里转进去的func是accumulate_v2，如果传其它函数，那么就会对其它函数也做相同的装饰。

以上的print_run_time还不够完善，它只能修饰无参数、无返回值的函数，比如accumulate_v2。

假设要对accumulate_v2进行修改，改成了这样，其实也就增加了return那行

```
def accumulate_v3():
    """
    计算从0到n的所有整数的累加和。通过装饰器打印程序运行时间。返回计算结果。
    """
    n = 100
    res = 0
    for i in range(n + 1):
        res += i
    return res
```

那么@print_run_time就不太适用了，因为wrapper没有return，为了让wrapper也return，就修改成下面这样就行了

```
def print_run_time_v2(func):
    """
    计算并打印函数运行时间。支持func存在返回值
    """
    def wrapper():
        start_time = time.time()
        res = func()	# 接收func()的结果
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000  # 转换为毫秒
        print(f"函数{func.__name__} 耗时 {elapsed_time:.4f} 毫秒.")
        return res		# 返回func()的结果
    return wrapper
```

但如果accumulate_v3不仅要返回结果，还要入参，比如像这样

```
def accumulate_v4(n):
    """
    计算从0到n的所有整数的累加和。通过装饰器打印程序运行时间。返回计算结果。n由参数指定
    """
    res = 0
    for i in range(n + 1):
        res += i
    return res
```

类似的，还是修改wrapper，给它也传参就行，比如这样

```
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
```

为了使得它的通用性更强，用`*args, **kwargs`这种比较抽象的形式表示入参，而不是具体的参数名n，这样其它各式各样的函数都可以通过@print_run_time_v3实现计时。

## 2.2 打印日志

有时候调试程序需要查看函数的返回结果，有时候也想知道程序执行到哪个函数了。

```

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
```

以上示例定义了一个装饰器 log_decorator，用于在函数调用前后打印函数名以及函数返回值。

accumulate函数@log_decorator装饰器。

在主程序中，调用 accumulate 函数，运行程序将会打印以下内容

```
accumulate was called
accumulate returned: 5050
```

如果以后要跟踪哪个函数是否被执行了，@一下log_decorator就可以了。

## 2.3 反复尝试执行

有时候执行函数一次得不到想要结果，可能需要反复执行，比如网络请求。不过这里不写这么复杂的例子，就用个简单点的。

代码如下，random_even函数要在min和max之间随机选一个偶数，而函数中的random.randint可能会选到基数，那是不符合需要的，就要重复再选，直到选中偶数为止，但是也有可能一直都选中基数，虽然概率很小。选不到偶数，程序还要前进，不能一直等，所以限定重复的次数。retry函数就实现了这样的功能。

```
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
```

这个retry跟前面的装饰器不太一样，它自己也有参数，可以设置最多重复尝试func多少次。retry的入参不是func，它里面的decorator的入参才是func，所以decorator才是真正装饰random_even的装饰器，retry只是生成这样的装饰器。retry函数return decorator，decorator函数return wrapper。

## 2.3 缓存计算结果

不知道有什么常见的场景，就拿斐波那契数举例把，函数`fibonacci(n)`就是返回斐波那契数列中的第n个数。

从fibonacci函数的递归代码中可以想到，有很多重复的计算。memoize装饰就起到了缓存的作用，计算结果会存到cache中，如果下次遇到同样的计算，就从cache中读取，而不需要重复计算。

```
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

```

以上代码的执行结果如下，第二次调fibonacci函数的耗时比第一次少了很多很多，因为第二次压根没计算，直接在缓存取结果

```
第一次调用 fibonacci 函数时会计算结果，并将结果缓存
0.0868 ms.
后续再次调用相同的 fibonacci 函数时，直接返回缓存的结果
0.0002 ms.
```

## 2.4 单例模式

由于某种原因，有时候一个类只允许创建一个实例，可能因为这个类的实例比较占内存。这就是单例模式（singleton）。以下代码中的 singleton 装饰器实现了这样的功能。

当类被 @singleton 装饰时，创建类的实例时将会通过装饰器中的逻辑进行处理，确保只创建一个实例，并在后续请求中返回相同的实例。
在示例代码中，ExampleClass 是一个使用了单例模式的类，它只允许创建一个实例。

在主程序中，示范了如何使用 ExampleClass 创建实例，并打印它们的 id 和 name 属性。

```
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class ExampleClass:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    instance1 = ExampleClass('A')
    print(id(instance1), instance1.name)
    instance2 = ExampleClass('B')
    print(id(instance2), instance2.name)
```

程序的运行结果如下，由于单例模式的限制，无论创建多少次实例，它们的 id 都会相同，说明它们是同一个实例。

```
140456725134976 A
140456725134976 A
```

