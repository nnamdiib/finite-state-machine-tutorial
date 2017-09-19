# log is a decorator we will use to print out each state
# transition from the initial to the final state.
# FUnction decorators are another cool aspect of Python.
import functools

def log(func):
  @functools.wraps(func) # Yup. We can still decorate functions within our decorator.
  def logged(*args):
    result = func(*args)
    print('I am in State %s,\
           I have received input %s,\
           I am going to State %s' % (args[0], args[1], result)
          )
    return result
  return logged