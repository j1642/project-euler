package main

import (
	"euler/timer"
	"fmt"
)

func main() {
	// Find max n / phi(n) (Euler's Totient function) for n <= 1,000,000
	defer timer.Timer("main")()
	maxN := 1_000_000
	maxVal := 0.0
	ans := 0
	c := 0.0
	for i := 2; i <= maxN; i++ {
		factors := findPrimeFactors1(i)
		// c is Euler's Totient function result.
		c = float64(i)
		for k, _ := range factors {
			c = c * (1.0 - (1.0 / float64(k)))
		}
		if maxVal < float64(i)/c {
			maxVal = float64(i) / c
			ans = i
		}
	}
	fmt.Println(ans)
}

func findPrimeFactors1(n int) map[int]bool {
	// Prime factorization by trial division.
	factors := make(map[int]bool)
	for n%2 == 0 {
		factors[2] = true
		n /= 2
	}
	for d := 3; d*d <= n; {
		if n%d == 0 {
			factors[d] = true
			n /= d
		} else {
			d += 2
		}
	}
	if n != 1 {
		factors[n] = true
	}
	return factors
}
