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
            int num = 1;
            while (num < 40)
            {
                Console.WriteLine("First 20 natural numbers: " + num);
                num += 2;
            }
            Console.ReadKey();
        }
    }
}
