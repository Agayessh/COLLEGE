using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Yabut_Aleerah_M_LabExam
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] name = new string[5];
            string[] values = new string[5];
            float[,] values2 = new float[5,4];

            for (int p = 0; p <= 4; p++)
            {
                Console.WriteLine("The exam will have the following:");
                Console.WriteLine("Math, Reading, History");

                Console.WriteLine("\nPress ENTER to continue");

                Console.WriteLine("\nEnter your name: ");
                name[p] = Console.ReadLine();

                Console.Clear();

                float score1 = 0;
                float score2 = 0;
                float score3 = 0;
                float ave = 0;

                Console.WriteLine("\n Math:");
                Console.Write("\n1. What is 1 + 1?");
                Console.WriteLine("\nA " + "2");
                Console.WriteLine("B " + "1");
                Console.WriteLine("C " + "3");
                Console.WriteLine("D " + "4");
                Console.Write("\nAnswer: ");
                char answer1 = char.Parse(Console.ReadLine());
                if (answer1 == 'A')
                {
                    score1 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Math:");
                Console.Write("\n2. What is 7 * 7?");
                Console.WriteLine("\nA " + "52");
                Console.WriteLine("B " + "17");
                Console.WriteLine("C " + "38");
                Console.WriteLine("D " + "49");
                Console.Write("\nAnswer: ");
                char answer2 = char.Parse(Console.ReadLine());
                if (answer2 == 'D')
                {
                    score1 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Math:");
                Console.Write("\n3. What are the parts of Multiplication?");
                Console.WriteLine("\nA " + "Product & Multiplier");
                Console.WriteLine("B " + "Multiplier & Multiplicand");
                Console.WriteLine("C " + "Multiplicand & Product");
                Console.WriteLine("D " + "Product");
                Console.Write("\nAnswer: ");
                char answer3 = char.Parse(Console.ReadLine());
                if (answer3 == 'B')
                {
                    score1 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Math:");
                Console.Write("\n4. If m = 1, calculate 4 + m");
                Console.WriteLine("\nA " + "2");
                Console.WriteLine("B " + "5");
                Console.WriteLine("C " + "3");
                Console.WriteLine("D " + "4");
                Console.Write("\nAnswer: ");
                char answer4 = char.Parse(Console.ReadLine());
                if (answer4 == 'B')
                {
                    score1 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Math:");
                Console.Write("\n5. 10 * 0");
                Console.WriteLine("\nA " + "2");
                Console.WriteLine("B " + "5");
                Console.WriteLine("C " + "3");
                Console.WriteLine("D " + "0");
                Console.Write("\nAnswer: ");
                char answer5 = char.Parse(Console.ReadLine());
                if (answer5 == 'D')
                {
                    score1 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Reading:");
                Console.Write("\n1. Which of the following is an example of skimming a text?");
                Console.WriteLine("\nA " + "Focusing only on the most important ideas while ignoring details.");
                Console.WriteLine("B " + "Reading every word of the text slowly and carefull");
                Console.WriteLine("C " + "Using prior knowledge to make predictions about the text");
                Console.WriteLine("D " + "None of the above");
                Console.Write("\nAnswer: ");
                char answer6 = char.Parse(Console.ReadLine());
                if (answer6 == 'D')
                {
                    score2 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Reading:");
                Console.Write("\n2. Which of the following is an example of a non-fiction text?");
                Console.WriteLine("\nA " + "A science fiction story");
                Console.WriteLine("B " + "A fairy tale");
                Console.WriteLine("C " + "A historical biography");
                Console.WriteLine("D " + "A romance novel");
                Console.Write("\nAnswer: ");
                char answer7 = char.Parse(Console.ReadLine());
                if (answer7 == 'C')
                {
                    score2 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Reading:");
                Console.Write("\n3. What is the universal language?");
                Console.WriteLine("\nA " + "Science");
                Console.WriteLine("B " + "Mathematics");
                Console.WriteLine("C " + "English");
                Console.WriteLine("D " + "Morse Code");
                Console.Write("\nAnswer: ");
                char answer8 = char.Parse(Console.ReadLine());
                if (answer8 == 'C')
                {
                    score2 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Reading:");
                Console.Write("\n4. Do you like reading?");
                Console.WriteLine("\nA " + "Maybe");
                Console.WriteLine("B " + "Yes");
                Console.WriteLine("C " + "nah");
                Console.WriteLine("D " + "EwW");
                Console.Write("\nAnswer: ");
                char answer9 = char.Parse(Console.ReadLine());
                if (answer9 == 'B')
                {
                    score2 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n Reading:");
                Console.Write("\n5. What symbol do you use for asking questions?");
                Console.WriteLine("\nA " + ".");
                Console.WriteLine("B " + "!");
                Console.WriteLine("C " + "@");
                Console.WriteLine("D " + "?");
                Console.Write("\nAnswer: ");
                char answer10 = char.Parse(Console.ReadLine());
                if (answer10 == 'D')
                {
                    score2 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n History:");
                Console.Write("\n1. Who was the fourth president of the United States?");
                Console.WriteLine("\nA " + "Emilio Aguinaldo");
                Console.WriteLine("B " + "James Madison");
                Console.WriteLine("C " + "Napoleon");
                Console.WriteLine("D " + "You");
                Console.Write("\nAnswer: ");
                char answer11 = char.Parse(Console.ReadLine());
                if (answer11 == 'B')
                {
                 score3 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n History:");
                Console.Write("\n2. The United States bought Alaska from which country?");
                Console.WriteLine("\nA " + "Russia");
                Console.WriteLine("B " + "Sweden");
                Console.WriteLine("C " + "Norway");
                Console.WriteLine("D " + "Mongolia");
                Console.Write("\nAnswer: ");
                char answer12 = char.Parse(Console.ReadLine());
                if (answer12 == 'A')
                {
                 score3 += 1;
                }
                else { }

                Console.Clear();

                Console.WriteLine("\n History:");
                Console.Write("\n3. The United States bought Alaska from which country?");
                Console.WriteLine("\nA " + "Russia");
                Console.WriteLine("B " + "Sweden");
                Console.WriteLine("C " + "Norway");
                Console.WriteLine("D " + "Mongolia");
                Console.Write("\nAnswer: ");
                char answer13 = char.Parse(Console.ReadLine());
                if (answer13 == 'A')
                {

                 score3 += 1;

                }
                else { }

                Console.Clear();

                Console.WriteLine("\n History:");
                Console.Write("\n4.  Longest River in the world?");
                Console.WriteLine("\nA " + "Nile");
                Console.WriteLine("B " + "Dniper");
                Console.WriteLine("C " + "Amazon");
                Console.WriteLine("D " + "Kumagawa");
                Console.Write("\nAnswer: ");
                char answer14 = char.Parse(Console.ReadLine());
                if (answer14 == 'A')
                {
                 score3 += 1;
                 }
                else { }

                Console.Clear();

                Console.WriteLine("\n History:");
                Console.Write("\n5.  Which Country started the first newspaper in the world?");
                Console.WriteLine("\nA " + "USA");
                Console.WriteLine("B " + "China");
                Console.WriteLine("C " + "Russia");
                Console.WriteLine("D " + "Bhutan");
                Console.Write("\nAnswer: ");
                char answer15 = char.Parse(Console.ReadLine());
                if (answer15 == 'B')
                {

                 score3 += 1;

                }
                else { }

                Console.Clear();

                Console.WriteLine("The exam is now concluded, congratulations!");
                Console.WriteLine("Want to see your scores? Compare it to other people?");

                float sum = score1 + score2 + score3;

                Console.WriteLine("{0}'s score: {1}", p, sum, "/ 15");

                Console.ReadKey();
                Console.WriteLine("Gonna show it anyway");

                ave = (score1 + score2 + score3) / 3;

                if (ave >= 3.5)
                {
                    values[p] = "Passed";
                    Console.WriteLine("Passed");
                }

                else 
                {
                    values[p] = "Failed";
                    Console.WriteLine("Failed");
                }

                values2[p, 0] = score1;
                values2[p, 1] = score2;
                values2[p, 2] = score3;
                values2[p, 3] = ave;
                Console.Clear();
                    
            }

            for (int i = 0; i < 5; i++) 
            {
                Console.Write(name[i] + "\t");
                for (int o = 0; o < 4; o++) 
                {

                    Console.Write(String.Format("{0:0.00}", values2[i, o]) + "\t");

                }

                Console.Write(values[i] + "\t");
                Console.WriteLine();


            }

            Console.ReadKey();
        }
    }
}