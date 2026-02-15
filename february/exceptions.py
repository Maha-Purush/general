  # number = float(input("Enter a denominator for the expression [1/number]:"))
  # try:
  #   print(1/number)
  #   number = float(input("Enter a denominator for the expression [1/number]:"))
  # except Exception:
  #     print("Enter a valid number.")

class IDKException(Exception):
  pass
try:
  number = float(input("Enter a denominator for the expression [1/number]:"))
  if number<=0:
    raise IDKException
  else:
    print(1/number)
except IDKException:
  print("bruh")
