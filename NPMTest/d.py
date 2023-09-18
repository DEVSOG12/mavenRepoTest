c = "catsandog"


k = ["cats","dog","sand","and","cat"]

f = None
for i in range(len(k)):
    # print("".join(c.split(k[i]).pop()))
    f = "".join(c.split(k[i]).pop())
    print(f)

# Check if  of the elements in k is reused multiple times is in f
# if f in k or f == "" :
#     print("True")
# else:
#     print("False")

if f in k or f == "" or list(set(f))[0] in k or f in [list(set(l))[0] for l in k]:
    print("True")
else:
    print("False")



