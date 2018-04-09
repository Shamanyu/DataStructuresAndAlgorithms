N = int(raw_input(""))
laptop_count_dict = dict()
for counter in range(N):
	company = raw_input("")
	laptop_count_dict[company] = laptop_count_dict.get(company, 0) + 1
most_laptops_company = 'zzzzzzzzzzzzzzz'
most_laptops_count = 0 
for company in laptop_count_dict:
	if (laptop_count_dict[company] > most_laptops_count) or (laptop_count_dict[company] == most_laptops_count and company < most_laptops_company):
		most_laptops_company = company
		most_laptops_count = laptop_count_dict[company]
print most_laptops_company
