# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input

# Program to Display Fibonacci Sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
def fibonacci():
  nterms = int(input("How many terms? "))
  if nterms <= 0:
     print("Only Positive numbers LOL!")
  else:
     print("Fibonacci sequence:")
     for i in range(nterms):
         print(recur_fibo(i))
       
if __name__ == "__main__":
    fibonacci()