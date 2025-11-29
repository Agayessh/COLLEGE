using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP2_Yabut
{
    internal class Program
    {
        private static string sval1;

        static void Main(string[] args)
        {

            int val1, val2, totVal, totVal1, totVal2, totVal3;

            String sval1;
            Console.Write("Enter the 1st number: ");
            sval1 = Console.ReadLine();
            val1 = Int32.Parse(sval1);
            Console.Write("Enter the 2nd number: ");
            val2 = Int32.Parse(Console.ReadLine());

            totVal = val1 + val2;
            Console.WriteLine("The sum of the two numbers is: " + totVal);
            Console.ReadKey();

            totVal1 = val1 - val2;
            Console.WriteLine("The difference of the two numbers is: " + totVal1);
            Console.ReadKey();

            totVal2 = val1 * val2;
            Console.WriteLine("The product of the two numbers is: " + totVal2);
            Console.ReadKey();

            float qNum;
            qNum = (float)val1 / (float)val2;
            totVal3 = val1 / val2;
            Console.WriteLine("The quotient of the two numbers is: " + (qNum));
            Console.ReadKey();

            Console.WriteLine();

            int a, b, c, d, e, f, g, h;
            String sa;
            Console.Write("Enter the 1st Number: ");
            sa = Console.ReadLine();
            a = Int32.Parse(sa);
            Console.ReadKey();

            Console.Write("Enter the 2nd number: ");
            b = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            Console.Write("Enter the 3rd number: ");
            c = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            Console.Write("Enter the 4th number: ");
            d = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            Console.Write("Enter the 5th number: ");
            e = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            Console.Write("Enter the 6th number: ");
            f = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            g = a + b + c + d + e + f;
            h = g / 6;
            float qNum1;
            qNum1 = (float)g / (float)h;
            Console.WriteLine("The average is: " + (qNum1));
            Console.ReadKey();


        }

    }
}
