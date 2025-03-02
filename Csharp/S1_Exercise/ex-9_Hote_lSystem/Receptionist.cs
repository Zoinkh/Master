using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_9_Hote_lSystem
{
    public class Receptionist : Person
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Phone { get; set; }
        public int StartHour { get; set; }
        public int EndHour { get; set; }

        public Receptionist(string name, string address, string phone, int startHour, int endHour)
        {
            Name = name;
            Address = address;
            Phone = phone;
            StartHour = startHour;
            EndHour = endHour;
        }

        public void DisplayReceptionistProfile()
        {
            Console.WriteLine($"Receptionist Name: {Name}");
            Console.WriteLine($"Address: {Address}");
            Console.WriteLine($"Phone: {Phone}");
            Console.WriteLine($"Working Hours: {StartHour} - {EndHour}");
        }
    }

}
