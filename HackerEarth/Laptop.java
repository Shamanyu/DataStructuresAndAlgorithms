import java.util.*;

public class Laptop
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		HashMap<String, Integer> company_to_count_map = new HashMap<String, Integer>();
		int N = scan.nextInt();
		String company = new String();
		String best_selling_company = new String();
		best_selling_company = "zzzzzzzzzzzzzzzzzzzzzzzzzzz";
		int best_selling_quantity = 0;
		int counter;
		for(counter=0;counter<N;counter++)
		{
			company = scan.next();
			Integer present_value = new Integer(0);
			if(company_to_count_map.containsKey(company))
			{
				present_value = company_to_count_map.get(company);
			}
			company_to_count_map.put(company, present_value+1);
		}
		Iterator iterator = company_to_count_map.entrySet().iterator();
		while(iterator.hasNext())
		{
			Map.Entry company_info = (Map.Entry)iterator.next();
			if((int)company_info.getValue() > best_selling_quantity || ((int)company_info.getValue() == best_selling_quantity && (company_info.getKey().toString()).compareTo(best_selling_company) <= 0))
			{
				best_selling_company = company_info.getKey().toString();
				best_selling_quantity = (int)company_info.getValue();
			}
		}
		System.out.println(best_selling_company);
	}
}
	
