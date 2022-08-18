using System;
using Random;

public class Class1
{
	public Class1()
	{
		int[] result = new int[6] = 0;
		Random rnd = new Random();

		for(int i = 0; i < 1000; i++)
        {
			result[rnd.Next(5)]++;
        }

		for(int j = 0; j < 6; j++)
        {
			Console.WriteLine("Number " + j + " rolled: " + result[j] " times" + \n);
        }
	}
}
