using System.Numerics;

namespace ex_3_gradeCalculator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\tGrade Calculator");
            Console.Write("OOP :");
            double oop = double.Parse(Console.ReadLine());
            Console.Write("Satistic :");
            double sat = double.Parse(Console.ReadLine());
            Console.Write("English :");
            double eng = double.Parse(Console.ReadLine());
            Console.Write("Writing Skill :");
            double writ = double.Parse(Console.ReadLine());
            Console.Write("Microprocessor :");
            double micro = double.Parse(Console.ReadLine());
            Console.Write("DataBase :");
            double db = double.Parse(Console.ReadLine());
            Console.Write("Python :");
            double py = double.Parse(Console.ReadLine());
            double total = oop + sat + eng + writ + micro + db + py;
            double avg = total / 7;
            Console.WriteLine("Average :" + avg);
            Console.WriteLine("Total :" + total);
            if (avg > 90)
            {
                Console.WriteLine("Your grade is A");
            }
            else if (avg > 80)
            {
                Console.WriteLine("Your grade is B");
            }
            else if (avg > 70)
            {
                Console.WriteLine("Your grade is C");
            }
            else if (avg > 60)
            {
                Console.WriteLine("Your grade is D");
            }
            else if (avg > 50)
            {
                Console.WriteLine("Your grade is E");
            }
            else
            {
                Console.WriteLine("Your grade is F");
            }
        }
    }
}
