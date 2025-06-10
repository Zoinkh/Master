namespace ex_4_sumNum
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Num :");
            string input = Console.ReadLine();
            int sum = 0;
            foreach (char c in input)
            {

                if (char.IsDigit(c))
                {

                    sum += (c - '0');
                }
                else
                {
                    Console.WriteLine($"Invalid character '{c}' ");
                    return;
                }
            }  
            Console.WriteLine(" sum : " + sum);
        }
    }
}
