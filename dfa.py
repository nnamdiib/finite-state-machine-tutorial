from logger import log
# Complementary code for my tutorial on the basics
# of finite state machines.

# This machine recognises strings with an odd number of 1's
Q = ('qe', 'q0')

E = ('0', '1')

# d(state, symbol) --> state
@log
def d(state, symbol):
  cs = state + symbol
  if cs == 'qe0':
    next_state = 'qe'
  elif cs == 'qe1':
    next_state = 'q0'
  elif cs == 'q00':
    next_state = 'q0'
  elif cs == 'q01':
    next_state = 'qe'
  return next_state

q = Q[0]

F = ('q0')

# Now we formally define our deterministic automaton.
M = (Q, E, d, q, F)

string = '10001'

def check_string(string, q):
  for char in string:
    q = d(q, char)
  if q == 'q0':
    print('{} is accepted'.format(string))
  else:
    print('{} is rejected'.format(string))

check_string('1001', q)
check_string('1', q)
check_string('10011', q)