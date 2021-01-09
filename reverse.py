#reverse the string
a= "london"
print(a[::-1])

#another option
def reverse_word(word):
    b=[]
    n=len(word)-1
    for letter in range(n+1):
        b.append(word[n])
        n-=1
        c= "".join(b)
    print(c)
reverse_word("New York")
