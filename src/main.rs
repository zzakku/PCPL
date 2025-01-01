//Нужен Левенштейн с модульными тестами и хотя бы одним макросом

mod levenshtein;

use std::io::{
    stdin,
    stdout,
    Write
};

/// Чтение одной строки из консоли. По идее должно работать корректно на Windows и Linux.
/// Возвращает единичку, потому что... :3
fn read_input(buf: &mut String) -> usize
{
    let _ = stdout().flush(); // Убедимся, что в потоке ничего нет
    stdin()
        .read_line(buf)
        .expect("Invalid input");

    // Очищаем... trailing characters, хз как по-русски.
    // /r/n - Windows, /n - Unix
    if let Some('\n') = buf.chars().next_back() {
        buf.pop();
    }
    if let Some('\r') = buf.chars().next_back() {
        buf.pop();
    }

    1
}

fn main() {
    println!("Please enter the first UTF-8 string.");
    let mut s1 = String::new();

    read_input(&mut s1);

    let mut s2 = String::new();

    println!("Please enter the second UTF-8 string.");

    read_input(&mut s2);

    let distance = levenshtein::l_distance(&s1, &s2);
    let distance2 = levenshtein::s_d_distance(&s1, &s2);
    
    println!("Levenshtein distance between {s1} and {s2} is {distance}.");
    println!("Damerau-Levenshtein distance between {s1} and {s2} is {distance2}.");
}
