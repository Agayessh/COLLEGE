using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP3
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = 0;
            double sum = 0;
            double number;
            Console.Write("Count of Numbers: ");
            double n = Convert.ToDouble(Console.ReadLine());

            while (true)
            {
                if (num == n)
                {
                    break;
                }
                Console.Write("Number {0} : ", num + 1);
                number = Int32.Parse(Console.ReadLine());
                sum += number;
                num++;

            }
            Console.WriteLine("===============================");
            float qNum;
            qNum = (float)sum / (float)n; 
            Console.WriteLine("Sum of Numbers is:" + sum);
            Console.WriteLine("Average of numbers is:" + (qNum));
            Console.ReadKey();
        }
    }
}
