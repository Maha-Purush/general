number = float(input("Enter a denominator for the expression [1/number]:"))
try:
  print(1/number)
  number = float(input("Enter a denominator for the expression [1/number]:"))
except Exception:
    print("Enter a valid number.")