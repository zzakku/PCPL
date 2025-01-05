import unittest
import classes

test_langs = [
    classes.Lang(1, "C"),
    classes.Lang(2, "Java"),
    classes.Lang(3, "Python"),
    classes.Lang(4, "C#"),
    classes.Lang(5, "B")
]

test_envs = [
    classes.Env(1, "Visual Studio", 1997, 4),
    classes.Env(2, "Eclipse", 2001, 2),
    classes.Env(3, "PyCharm", 2010, 3),
    classes.Env(4, "Vim", 1991, 1),
    classes.Env(5, "Borland Turbo C", 1987, 1),
]

test_langs_envs = [
    classes.EnvLang(1, 1),
    classes.EnvLang(3, 1),
    classes.EnvLang(4, 1),

    classes.EnvLang(2, 2),
    classes.EnvLang(1, 2),

    classes.EnvLang(3,3),

    classes.EnvLang(1,4),
    classes.EnvLang(3,4),

    classes.EnvLang(1,5)
]

# Соединение данных один-ко-многим 
test_one_to_many = [(l.name, e.name, e.init_release_yr) 
    for l in test_langs 
    for e in test_envs
    if e.lang_id==l.id]

# Соединение данных многие-ко-многим
test_many_to_many_temp = [(l.name, le.lang_id, le.env_id) 
    for l in test_langs 
    for le in test_langs_envs 
    if l.id==le.lang_id]

test_many_to_many = [(e.name, e.init_release_yr, lang_name) 
    for lang_name, lang_id, env_id in test_many_to_many_temp
    for e in test_envs if e.id==env_id]

class TestQueries(unittest.TestCase):
    
    def setUp(self):
        self.one_to_many = test_one_to_many
        self.many_to_many = test_many_to_many

    def test1(self):
        expected = [('C', 'Vim', 1991), ('C', 'Borland Turbo C', 1987), ('C#', 'Visual Studio', 1997)]
        result = classes.query1(self.one_to_many)
        self.assertEqual(expected, result)

    def test2(self):
        expected = [('C', 1987), ('C#', 1997), ('Java', 2001), ('Python', 2010)]
        result = classes.query2(self.one_to_many)
        self.assertEqual(expected, result)

    def test3(self):
        expected = {'Visual Studio': set(['C', 'C#', 'Python']), 'Vim': set(['C', 'Python'])}
        result = classes.query3(self.many_to_many)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()