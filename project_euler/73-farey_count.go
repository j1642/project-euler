// https://projecteuler.net/problem=73
package main

import (
	"euler/timer"
	"fmt"
)

func main() {
	timer.Timer("main")()
	fmt.Println(countFarey(12000))
}

func countFarey(max int) int {
	/* Return the amount of fractions in the Farey sequence between 1/3
	   and 1/2, when the maxmimum denominator is 12,000.*/
	count := 0
	past1Over3 := false
	a, b, c, d := 0, 1, 1, max
	for c <= max {
		k := (max + b) / d
		a, b, c, d = c, d, k*c-a, k*d-b
		switch {
		case a == 1 && b == 3:
			past1Over3 = true
		case past1Over3:
			if a == 1 && b == 2 {
				return count
			}
			count += 1
		}
	}
	return -1
}
