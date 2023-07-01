package main

import (
	"euler/timer"
	"fmt"
)

func main() {
	// Prime sieve-esque approach for solving 1,000,000 totient functions.
	defer timer.Timer("main")()
	max := 1_000_001

	totients := make([]int, max)
	for i, _ := range totients {
		totients[i] = i
	}
	// Skip totient functions of 0 and 1.
	for i, totient := range totients[2:] {
		i += 2
		if totient == i {
			for j := 1; j*i < max; j++ {
				totients[i*j] -= totients[i*j] / i
			}
		}
	}

	sum := 0
	for _, totient := range totients[2:] {
		sum += totient
	}

	fmt.Println(sum)
}
