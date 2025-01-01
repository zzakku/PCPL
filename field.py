# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def field(items: list[dict], *args):
    argcnt = len(args)

    # items - список словарей, position - словарь из списка, fld - поле из переданных аргументов

    if argcnt == 1:
        for position in items:
            for fld in args:
                yield position.get(fld)
    else:
        for position in items:
            searchres = {fld: position[fld] for fld in args}
            if searchres:
                yield searchres


if __name__ == "__main__":
    goods = [
        {"title": "Ковер", "price": 2000, "color": "green"},
        {"title": "Диван для отдыха", "price": 5300, "color": "black"},
    ]

    for f in field(goods, "title"):
        print(f)

    for f in field(goods, "title", "price"):
        print(f)
