using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grade
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int nm, nm1, prelim, mid, final;
            String sprelim;
            Console.Write("Enter the Prelim grade: ");
            sprelim = Console.ReadLine();
            prelim = Int32.Parse(sprelim);
            Console.ReadKey();

            Console.Write("Enter the Midterm grade: ");
            mid = Int32.Parse(Console.ReadLine());
            Console.ReadKey();

            Console.Write("Enter the Final grade: ");
            final = Int32.Parse(Console.ReadLine());

            Console.ReadKey();

            Console.Write(prelim * 0.30);
            Console.Write(mid * 0.30);
            Console.Write(final * 0.40);

            nm = prelim + mid + final;
            nm1 = nm / 3;
            Console.WriteLine();
            Console.WriteLine("Overall Grade:" + (nm1));
            Console.ReadKey();

            if (nm1 >= 97)
            {
                Console.WriteLine("1.00");
            }
            else if (nm1 >= 93)
            {
                Console.WriteLine("1.25");
            }
            else if (nm1 >= 89)
            {
                Console.WriteLine("1.50");
            }
            else if (nm1 >= 85)
            {
                Console.WriteLine("1.75");
            }
            else if (nm1 >= 82)
            {
                Console.WriteLine("2.00");
            }
            else if (nm1 >= 79)
            {
                Console.WriteLine("2.25");
            }
            else if (nm1 >= 76)
            {
                Console.WriteLine("2.50");
            }
            else if (nm1 >= 73)
            {
                Console.WriteLine("2.75");
            }
            else if (nm1 >= 70)
            {
                Console.WriteLine("3.00");
            }
            else if (nm1 >= 70)
            {
                Console.WriteLine("5.00");
            }
            else if (nm1 >= 65)
            {
                Console.WriteLine("6.00");
            }
            else if (nm1 >= 60)
            {
                Console.WriteLine("0.00");
            }
            Console.ReadKey();
        }
    }
}
