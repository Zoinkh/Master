using System;
using System.Text;
using System.Text.RegularExpressions;

namespace Password_Lock
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            Console.InputEncoding = Encoding.UTF8;
            while (true)
            {
                Console.Write("Enter Password: ");
                string password = Console.ReadLine();

                bool isValid = true;

                if (password.Length < 8)
                {
                    Console.WriteLine("Password is too short. (It must be at least 8 characters.)");
                    isValid = false;
                }

                if (!Regex.IsMatch(password, @"[A-Z]"))
                {
                    Console.WriteLine("Password must contain at least one uppercase letter.");
                    isValid = false;
                }

                if (!Regex.IsMatch(password, @"[a-z]"))
                {
                    Console.WriteLine("Password must contain at least one lowercase letter.");
                    isValid = false;
                }

                if (!Regex.IsMatch(password, @"\d"))
                {
                    Console.WriteLine("Password must contain at least one digit.");
                    isValid = false;
                }

                if (!Regex.IsMatch(password, @"[\W_]"))
                {
                    Console.WriteLine("Password must contain at least one special character (e.g., !, @, #, $).");
                    isValid = false;
                }

                if (!Regex.IsMatch(password, @"[\u1780-\u17FF]"))
                {
                    Console.WriteLine("Password must contain at least one Khmer character (ក-អ).");
                    isValid = false;
                }

                if (isValid)
                {
                    Console.WriteLine("Password is strong!");
                    break;
                }
            }
        }
    }
}
