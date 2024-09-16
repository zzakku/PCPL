using System;
using System.Text;
using System.Collections.Generic;

namespace Biquad
{
    class Program
    {
        static void Main(string[] args)
        {
            double[] coeffs = [0, 0, 0];
            char[] aliases_for_coeffs = ['A', 'B', 'C']; // Для подстановки в строчку "Введите коэффициент..."
            if (args.Length == 0) // Из командной строки ничего не передано? Переходим в режим "ручного управления"
            {
                for (int i = 0; i < 3; )
                {
                    do
                    {
                        Console.Write("Введите коэффициент {0}: ", aliases_for_coeffs[i]);                        
                    } while (!double.TryParse(Console.ReadLine(), out coeffs[i]) || (coeffs[0] == 0));         

                    i++; // Переходим на следующую итерацию цикла, как только коэффициент обрёл приемлемое значение      
                }
                
                BiquadEquation problem = new BiquadEquation();
                problem.PrintRoots(coeffs[0], coeffs[1], coeffs[2]);

                Console.ResetColor();
            }
            else if (args.Length == 3)
            {
                for (int i = 0; i < 3; )
                {
                    if (!double.TryParse(args[i], out coeffs[i]) || (coeffs[0] == 0))
                    {
                        Console.WriteLine("Неверный ввод. Попробуйте заново.");
                        return;
                    }        

                    i++; // Переходим на следующую итерацию цикла, как только коэффициент обрёл приемлемое значение      
                }
                
                BiquadEquation problem = new BiquadEquation();
                problem.PrintRoots(coeffs[0], coeffs[1], coeffs[2]);

                Console.ResetColor();                
            }
            else
            {
                Console.WriteLine("Программа принимает на вход либо 0, либо 3 аргумента. Попробуйте заново.");
            }
        }
    }
}

