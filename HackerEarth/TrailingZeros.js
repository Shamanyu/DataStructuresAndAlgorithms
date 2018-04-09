(function()
{
	var number, trailing_zeros, divider, adder;
	number = parseInt(prompt(""));
	trailing_zeros=0;
	divider=5;
	adder=number/divider;
	while(adder>0)
	{
		trailing_zeros+=adder;
		divider*=5;
		adder=number/divider;
	}
	alert(trailing_zeros);
});
	
