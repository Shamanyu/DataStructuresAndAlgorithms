import java.math.*;
import java.util.Scanner;

public class CubeChange
{
    public static void main(String args[])
    {
	int test_cases, counter, sides_temp;
	BigInteger sides;
        Scanner scan = new Scanner(System.in);
	test_cases = scan.nextInt();
	for(counter=0;counter<test_cases;counter++)
	{
		sides_temp = scan.nextInt();
		sides = new BigInteger(Integer.toString(sides_temp));
		if(sides_temp == 1)
		{
			System.out.println("1");
		}
		else
		{
			System.out.println((((sides.pow(2)).multiply(BigInteger.valueOf(6))).add(sides.multiply(BigInteger.valueOf(-12)))).add(BigInteger.valueOf(8)));
		}
	}
    }
}
