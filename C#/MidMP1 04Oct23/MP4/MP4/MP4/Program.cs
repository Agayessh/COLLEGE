using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MP4
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, nh;
            Console.Write("Enter the number: ");
            nh = Convert.ToInt32(Console.ReadLine());
            for (n=0; n <= nh; n++)
                {
                Console.Write("The number has the cube of: {0} \n", (n * n * n));
                }
            Console.ReadKey();
        }
    }
}
