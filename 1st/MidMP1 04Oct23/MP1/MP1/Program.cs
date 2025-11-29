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
            int z = 1;
            while (z < 11)
            {
                Console.WriteLine("First 10 natural numbers: " + z);
                z++;
            }
            Console.ReadKey();
        }
    }
}
