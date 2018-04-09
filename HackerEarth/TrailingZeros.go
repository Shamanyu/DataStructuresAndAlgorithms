package main

import "fmt"

func main(){
	var number, trailing_zeros, divider, adder int
	fmt.Scanf("%d", &number)
	trailing_zeros = 0
	divider = 5
	adder = number/divider
	for adder > 0{
		trailing_zeros += adder
		divider *= 5
		adder = number/divider
	}
	fmt.Println(trailing_zeros)
}

