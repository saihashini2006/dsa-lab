def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)
    
principal = 1000
rate = 0.05  
years = 3
          
amount = principal * power(1 + rate, years)

print("Final amount after", years, "years is:", amount)
