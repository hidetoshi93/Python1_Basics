# làm tròn đến số thập phân

X = input().split(' ')
X = [int(i) for i in X]
sum = sum(X)
output = sum/len(X)
print ("%.1f" % output)