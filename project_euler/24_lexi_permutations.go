package main

import (
	"fmt"
	"log"
	"strings"
)

func main() {
	// Find 1,000,000th lexicographic permutation of "0123456789".
	nums := strings.Split("0123456789", "")
	rev_ans := make([]string, 0, 10)
	permute(nums, 999_999, &rev_ans)

	fmt.Println(strings.Join(rev_ans, ""))
}

func permute(nums []string, rem int, rev_ans *[]string) {
	// 10! = 3,628,800 possible answers.
	// At the start, the first (10-1)! numbers start with 0.
	perm_count := factorial(len(nums) - 1)
	num_ind := rem / perm_count
	rem = rem % perm_count
	*rev_ans = append(*rev_ans, string(nums[num_ind]))

	if len(nums) > 1 {
		// Remove used number from 'nums.'
		new_nums := nums[:num_ind]
		if num_ind < len(nums)-1 {
			new_nums = append(new_nums, nums[num_ind+1:]...)
		}
		permute(new_nums, rem, rev_ans)
	}

}

func factorial(n int) int {
	if n < 0 {
		log.Fatal("invalid n. got=", n)
	}
	if n == 1 || n == 0 {
		return 1
	}
	return n * factorial(n-1)
}
