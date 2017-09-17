# Complementary code for my tutorial on the basics
# of finite state machines.

Q = set(('a', 'b', 'c', 'd')))

# d(state, symbol) --> state
def d(state, symbol):
  pass

q0 = Q[0]

F = set(('d', 'c'))

# Now we formally define our deterministic automaton.
M = (Q, E, d, q0, F)