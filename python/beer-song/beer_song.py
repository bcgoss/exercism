def song(start_at, end_at = 0):
  lyrics = ''
  for this_verse in range(start_at, end_at - 1, -1):
    lyrics += verse(this_verse) +"\n"
  return lyrics

def verse(start_at):
  bottles = str(start_at)
  next_verse = str(start_at - 1)

  if start_at > 2:
    return bottles + " bottles of beer on the wall, " + bottles + " bottles of beer.\nTake one down and pass it around, " + next_verse + " bottles of beer on the wall.\n"
  elif start_at == 2:
    return bottles + " bottles of beer on the wall, " + bottles + " bottles of beer.\nTake one down and pass it around, " + next_verse + " bottle of beer on the wall.\n"
  elif start_at == 1: 
    return bottles + " bottle of beer on the wall, " + bottles + " bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n"
  else:
    return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
