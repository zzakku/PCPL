/// Макрос, возвращающий наименьшее число из произвольного числа переданных.
/// Возможно, не очень дружит с числами разных типов...
macro_rules! min_of_n {
    
    // (Я уверен, что где-то в стандартной библиотеке такое уже есть)

    // Не уверен, что код снизу "работает", но вроде как попытка вызвать макрос 
    // без аргументов вынуждает компилятор ругаться, что хорошо :)
    () => {
        panic!("Attempted to find the smallest number in an empty number set")
    };

    ($($args:expr),*) => {
        {
        let mut smallest = usize::MAX;

        $(
            if smallest > $args
            {
                smallest = $args;
            }
        )*

        smallest
        }
    };
}

    /// Функция находит расстояние Левенштейна между двумя строками алгоритмом Вагнера — Фишера.
pub fn l_distance(s1: &str, s2: &str) -> usize
{
    // &str говорит о том, что входные строки лишь читаются, внешний контекст сохраняет владение ими.

    // Для Rust неверно предполагать, что символ кодируется одним байтом, поэтому длина строки считается не
    // функцией len(). Кроме того, невозможна индексация вида s1[i]... Грустно!

    let s1len = s1.chars().count();
    let s2len = s2.chars().count();

    if s1len == 0 && s2len == 0
    {
        return 0;
        // Тривиальный случай: обе строки пустые. Не требует вычисления D.
    }
    else if s1len == 0 && s2len > 0
    {
        return s2len;
        // Тоже тривиально: чтобы воспроизвести непустую строку в пустой, нужно
        // последовательно вставить в неё все символы непустой строки.
    }
    else if s2len == 0
    {
        return s1len;
        // Последний тривиальный случай аналогичен второму.
    }

    let cell_count = (s1len + 1) * (s2len + 1); // Общее число ячеек матрицы
    let mut d: Vec<usize> = vec![0; cell_count]; // Матрица D в виде одномерного вектора

    for i in 0..(s1len+1)
    {
        d[i * (s2len + 1)] = i;
    }

    for j in 1..(s2len+1)
    {
        d[j] = j;
    }

    // Если мы имеем невырожденный случай, то клетки первого столбца и первой строки
    // ("первой" в смысле математическом) заполняются по простому закону.
    // Я выделил эти два цикла из общего вложенного, чтобы не проверять i и j
    // лишний раз и уменьшить диапазоны i и j во вложенном цикле.

    for i in 1..(s1len+1)
    {
        for j in 1..(s2len+1)
        {
            let m = match s1.chars().nth(i - 1) == s2.chars().nth(j - 1) {
                true  => 0, // Совпадение
                false => 1, // Замена 
            };

            d[i * (s2len + 1) + j] = min_of_n!(
                d[(i - 1) * (s2len + 1) + j] + 1, // Удаление
                d[i * (s2len + 1) + (j - 1)] + 1, // Вставка
                d[(i - 1) * (s2len + 1) + (j - 1)] + m) // Замена/Совпадение   
        }
    }

//    print_matrix(&d, s2len + 1);

    d[s1len * (s2len + 1) + s2len]
}

    /// Функция находит расстояние Дамерау-Левенштейна упрощённым алгоритмом.
    /// Это означает, что любая подстрока может быть отредактирована не более одного раза.
    /// Это не всегда верно, если мы ищем названное расстояние в точности согласно его определению...
    /// но достаточно хорошо во многих случаях :)
pub fn s_d_distance (s1: &str, s2: &str) -> usize
{

    let s1len = s1.chars().count();
    let s2len = s2.chars().count();

    if s1len == 0 && s2len == 0
    {
        return 0;
    }
    else if s1len == 0 && s2len > 0
    {
        return s2len;
    }
    else if s2len == 0
    {
        return s1len;
    }

    let cell_count = (s1len + 1) * (s2len + 1); // Общее число ячеек матрицы
    let mut d: Vec<usize> = vec![0; cell_count]; // Матрица D в виде одномерного вектора

    for i in 0..(s1len+1)
    {
        d[i * (s2len + 1)] = i;
    }

    for j in 1..(s2len+1)
    {
        d[j] = j;
    }

    // В отличие от расстояния Левенштейна мы также учитываем возможность транспозиции двух соседних символов

    for i in 1..(s1len+1)
    {
        for j in 1..(s2len+1)
        {
            let m = match s1.chars().nth(i - 1) == s2.chars().nth(j - 1) {
                true  => 0, // Совпадение
                false => 1, // Замена 
            };
            
            d[i * (s2len + 1) + j] = min_of_n!(
                d[(i - 1) * (s2len + 1) + j] + 1, // Удаление
                d[i * (s2len + 1) + (j - 1)] + 1, // Вставка
                d[(i - 1) * (s2len + 1) + (j - 1)] + m); // Замена/Совпадение
            if i > 1 && j > 1 &&
            s1.chars().nth(i) == s2.chars().nth(j - 1) &&
            s1.chars().nth(i - 1) == s2.chars().nth(j)
            {
                d[i * (s2len + 1) + j]  = min_of_n!(
                    d[i * (s2len + 1) + j],
                    d[(i - 2) * (s2len +1) + (j - 2)] + 1 // Транспозиция
                )                
            }
        }
    }

    d[s1len * (s2len + 1) + s2len]    
}    

/// Вывод матрицы, хранящейся как одномерный массив. Использовалось для тестирования.
#[allow(dead_code)]
fn print_matrix(m: &Vec<usize>, colcnt: usize) 
{
    let mut testout = String::new();
    let mut pos = 0;

    for i in m
    {
        pos = pos + 1;
        testout.push_str(&(i.to_string()));
        testout.push(' ');
        if pos % (colcnt) == 0
        {
            println!("{testout}");
            testout.clear();
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn levitest() {
        let result = l_distance("sitting", "kitten");
        assert_eq!(result, 3);
        let result = l_distance("polynomial", "exponential");
        assert_eq!(result, 6);
    }

    #[test]
    fn sdametest() {
        let result = s_d_distance("ca", "abc");
        assert_eq!(result, 3);
    }

    #[test]
    fn mintest() {
        let result = min_of_n!(545453,324356,2456);
        assert_eq!(result, 2456);
        let result = min_of_n!(2);
        assert_eq!(result, 2);
    }
}