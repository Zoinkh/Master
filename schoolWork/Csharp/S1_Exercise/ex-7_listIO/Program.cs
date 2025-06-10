namespace ex_6_listIO
{
    internal class Program
    {
        static void Main(string[] args)
        {         
            Console.Write("Enter Num (separated by spaces) :");        
            string input = Console.ReadLine();
            string[] inputArray = input.Split(' ');
            List<int> digits = new List<int>();
            foreach (var str in inputArray)
            {
                if (int.TryParse(str, out int result))
                {
                    digits.Add(result);
                }
            }
            if (digits.Count == 0)
            {
                Console.WriteLine("list is empty.");
                return;
            }
            int maxDigit = digits.Max();
            int minDigit = digits.Min();
            List<int> evenNumbers = digits.Where(d => d % 2 == 0).ToList();
            digits.Sort();
            Console.WriteLine($"Maximum : {maxDigit}");
            Console.WriteLine($"Minimum : {minDigit}");
            Console.WriteLine("Even numbers : " + string.Join(", ", evenNumbers));
            Console.WriteLine("Sorted list: " + string.Join(", ", digits));
        }
    }
}
