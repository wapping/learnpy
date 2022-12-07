

def show_list():
    """显示list的各种形式"""

    ls = [1, 2, 3]
    print(ls)

    ls = ["one", "two", "three"]
    print(ls)

    ls = [1, 2, 3, "one", "two", "three"]
    print(ls)

    ls = [[1, 2, 3], ["one", "two", "three"]]
    print(ls)

    ls = []
    print(ls)


def list_add():
    """往list添加数据"""
    ls = [1, 2, 3]
    print(ls)

    ls = []
    for i in range(1, 4):
        ls.append(i)
    print(ls)

    ls.insert(0, 0)
    print(ls)

    ls1 = [1, 2]
    ls2 = [3, 4]
    ls = ls1 + ls2
    print(ls)


def list_delete():
    """从list删除数据"""
    ls = [1, 2, 3]
    ls.clear()
    print(ls)

    ls = [1, 2, 3]
    ls.remove(3)
    print(ls)
    ls = [1, 2, 3, 3]
    ls.remove(3)
    print(ls)

    ls = [1, 2, 3, 3]
    ls.pop(0)
    print(ls)


def list_search():
    """在list中查找"""
    ls = [1, 2, 3]
    for i in ls:
        print(i, end='\t')

    ls = [1, 2, 3, 3]
    print(ls.index(3))
    print(ls.index(4))

    if 4 in ls:
        print(True)
    else:
        print(False)

    print("Count 3 =", ls.count(3))
    print("Count 4 =", ls.count(4))

    print(ls[0])

    print(ls[0: 3])


def list_sort():
    """对list排序"""
    ls = [2, 3, 1]
    ls.sort()
    print(ls)
    ls.sort(reverse=True)
    print(ls)
    

if __name__ == '__main__':
    ...
