'''
What I could've done better/faster:
string to integer conversion!
Figuring out what the output is asking for before solving the problem
(Like duh, you should've made it clear to either return the minimum time or the index)
fiddling with contrainsts, like minimum size of array
Assume the simplest mistakes, then go into deeper dive if none are found
'''
def times_to_second(time):

  '''
  Given a time value in format HH:MM:SS,
  times_to_second returns the total time represented in seconds
  '''
  hours = int(time[:2])
  minutes = int(time[3:5])
  seconds = int(time[6:8])

  time = hours * 360 + minutes * 60 + seconds

  return time

def wonRace(times):
  '''
  Given an array times with strings of format HH:MM:SS,
  wonRace determines who won the race (the minimum) and
  returns the index of the winner, or returns -1 if array is empty
  '''
  n = len(times)
  minimum = 0
  for i in range(1, n):
    total_seconds = times_to_second(times[i])
    if times_to_second(times[minimum]) > total_seconds:
      minimum = i
  
  return minimum


if __name__ == '__main__':
  sample_times = ['12:37:29', '01:28:32', '05:32:10']
  result = wonRace(sample_times)
  assert result == 1
