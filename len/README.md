我们知道python中`len()`可以获取对象的长度，类似其它一些语言中的`obj.size()`。

可是为什么`len()`不是`obj.len()`呢？`len()`不是对象的函数，是怎么知道对象的长度的？

事实上，python并不知道对象的长度，当你执行 `len(obj)` 时，Python 会调用对象的 `__len__()` 方法。所以，只要对象有`__len__()`方法，执行`len(obj)`就能返回结果，至于是不是对象的长度，就得看`__len__()`是怎么定义的了。

下面有两个类，一个有`__len__()`方法，而另一个没有。有`__len__()`方法的对象可以被`len()`，而试图`len()`一个没有`__len__()`方法的对象就会报错。

```
# 有__len__方法的类
class ExampleWithLen:
    def __init__(self, len):
        self.len = len

    def __len__(self):
        return self.len


# 没有__len__方法的类
class ExampleWoLen:
    def __init__(self, len):
        self.len = len


if __name__ == '__main__':
    example1 = ExampleWithLen(10)
    example2 = ExampleWoLen(10)
    print(len(example1))    # 打印example1的长度
    print(len(example2))    # 报错
```

程序输出结果如下

```
10
Traceback (most recent call last):
  File "len/len.py", line 20, in <module>
    print(len(example2))
TypeError: object of type 'ExampleWoLen' has no len()
```
