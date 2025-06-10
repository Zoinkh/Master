namespace ex_5_reverseNum
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter num :");
            string num = Console.ReadLine();
            string reverse = string.Empty;
            for (int i = num.Length - 1; i >= 0; i--)
            {
                reverse += num[i];
            }
            Console.WriteLine("reversed num : " + reverse);
        }
    }
}
