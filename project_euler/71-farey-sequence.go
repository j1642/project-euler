package main

import (
	"euler/timer"
	"fmt"
)

func main() {
	defer timer.Timer("main")()
	fmt.Println(binaryFareySearch())
}

func binaryFareySearch() int {
	goalN := 3
	goalD := 7
	max := 1_000_000

	// Beginning and end of Farey sequence
	leftN := 0
	leftD := 1
	rightN := 1
	rightD := 1

	for leftD+rightD <= max {
		mediantN := leftN + rightN
		mediantD := leftD + rightD

		if float64(mediantN)/float64(mediantD) < float64(goalN)/float64(goalD) {
			leftN = mediantN
			leftD = mediantD
		} else {
			rightN = mediantN
			rightD = mediantD
		}
	}
	return leftN
}
