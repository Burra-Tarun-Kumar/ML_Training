def dev_dec(func):
  def inner(a,b):
    if a<b:
      a,b=b,a
    return func(a,b)
  return inner
@dev_dec
def div(a,b):
  return a/b
print(div(2,4))
