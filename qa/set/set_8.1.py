s1={4,5,2,7,64,3}
s2={5,7,32,42,13}
s3=set()
s3.update(s1)
s3.update(s2)
print(s3)
s3.remove(2)
print(s3)
print(max(s3))
print(min(s3))
print(len(s3))
s4=set()
s4.update(s3)
s4.add(31)
print(s4)
s1.clear()
s2.clear()
print(s1)
print(s2)