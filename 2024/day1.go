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

func solve() {

}

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

	// make difference and sum as we go
	sum := 0
	for i, l := range left {
		r := right[i]
		sum += absInt(l, r)
	}

	// print answer
	fmt.Printf("The answer is: %d", sum)
}
