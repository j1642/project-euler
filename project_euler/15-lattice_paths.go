package main

import (
    "fmt"
    "math/big"
)

func main() {
    // Number of paths through a 20x20 grid, only moving right and down.
    // 20*2 choose 20.
    fmt.Println(countCombinations(40, 20))
}

func countCombinations(n, r int64) *big.Int {
    bigN := big.NewInt(n)
    bigN = bigN.MulRange(2, n)
    bigFactorialRSquared := big.NewInt(factorial(r))
    bigFactorialRSquared = bigFactorialRSquared.Mul(
        bigFactorialRSquared,
        bigFactorialRSquared)
    return bigN.Div(bigN, bigFactorialRSquared)
}

func factorial(n int64) int64 {
    if n == 1 || n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

