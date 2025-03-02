using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ex_9_Hote_lSystem
{
    public class Person
    {
        public string Name { get; set; }
        public string Address { get; set; }
        public string Phone { get; set; }

        public Person() { }

        public Person(string Name, string Address, string Phone)
        {
            this.Name = Name;
            this.Address = Address;
            this.Phone = Phone;
        }

        protected void DisplayPersonProfile()
        {
            string info = $"Name: {Name}, Address: {Address}, Phone: {Phone}";
            Console.Write(info);
        }
    }
}
