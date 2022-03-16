import math
def inverse(value, lam):
  if lam == 0:
    return math.exp(value)
  return math.exp(math.log(lam * value + 1) / lam)
