import keyword

print(keyword.kwlist) 
print("-------")
reverved_word =keyword.kwlist #kwlist
for i in range(0, len(reverved_word)):
    print("[{:^10}]".format(reverved_word[i]), end="")
    if( (i+1)%5 ==0):
        print("\n")
    