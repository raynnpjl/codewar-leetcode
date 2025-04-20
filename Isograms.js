// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// Example: (Input --> Output)

// "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

// isIsogram "Dermatoglyphics" = true
// isIsogram "moose" = false
// isIsogram "aba" = false

function isIsogram(str){
    const check = []
    const lowerCaseStr = str.toLowerCase()
    for (i = 0; i < lowerCaseStr.length; i++) {
        if (!check.includes(lowerCaseStr[i])) {
            check.push(lowerCaseStr[i])
        } else {
            return false
        }
    }
    return true
  }

console.log(isIsogram("moOse"))

// optimal_solution >
// function isIsogram(str){
// 	return new Set(str.toUpperCase()).size == str.length;
// }