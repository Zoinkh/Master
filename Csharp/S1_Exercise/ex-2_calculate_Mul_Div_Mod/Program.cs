namespace ex_2_calculate_Mul_Div_Mod
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("\tCalculate Multiply, Divide,and Module\n A :");
            int A = int.Parse(Console.ReadLine());
            Console.Write("B :");
            int B = int.Parse(Console.ReadLine());
            Console.WriteLine($"Multiply : {A} * {B} = {A * B}");
            Console.WriteLine($"Divide : {A} / {B} = {A / B}");
            Console.WriteLine($"Module : {A} % {B} = {A % B}");
        }
    }
}
