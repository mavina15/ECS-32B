# Mel Avina-Beltran
# 4/20/23
# H2 P4
# Goal: Allows the user to specify the direction of a selection sort

def selectionSort(lyst, reverse = False): 
  if not reverse:
    i=0
    while i < len(lyst) - 1: 
      minIndex = i 
      j=i+1
      while j < len(lyst):
        if lyst[j] < lyst[minIndex]:
          minIndex = j 
        j += 1
      if minIndex != i: 
        swap(lyst, minIndex, i)
      i += 1 
  else:
    i = len(lyst) - 1
    while i > 0: 
      minIndex = i 
      j=i-1 
      while j >= 0:
        if lyst[j] < lyst[minIndex]:
          minIndex = j 
          j -= 1
      if minIndex != i: 
        swap(lyst, minIndex, i)
      i -= 1

def swap(lyst, x, y):
  lyst[x], lyst[y] = lyst[y], lyst[x]

def main():
  lyst = [2, 4, 3, 0, 1, 5] 
  selectionSort(lyst) 
  print(lyst)
  lyst = list(range(6)) 
  selectionSort(lyst)
  print(lyst)
  lyst = [2, 4, 3, 0, 1, 5] 
  selectionSort(lyst, reverse = True) 
  print(lyst)
  lyst = list(range(6)) 
  selectionSort(lyst, reverse = True) 
  print(lyst)

if __name__ == "__main__": 
  main()