package main

import (
	"euler/timer"
	"fmt"
)

var factorials74 [10]int

func main() {
	defer timer.Timer("main")()

	for i := 0; i < len(factorials74); i++ {
		factorials74[i] = factorial74(i)
	}

	countLen60 := 0
	for i := 0; i < 1_000_000; i++ {
		if chainLength(i) == 60 {
			countLen60 += 1
		}
	}

	fmt.Println(countLen60)
}

func chainLength(n int) int {
	sums := make(map[int]int, 30)
	count := 0
	for {
		sums[n] = 0
		count += 1
		n = digitFactorialSum(n)
		if _, ok := sums[n]; ok {
			break
		}
	}

	return count
}

func digitFactorialSum(n int) int {
	// Returns sum of the factorial of each digit.
	factorialSum := 0
	for n > 0 {
		factorialSum += factorials74[n%10]
		n /= 10
	}

	return factorialSum
}

func factorial74(n int) int {
	if n < 2 {
		return 1
	}
	return n * factorial74(n-1)
}
