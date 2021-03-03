// Package gigasecond adds a giga second to the given time
package gigasecond

// import path for the time package from the standard library
import "time"

// AddGigasecond adds 1,000,000,000 seconds to the given time
func AddGigasecond(t time.Time) time.Time {
  gigasecond := time.Second * 1000000000
	return t.Add(gigasecond)
}
