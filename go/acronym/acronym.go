// Package acronym provides a function for abbreviating long names
package acronym

import (
          "strings"
          "regexp"
)

// Abbreviate provides an acronym derived from the provided name
func Abbreviate(name string) string {
  name = cleanNonWordCharacters(name)
  names := strings.Split(name, " ")
  acronym := ""
  for _, word := range names {
    if len(word) > 0 {
      first_rune := strings.ToUpper(string([]rune(word)[0]))
      acronym += first_rune
    }
  }
  return acronym
}

func cleanNonWordCharacters(name string) string {
  expression := regexp.MustCompile("[^A-Za-z0-9']")
  return expression.ReplaceAllString(name, " ")
}

