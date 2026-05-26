using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num = new int [15];
            int[] even = new int [15];
            int[] odd = new int[15];
            int Odd = 0;
            int Even = 0;

            Console.WriteLine("Enter 15 numbers: ");

            for (int z = 0; z < 15; z++)
            {
                num[z] = Convert.ToInt32(Console.ReadLine());

                if (num[z] % 2 == 0)
                {
                    even[Even] = num[z];
                    Even++;
                }
                else
                {
                    odd[Odd] = num[z];
                    Odd++;
                }
            }

            Console.Write("Odd Numbers: ");
            for (int z = 0; z < Odd; z++)
            {
                Console.Write(odd[z] + " ");
            }

            Console.Write("\nEven Numbers: ");
            for (int z = 0; z < Even; z++)
            {
                Console.Write(even[z] + " ");
            }
            Console.ReadKey();
        }
    }
}
