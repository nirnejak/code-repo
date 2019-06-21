package main

import "fmt"

func add(x float64, y float64) float64 {
	return x + y
}

func add2(x, y float64) float64 {
	return x + y
}

const x int = 5

func multiple(a, b string) (string, string) {
	return a, b
}

func main() {
	// Manual Typing
	var num1, num2 float64 = 5.6, 9.5
	fmt.Println(add(num1, num2))

	// Automatically detect type at compile time, after detection type will be fixed
	num3, num4 := 5.6, 9.5
	fmt.Println(add(num3, num4))

	w1, w2 := "Hey", "there"
	fmt.Println(multiple(w1, w2))

	var a int = 62
	var b float64 = float64(a) // Explicit Conversion

	x := a // x will be type int
}
