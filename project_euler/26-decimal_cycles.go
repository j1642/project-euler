// https://projecteuler.net/problem=26
package main

import (
	"fmt"
	"math"
)

func main() {
	// Find longest recurring decimal cycle of 1 / d, for d < 1000.
	primes := sievePrimes(1000)
	maxCycle := 0
	maxPrime := 0
	for _, p := range primes {
		cycleLength := findCycleLength(p)
		if maxCycle < cycleLength {
			maxCycle = cycleLength
			maxPrime = p
		}
	}
	fmt.Println(maxPrime)
}

func findCycleLength(n int) int {
	seen := make(map[int]int)
	remainder := 10
	for i := 0; ; i++ {
		if remainder == 0 {
			return 0
		} else if seen[remainder] != 0 {
			return i - seen[remainder]
		}
		seen[remainder] = i
		remainder = 10 * (remainder % n)
	}
}

func sievePrimes(max int) []int {
	tf := make([]bool, max)
	for i, _ := range tf {
		tf[i] = true
	}
	for i := 2; i < int(math.Sqrt(float64(max)))+1; i++ {
		if tf[i] {
			for j := i * i; j < max; j += i {
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
