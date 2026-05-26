using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter a number: ");
            int noo = Int32.Parse(Console.ReadLine());
            Console.WriteLine("The Fibonacci series " + noo + " number is : ");
            int d = 0, pq = 1;
            for (int x = 0; x < noo; x++)
            {
                Console.Write(d + " ");

                int next = d + pq;
                d = pq;
                pq = next;
            }
            Console.WriteLine();
            Console.ReadKey();
        }
    }
}
