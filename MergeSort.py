def MergeSort(A, p, r):
  if p < r:
    q = (p+r)//2
    MergeSort(A, p, q)
    MergeSort(A, q+1, r)
    Merge(A, p, q, r)
    
def Merge(A, p, q, r):
  
