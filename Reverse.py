c=raw_input()
d=['a','e','i','o','u']
l=list(c)
for i in l:
    if i in d:
        l.remove(i)
l=(l[::-1])
l="".join(l)
print(l)
