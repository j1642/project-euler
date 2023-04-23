package main

import (
    "fmt"
    "log"
    "strconv"
    "strings"
    "os"
)


func main() {
    matrix := buildMatrix()
    maxSum := findMaxPathSum(matrix)
    fmt.Println(maxSum)
}

func findMaxPathSum(matrix [][]int) int {
    for i := len(matrix) - 1; i > 0; i-- {
        for j := 0; j < len(matrix[i]) - 1; j++ {
            if matrix[i][j] > matrix[i][j+1] {
                matrix[i-1][j] += matrix[i][j]
            } else {
                matrix[i-1][j] += matrix[i][j+1]
            }
        }
    }
    return matrix[0][0]
}

func buildMatrix() [][]int {
    f, err := os.ReadFile("67-nums.txt")
    if err != nil {
        log.Fatal(err)
    }
    rows := strings.Split(string(f), "\n")
    matrix := make([][]int, len(rows) - 1)
    for i, row := range rows {
        line := strings.Split(row, " ")
        // Why is the final line a slice of one empty string?
        if line[0] == "" && len(line) == 1 {
            break
        }
        matrix[i] = make([]int, i + 1)
        for j, digits := range line {
            num, err := strconv.Atoi(digits)
            if err != nil {
                log.Fatal(err)
            }
            matrix[i][j] = num
        }
    }
    return matrix
}
