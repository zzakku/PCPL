import random

# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1


def gen_random(num_count, begin, end):
    random.seed()
    return [random.randrange(begin, end + 1) for i in range(num_count)]


if __name__ == "__main__":
    print(gen_random(5, 1, 3))
