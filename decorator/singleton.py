"""
用 Python 装饰器实现单例模式。在单例模式中，一个类只允许创建一个实例。
代码中的 singleton 装饰器实现了这个功能。当类被 @singleton 装饰时，创建类的实例时将会通过装饰器中的逻辑进行处理，确保只创建一个实例，并在后续请求中返回相同的实例。
在示例代码中，ExampleClass 是一个使用了单例模式的类，它只允许创建一个实例。
在主程序中，示范了如何使用 ExampleClass 创建实例，并打印它们的 id 和 name 属性。由于单例模式的限制，无论创建多少次实例，它们的 id 都会相同，说明它们是同一个实例。
"""

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
