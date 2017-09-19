def log(func):
  def logged(*args):
    result = func(*args)
    print('I am in State %s,\
           I have received input %s,\
           I am going to State %s' % (args[0], args[1], result)
          )
    return result
  return logged