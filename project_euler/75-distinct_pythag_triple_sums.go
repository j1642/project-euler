// https://projecteuler.net/problem=75
package main

import (
	"euler/timer"
	"fmt"
)

func main() {
	defer timer.Timer("main")()
	fmt.Println(findEuclidTriples())
}

func findEuclidTriples() int {
	a, b, c := 0, 0, 0
	lengths := make(map[int]bool)
	maxSum := 1_500_000

	// Unsure of how to optimally limit the outer "m" loop's repetitions.
	for m := 2; m < maxSum/2; m++ {
		for n := 1; n < m; n++ {
			if m%2 == n%2 {
				continue
			}
			if euclidGCD(n, m) != 1 {
				continue
			}
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			if a+b+c > maxSum {
				break
			}

			// Scale up primitive triples to be just under maxSum.
			perimeter := a + b + c
			i := 1
			for i*perimeter < maxSum {
				if _, ok := lengths[i*perimeter]; ok {
					lengths[i*perimeter] = false
				} else {
					lengths[i*perimeter] = true
				}
				i += 1
			}
		}
		if a+b+c > maxSum {
			continue
		}
	}
	count := 0
	for _, v := range lengths {
		if v {
			count += 1
		}
	}

	return count
}

func euclidGCD(n, m int) int {
	for m != 0 {
		n, m = m, n%m
	}
	return n
}
