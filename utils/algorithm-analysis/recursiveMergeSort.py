def mergesort(m):
   if length(m) ≤ 1:
       return m
   else:
       middle = length(m) / 2
       for each x in m up to middle - 1:
           left += x
       for each x in m at and after middle:
           right += x
       left = mergesort(left)
       right = mergesort(right)
       if last(left) ≤ first(right):
          right += left
          return left
       result = merge(left, right)
       return result


def merge(left,right):
   while length(left) > 0 and length(right) > 0:
       if first(left) ≤ first(right):
           result += first(left)
           left = rest(left)
       else:
           result += first(right)
           right = rest(right)
   if length(left) > 0:
       result += rest(left)
   if length(right) > 0 
       result += rest(right)
   return result