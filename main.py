import math
def cz(n):
  x = [n]
  e = 0
  while x[e] != 1:
    if x[e] % 2 == 0:
      x.append(int((x[e])/2))
    else:
      x.append(int((3*(x[e]))+1))
    e += 1  
  return x

def chain(n):
  collatz = {}
  for x in range(2, n+1):
    collatz[x] = [cz(x)]
  return collatz
def longestChain(n):
  bruh = 2
  for x in range(2, n-1):
    if len(cz(x)) >= len(cz(bruh)):
      bruh = x
  print("Longest Chain: ", bruh)
  print("Length of Chain:",len(cz(bruh)))
  print("Chain\n",cz(bruh))
def Log2(x): 
    return (math.log10(x) / 
            math.log10(2));
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 
def isntPowerOfTwo(n):
  if(isPowerOfTwo(n)):
    return 2
  else:
    return 1
def shortestChainNotP2(n):
  bruh = 3
  for x in range(2, n):
        if isntPowerOfTwo(x) == 1:
          if len(cz(x)) <= len(cz(bruh)): 
            bruh = x
  print("Shortest Chain not power of 2:",bruh)
  print("Chain Length:",len(cz(bruh)))
  print("Chain:\n",cz(bruh))
def avgChainLength(n):
  bruh = 0
  for x in range(2, n):
    bruh += len(cz(x))
  print("Average Chain from numbers 1 to", n,":", (bruh/9999))

def main(n):
  longestChain(n)
  shortestChainNotP2(n)
  avgChainLength(n)
main(int(input("Range of evaluation: ")))