// https://projecteuler.net/problem=69
package main

import (
	"euler/timer"
	"fmt"
	"math"
)

func main() {
	defer timer.Timer("main")()
	maxN := 1_000_000
	primes := sievePrimes69(maxN)
	n := 1
	// Find highest number under 1,000,000 with only prime factors.
	for i := 0; n <= maxN/primes[i+1]; i++ {
		n *= primes[i]
	}
	fmt.Println(n)
}

func slowSolution() {
	// Find max n / phi(n) (Euler's Totient function) for n <= 1,000,000
	maxN := 1_000_000
	maxRatio := 0.0
	ans := 0
	c := 0.0
	for i := 2; i <= maxN; i++ {
		factors := findPrimeFactors1(i)
		// c is Euler's Totient function result.
		c = float64(i)
		for k, _ := range factors {
			c = c * (1.0 - (1.0 / float64(k)))
		}
		if maxRatio < float64(i)/c {
			maxRatio = float64(i) / c
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

func sievePrimes69(max int) []int {
	// Returns slice of prime numbers less than the given int.
	tf := make([]bool, max)
	for i, _ := range tf {
		tf[i] = true
	}

	maxI := int(math.Sqrt(float64(max))) + 1
	for i := 2; i < maxI; i++ {
		if tf[i] {
			for j := i * i; j < maxI; j += i {
				tf[j] = false
			}
		}
	}

	primes := make([]int, 0)
	for i, v := range tf[2:] {
		if v {
			primes = append(primes, i+2)
		}
	}

	return primes
}
