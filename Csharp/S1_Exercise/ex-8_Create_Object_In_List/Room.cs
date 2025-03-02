using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _8._1_._2
{
    class Room
    {
        public string RoomNumber { get; set; }
        public string Style { get; set; }
        public string Status { get;  set; }
        public double BookingPrice { get; set; }
        public bool IsSmoking { get; set; }
        public Room() { }
        public Room(string number, string style, string status, double price, bool issmoking)
        {
            this.RoomNumber = number;
            this.Style = style;
            this.BookingPrice = price;
            this.Status = status;
            this.IsSmoking = issmoking;
        }
        public void DisplayRoomDetail()
        { 
            Console.WriteLine("===============================");
            Console.WriteLine("Room Number:" + RoomNumber);
            Console.WriteLine("Room Style:" + Style);
            Console.WriteLine("Room Status:" + Status);
            Console.WriteLine("Price:" + BookingPrice);
            Console.WriteLine("Smoking:" + (IsSmoking ? "Yes" : "No"));
            Console.WriteLine("===============================");
        }
        public void EnterRoomDetails()
        {
            Console.Write("Enter Room Number: ");
            RoomNumber = Console.ReadLine();

            Console.Write("Enter Room Style (Single/Double/Suite): ");
            Style = Console.ReadLine();

            Console.Write("Enter Room Status (Available/Occupied/Maintenance): ");
            Status = Console.ReadLine();

            Console.Write("Enter Booking Price: ");
            double.Parse(Console.ReadLine());

            Console.Write("Is Smoking Allowed? (yes/no): ");
            string smokingInput = Console.ReadLine().ToLower();
            IsSmoking = smokingInput == "yes";
        }
    }
}
