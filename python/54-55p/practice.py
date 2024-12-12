def two_sum(array:list,target:int):
  res = []
  for j in range(len(array)-1):
    for i in array:
      if i + array[j+1] == target:
        res.append(i.)
        res.append(array[j+1])
        return res
      elif i + array[j+2] == target:
        res.append(i)
        res.append(array[j+2])
      else:
        return res
print(two_sum([3,3],6))