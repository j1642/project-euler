// https://projecteuler.net/problem=31
package main

import (
    "euler/timer"
    "fmt"
)

func main() {
    defer timer.Timer("main")()
    coins := [8]int{1, 2, 5, 10, 20, 50, 100, 200}
    goal := 200

    ways := [201]int{0}
    ways[0] = 1

    for _, coin := range coins {
        for pence := coin; pence < goal+1; pence++ {
            ways[pence] += ways[pence-coin]
        }
    }

    fmt.Println(ways[200])
}
