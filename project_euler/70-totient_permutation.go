// https://projecteuler.net/problem=70
package main

import (
	"euler/timer"
	"fmt"
	"math"
)

func main() {
	/* Find the smallest n / phi(n) (Euler's Totient function) for
	   n <= 10,000,000 where phi(n) is a permutation of the digits of n.*/
	defer timer.Timer("main")()
	maxN := 10_000_000
	minRatio := math.Inf(1)
	ans := 0
	totient := 0.0
	primes := sievePrimes70(maxN)

	for i := 2; i < maxN; i++ {
		totient = float64(i)
		reduced := i
		for _, prime := range primes {
			if prime*prime > reduced {
				break
			}
			if reduced%prime != 0 {
				continue
			}
			for reduced%prime == 0 {
				reduced /= prime
			}
			totient -= totient / float64(prime)
			if minRatio < float64(i)/totient {
				break
			}
		}
		/* Account for any missed factors, sometimes due to breaks in the
		   for block above (like for i=2).*/
		if reduced > 1 {
			totient = totient - totient/float64(reduced)
		}
		if minRatio < float64(i)/totient {
			continue
		}
		if isPermutation(i, int(totient)) {
			minRatio = float64(i) / totient
			ans = i
		}
	}

	fmt.Println(ans, minRatio)
}

func isPermutation(n, m int) bool {
	// Compare digit histograms.
	histN, err := intToHist(n)
	if err != nil {
		panic(err)
	}
	histM, err := intToHist(m)
	if err != nil {
		panic(err)
	}

	return histN == histM
}

func intToHist(n int) ([10]int, error) {
	// Returns a histogram of the digits in the given int.
	hist := [10]int{}
	digits, err := intToRevSlice(n)
	if err != nil {
		return hist, err
	}
	for _, digit := range digits {
		hist[digit] += 1
	}

	return hist, nil
}

func intToRevSlice(n int) ([]int, error) {
	// Returns reversed slice of given int. Undoing the reversal is unnecessary.
	if n < 0 {
		return nil, fmt.Errorf("int less than 0 not supported. got=%d", n)
	}
	digits := []int{}
	for n != 0 {
		digit := n % 10
		digits = append(digits, digit)
		n /= 10
	}

	return digits, nil
}

func sievePrimes70(max int) []int {
	// Returns slice of prime numbers less than the given int.
	defer timer.Timer("sievePrimes70")()
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
