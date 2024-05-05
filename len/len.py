
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

