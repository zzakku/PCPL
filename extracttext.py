import json

# Скрипт работает с экспортированными логами Telegram. В результате его работы
# генерируется файл sourcetext.txt с текстовым содержимым всех постов.

# Данный файл подогнан под обработку содержимого конкретного канала

path = "result.json"  # Путь до файла


def process_export_log(path):
    with open(path, "r") as f:
        data = json.load(f)  # Загружаем в память весь лог (плохо для больших файлов?)

    data = data["messages"]
    parsed_data = (
        list()
    )  # Строки в Питоне неизменяемые, а мы хотим активно работать с формируемой строкой
    droppable = False

    departments = [
        "#ФН",
        "#ИУ",
        "#СГН",
        "#МТ",
        "#РК",
        "#РКТ",
        "#ФВ",
        "#Э",
        "#ИБМ",
        "СМ",
        "#Л",
        "#ЮР",
        "#РЛ",
        "#БМТ",
    ]  # Список кафедр для произведения замены

    for m in data:  # Итерируемся по сообщениям
        if isinstance(m["text"], list):  # Пустые сообщения игнорируются

            temp_pd = (
                list()
            )  # Может так случиться, что в сообщении встретится нежелательный для корпуса контент
            droppable = False

            for mpart in m[
                "text"
            ]:  # Поле "text" каждого сообщения содержит список частей сообщения

                if isinstance(mpart, str) and not droppable:
                    temp_pd.append(mpart)
                    if mpart and mpart != " " and mpart[-1] != "\n":
                        temp_pd.append(" ")
                elif isinstance(mpart, dict) and not droppable:
                    if (
                        mpart["type"] != "link"
                        and mpart["type"] != "mention"
                        and mpart["type"] != "hashtag"
                    ):
                        temp_pd.append(mpart["text"])
                        temp_pd.append(" ")
                    elif mpart["type"] == "hashtag":
                        if (
                            mpart["text"][-1].isnumeric()
                            or mpart["text"].upper() in departments
                        ):
                            temp_pd.append("#ИИ5")
                        else:
                            temp_pd.append("#Роботник")
                        temp_pd.append(" ")
                    elif mpart["type"] == "link":
                        droppable = (
                            True  # Пропускаем сообщение с нежелательными элементами
                        )
                else:
                    continue

            if not droppable:
                temp_pd.append("¶")  # Знаком параграфа будем означать конец сообщения
                parsed_data.extend(temp_pd)
                parsed_data.append("\n\n")

    return "".join(parsed_data)


parsed_log = process_export_log(path)

with open("sourcetext.txt", "w") as f:
    print(parsed_log, file=f)
