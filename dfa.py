from logger import log
# Complementary code for my tutorial on the basics
# of finite state machines.

# This machine recognises binary strings with an odd number of 1's

# Our set of states, Q
Q = ('qe', 'q0')

# Our transition function
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

# Our alphabet (set of symbols)
E = ('0', '1')

# The initial state
q = Q[0]

# The set of final states Q
F = ('q0')

# Now we formally define our deterministic automaton.
M = (Q, E, d, q, F)

string = '10001'

def is_accepted(string, q):
  for char in string:
    q = d(q, char)
  if q in F:
    return True
  else:
    return False

string1 = '1001' # Should be False
string2 = '00000000011100000000' # Should be True

assert(is_accepted(string1, q) == False)
assert(is_accepted(string2, q) == True)