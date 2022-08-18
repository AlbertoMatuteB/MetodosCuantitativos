int[] result = new int[6];
Array.Clear(result, 0, 6);
Random rnd = new Random();
int i;
for(i = 0; i < 1000; i++)
{
    result[rnd.Next(0, 6)]++;
}

for(i = 0; i < 6; i++)
{
    Console.WriteLine((i+1) + "\t " +result[i] + "\n");
}
    