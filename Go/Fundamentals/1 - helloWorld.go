package main

import (
	"fmt"
	"math"
	"math/rand"
)

func foo1() {
	fmt.Println("Square root of 4 is", math.Sqrt(4))
}

func foo2() {
	fmt.Println("A number from 1-100", rand.Intn(100))
}

func main() {
	/* First Application */
	var age int

	age = 5

	fmt.Println("Hi there")
	fmt.Println(age)
	foo1()
	foo2()
}
