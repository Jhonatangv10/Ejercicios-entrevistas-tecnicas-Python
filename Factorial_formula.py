def factorial(n):
  n_factorial = 1
  for x in range(1, n+1):
    y = n_factorial * (n-x)
    n_factorial += y
  return n_factorial
  
resultado = factorial(5)
print(resultado)
