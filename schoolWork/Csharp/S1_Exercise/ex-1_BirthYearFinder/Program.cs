namespace BirthYearFinder
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("\tBirth_Year_Finder\nEnter your age:");
            int birthYear = DateTime.Now.Year - int.Parse(Console.ReadLine());
            Console.WriteLine("Your Birth Year :" + birthYear);
        }
    }
}
