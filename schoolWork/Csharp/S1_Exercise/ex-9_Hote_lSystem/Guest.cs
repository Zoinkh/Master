using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_9_Hote_lSystem
{
public class Guest : Person
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Phone { get; set; }

        public void DisplayGuestProfile()
        {
            Console.WriteLine($"Guest Name: {Name}");
            Console.WriteLine($"Address: {Address}");
            Console.WriteLine($"Phone: {Phone}");
        }
    }
    
}

