package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		fmt.Print(i)
	}

	fmt.Println("")

	j := 0
	for j < 10 {
		fmt.Print(j, " ")
		j++
	}

	fmt.Println("")

	x := 5
	for {
		fmt.Println("Do stuff", x)
		x += 3
		if x > 25 {
			break
		}
	}
}
