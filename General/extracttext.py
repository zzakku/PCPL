import json

# Скрипт работает с экспортированными логами Telegram. В результате его работы
# генерируется файл sourcetext.txt с текстовым содержимым всех постов.

path = "result.json"  # Путь до файла


def process_export_log(path):
    with open(path, "r") as f:
        data = json.load(f)  # Загружаем в память весь лог (плохо для больших файлов?)

    data = data["messages"]
    parsed_data = (
        list()
    )  # Строки в Питоне неизменяемые, а мы хотим активно работать с формируемой строкой

    for m in data:  # Итерируемся по сообщениям
        if isinstance(m["text"], list):  # Пустые сообщения игнорируются
            for mpart in m[
                "text"
            ]:  # Поле "text" каждого сообщения содержит список частей сообщения
                if isinstance(mpart, str):
                    parsed_data.append(" ")
                    parsed_data.append(mpart)
                elif isinstance(mpart, dict):
                    parsed_data.append(" ")
                    parsed_data.append(mpart["text"])
            parsed_data.append("\n\n")

    return "".join(parsed_data)


parsed_log = process_export_log(path)

with open("sourcetext.txt", "w") as f:
    print(parsed_log, file=f)
