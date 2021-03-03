// Package bob provides a stimulating conversation partner
package bob

import (
        "strings"
)

// Hey responds to an individual remark
func Hey(remark string) string {
  switch  {
    case isShouting(remark) && isQuestion(remark):
      return "Calm down, I know what I'm doing!"
    case isShouting(remark):
      return "Whoa, chill out!"
    case isQuestion(remark):
      return "Sure."
    case isSilence(remark):
      return "Fine. Be that way!"
    default:
      return "Whatever."
  }
}

func isShouting(remark string) bool {
  return remark == strings.ToUpper(remark) && remark != strings.ToLower(remark)
}

func isQuestion(remark string) bool {
  return strings.HasSuffix(strings.TrimSpace(remark), "?")
}

func isSilence(remark string) bool {
  return strings.TrimSpace(remark) == ""
}

