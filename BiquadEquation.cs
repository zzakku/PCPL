using System;
using System.Text;
using System.Collections.Generic;

namespace Biquad
{
    /// <summary>
    /// Класс для работы с биквадратным уравнением
    /// </summary>
    class BiquadEquation
    {
        /// <summary>
        /// Вычисление корней
        /// </summary>
        public List<double> CalculateRoots(double a, double b, double c)
        {
            List<double> roots = new List<double>();
            double D = b * b - 4 * a * c;
            //Два потенциальных корня
            if (D == 0)
            {
                double subst_root = -b / (2 * a);
                if (subst_root > 0)
                {
                    double root1 = Math.Sqrt(subst_root);
                    double root2 = -1 * root1;    
                    roots.Add(root1);
                    roots.Add(root2);                
                }
                else if (subst_root == 0)
                {
                    double root = subst_root * (-1); // Костыль: иначе выведется "-0".  
                    roots.Add(root);      
                }
            }
            //Четыре потенциальных корня
            else if (D > 0)
            {
                double sqrtD = Math.Sqrt(D);
                double subst_root1 = (-b + sqrtD) / (2 * a);
                double subst_root2 = (-b - sqrtD) / (2 * a);
                if (subst_root1 > 0)
                {
                    double root1 = Math.Sqrt(subst_root1);
                    double root2 = -1 * root1;
                    roots.Add(root1);
                    roots.Add(root2);
                } 
                else if (subst_root1 == 0)
                {
                    double root1 = Math.Abs(subst_root1); // Костыль: иначе выведется "-0".  
                    roots.Add(root1);                        
                }

                if (subst_root2 > 0)
                {
                double root3 = Math.Sqrt(subst_root2);
                double root4 = -1 * root3;
                roots.Add(root3);
                roots.Add(root4);
                }
                else if (subst_root2 == 0)
                {
                    double root3 = Math.Abs(subst_root2); // Костыль: иначе выведется "-0".  
                    roots.Add(root3);                        
                }
            }
            return roots;
        }

        /// <summary>
        /// Вывод корней
        /// </summary>
        public void PrintRoots(double a, double b, double c)
        {
            List<double> roots = this.CalculateRoots(a, b, c);
            Console.Write("Коэффициенты: A={0}, B={1}, C={2}. ", a, b, c);
            if(roots.Count == 0)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Корней нет.");
                return;
            }

            Console.ForegroundColor = ConsoleColor.Green;

            if (roots.Count == 1)
            {
                Console.WriteLine("Один корень: {0}", roots[0]);
            }
            else if (roots.Count == 2)
            {
                Console.WriteLine("Два корня: {0} и {1}", roots[0], roots[1]);
            }
            else if (roots.Count == 3)
            {
                Console.WriteLine("Три корня: {0}, {1}, {2}", roots[0], roots[1], roots[2]);
            }
            else if (roots.Count == 4)
            {
                Console.WriteLine("Четыре корня: {0}, {1}, {2}, {3}", roots[0], roots[1], roots[2], roots[3]);
            }
        }

    }
}