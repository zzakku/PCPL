import json
import sys
from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1

path = "/home/gato/Документы/funcpy/data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(arg):
    result = Unique(sorted(field(arg, "job-name"), reverse=True), ignore_case=True)  # type: ignore
    return result


@print_result
def f2(arg):
    return filter(lambda x: True if "программист" in x else False, arg)


@print_result
def f3(arg):
    return map(lambda x: x + " с опытом Python", arg)


@print_result
def f4(arg):
    list_from_arg = list(arg)
    return dict(zip(list_from_arg, gen_random(len(list_from_arg), 100000, 200000)))


if __name__ == "__main__":
    with cm_timer_1():
        f4(f3(f2(f1(data))))
