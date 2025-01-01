def print_result(func):

    def printer(*args, **kwargs):
        func_res = func(*args, **kwargs)
        print(func.__name__)
        if type(func_res) is dict:
            for key, value in func_res.items():
                print(f"{key} = {value}")
        else:
            if type(func_res) is list:
                for item in func_res:
                    print(item)
            else:
                print(func_res)
        return func_res

    return printer


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return "iu5"


@print_result
def test_3():
    return {"a": 1, "b": 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == "__main__":
    print("!!!!!!!!")
    test_1()
    test_2()
    test_3()
    test_4()
