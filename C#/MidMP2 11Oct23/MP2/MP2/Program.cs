using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP2
{
    class Program
    {
        static void Main(string[] args)
        {
            String[] illama = new string[10];
            Console.WriteLine("Enter the names: ");
            for (int y = 0; y < 10; y++)
            {
                illama[y] = Console.ReadLine();

            }

            Console.WriteLine("\nNames in reverse: " + " ");
            
            for (int y = 9; y > 0; y--)
            {
                Console.Write(illama[y]);
            }

            Console.ReadKey();
    
        }

    }
}
