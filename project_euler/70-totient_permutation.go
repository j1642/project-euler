// https://projecteuler.net/problem=70
package main

import (
	"euler/timer"
	"fmt"
	"math"
)

func main() {
	/* Find the smallest n / phi(n) (Euler's Totient function) for
	   n <= 1,000,000 where phi(n) is a permutation of the digits of n.*/
	defer timer.Timer("main")()
	maxN := 10_000_000
	minRatio := math.Inf(1)
	ans := 0
	totient := 0.0
	primes := sievePrimes70(maxN)

	for i := 2; i < maxN; i++ {
		factors := findPrimeFactors70(i, primes)
		totient = float64(i)
		for k, _ := range factors {
			totient = totient * (1.0 - (1.0 / float64(k)))
		}
		if isPermutation(i, int(totient)) {
			if minRatio > float64(i)/totient {
				minRatio = float64(i) / totient
				ans = i
			}
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

func findPrimeFactors70(n int, primes []int) map[int]bool {
	/* Prime factorization by trial division of sieved primes.
	   Only distinct prime divisors are represented in the final map.*/
	factors := make(map[int]bool)
	if n%2 == 0 {
		factors[2] = true
		n /= 2
		for n%2 == 0 {
			n /= 2
		}
	}
	for _, d := range primes {
		if d*d > n {
			break
		}
		if n%d == 0 {
			factors[d] = true
			n /= d
		}
	}
	if n != 1 {
		factors[n] = true
	}

	return factors
}

func sievePrimes70(max int) []int {
	// Returns slice of prime numbers less than the given int.
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
