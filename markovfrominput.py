import markovify
import re

# В этом файле лежит вся логика, касающаяся работы генератора текста, к которому обращается бот.
# model - обработнанный корпус текста, используемый ботом.


class PostText(markovify.Text):
    """
    Подкласс от класса markovify.Text. Создаёт корпус, полагая концом "предложения"
    в корпусе условный символ "¶" ("конец поста").
    """

    # Сейчас будем расшифровывать кое-что из родительского класса
    # reject_pat = re.compile(r"(^')|('$)|\s'|'\s|[\"(\(\)\[\])]")
    # "(начало строки ') ИЛИ (' конец строки) ИЛИ пробельный символ ' ИЛИ ' пробельный символ ИЛИ
    # ОДИН ИЗ СПИСКА: [", ((, ), [, ])]

    def sentence_split(self, text):
        return re.split(r"\s*¶\s*", text)

    # Регулярное выражение значит следующее: "Ноль и более пробельных символов, "конец поста", ноль и более пробельных символов"
    # (по-моему) (вроде как)

    def make_post(self, init_state=None, **kwargs):
        temp_sentence = self.make_sentence(init_state, **kwargs)
        if temp_sentence:
            while temp_sentence.count("#Роботник") > 1:
                temp_sentence = temp_sentence.replace(
                    "#Роботник", "", 1
                )  # Удаляем дубликаты хештега
            temp_sentence = temp_sentence.replace("#Роботник", "\n#Роботник")
            while temp_sentence.count("#ИИ5") > 1:
                temp_sentence = temp_sentence.replace("#ИИ5", "", 1)
            temp_sentence = temp_sentence.replace("#ИИ5", "\n#ИИ5")
            temp_sentence = temp_sentence.replace("П:", "\nП:")
            temp_sentence = temp_sentence.replace("С:", "\nС:")
            return temp_sentence
        else:
            return None


with open("sourcetext.txt", "r") as f:
    text = f.read()

model = PostText(text)
