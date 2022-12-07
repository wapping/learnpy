

def show_dict():
    """显示dict"""

    d = {
        "a": 0,
        "b": 1
    }

    print(d)


def dict_add():
    d = dict()
    d["a"] = 0
    print(d)


def dict_delete():
    d = {
        "a": 0,
        "b": 1
    }
    d.pop("a")
    print(d)

    d.clear()
    print(d)


def dict_search():
    d = {
        "a": 0,
        "b": 1
    }

    val = d["a"]
    print(val)

    val = d.get("c")
    print(val)

    val = d["c"]


if __name__ == '__main__':
    ...
    # dict_add()
    # dict_delete()
    dict_search()
