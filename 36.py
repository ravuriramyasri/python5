import string
f = list(''.join(map(str,range(10))) + string.ascii_lowercase + ' ')
print len([i for i in raw_input().lower() if i not in f])
