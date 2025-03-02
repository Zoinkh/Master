namespace _8._1_._2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<Room> rooms = new List<Room>();

            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"\nEntering details for Room {i + 1}:");
                Room room = new Room();
                room.EnterRoomDetails();
                rooms.Add(room);
            }


            foreach (var room in rooms)
            {
                room.DisplayRoomDetail();
            }
        }
    }
}
