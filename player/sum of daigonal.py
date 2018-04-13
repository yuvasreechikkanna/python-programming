n = 3
a = [[11,2,4],[4,5,6],[10,8,-12]]
sum_first_diagonal = sum(a[i][i] for i in range(n))
sum_second_diagonal = sum(a[n-i-1][n-i-1] for i in range(n))
print(str(sum_first_diagonal)+" "+str(sum_first_diagonal))
