using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP3_Yabut
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int num, input;

            Console.WriteLine("Enter a number: ");
            input = int.Parse(Console.ReadLine());
            num = input % 2;

            if (num >= 1)
            {
                Console.WriteLine("It is an odd number");
            }
            else
            {
                Console.WriteLine("It is an even number");
            }
            Console.ReadKey();

            int prelim, midterm, finals;

        }
    }
}
