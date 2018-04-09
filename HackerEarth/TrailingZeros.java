import java.util.Scanner;

public class TrailingZeros
{
	public static void main(String []args)
	{
		int number, trailing_zeros, divider, adder;
		Scanner scan = new Scanner(System.in);
		number=scan.nextInt();
		trailing_zeros=0;
		divider=5;
		adder=number/divider;
		while(adder>0)
		{
			trailing_zeros+=adder;
			divider*=5;
			adder=number/divider;
		}
		System.out.println(trailing_zeros);
	}
}
