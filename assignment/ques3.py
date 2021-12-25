#counting number of strings
a= ["ama","bat","cat","d","eye"]
count = 0
for i in list(a):
    if len(i)>2:
        if i[0]==i[len(i-1)]:
            count=count+1

print(count)
