namespace ex_9_Hote_lSystem
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var g1 = new Guest();
            g1.Name = "Mr. Visual Studio Code";
            g1.Address = "Phnom Penh";
            g1.Phone = "012306090";
            g1.DisplayGuestProfile();

            var r1 = new Receptionist("Ms. Word Document", "Takeo", "088789654", 7, 17);
            r1.DisplayReceptionistProfile();
        }
    }
}

