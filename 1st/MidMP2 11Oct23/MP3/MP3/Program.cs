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
             for (int o = 1; o <= 10; o++)
            {
                for (int p = 1; p <= 10; p++)
                {
                    Console.Write(o * p + "\t");
                }

                Console.Write("\n");
            }
            Console.ReadKey();
        }
    }
}
