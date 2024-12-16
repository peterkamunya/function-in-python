def trirecursion(k):
    if(k>0):
        result =k+trirecursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("The results are")
trirecursion(6)
    