package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

var day = 1

func convertStringToInt(s string) int {
	// string to int
	i, err := strconv.Atoi(s)
	if err != nil {
		// ... handle error
		panic(err)
	}
	return i
}

func absInt(x, y int) int {
	if x < y {
		return y - x
	}
	return x - y
}

func main() {
	// Open file
	file, err := os.Open("day" + strconv.Itoa(day) + "_input.txt")
	if err != nil {
		log.Fatal(err)
		return
	}
	defer file.Close()

	// Create a scanner
	scanner := bufio.NewScanner(file)

	var left []int
	var right []int

	// Read and print lines
	for scanner.Scan() {
		line := scanner.Text()
		result := strings.Split(line, "   ")
		left = append(left, convertStringToInt(result[0]))
		right = append(right, convertStringToInt(result[1]))
	}

	// Check for errors
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	// sort left and right in place
	slices.Sort(left)
	slices.Sort(right)

	// go through values on the LEFT and make use of the fact they are ordered to slowly travel through the list on the right
	// such
	previous_value := 0
	j := 0
	result := 0
	count := 0
	for _, l := range left {
		if l == previous_value {
			// there's a duplicate in the left list
			// so we already calculated how many time it appears in the right and simply append the output
			result += l * count
			continue
		}

		// we are dealing with a new value in the left list so we rest the counter
		count = 0

		// while loop continue traveling over right slice until we either find a similar value as 'l' or something larger
		for j < len(right) {
			r := right[j]
			if l == r {
				// Increase the count and increment to next element in right slice
				count++
				j++
			} else if l < r {
				// the element in the left list is smaller than the right
				// thus we have finished going through all the values on the right that are equal to l
				// so we save the current counter and value and exit the while loop
				previous_value = l
				result += l * count
				break
			} else if l > r {
				// the element in the right list is smaller than the left
				// so we increment to next element in right slice
				// until it catches up to the left
				j++
				continue
			}
		}
	}

	// print answer
	fmt.Printf("The answer is: %d\n", result)
}
