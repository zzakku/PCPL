# Итератор для удаления дубликатов
class Unique(object):
    # Bool-параметр ignore_case определяет, будут ли считаться одинаковыми строки в разном
    # регистре.
    # Например: ignore_case = True, Aбв и АБВ - разные строки
    #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
    # По-умолчанию ignore_case = False
    def __init__(self, items, **kwargs):
        self.data = items
        self.used_elements = set()
        self.index = 0
        if kwargs.get("ignore_case") != None:
            self.ignore_case = kwargs.get("ignore_case")
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]  # текущий элемент из коллекции
                self.index = self.index + 1  # следующий за ним номер
                if (current not in self.used_elements and self.ignore_case == True) or (
                    str(current).casefold() not in self.used_elements
                    and self.ignore_case == False
                ):
                    if self.ignore_case == False:
                        self.used_elements.add(str(current).casefold())
                        # при ignore_case = False множество уникальных элементов содержит строки только в нижнем регистре
                    else:
                        self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = ["a", "A", "b"]

    for item in Unique(data, ignore_case=True):
        print(item)
