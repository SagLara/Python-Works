# -*- coding: utf-8 -*-
def palindrome(word):
    word=word.split(" ")
    count=len(word)
    result=""
    for i in word:
        for j in i:
            result=result+j
            
    print("The word without spaces is :"+result +" and have #"+str(count)+" word(s)")
    
    reverse_word=result[::-1]
    print ("The reverse word is: "+str(reverse_word))
    
    if result==reverse_word:
        print("is palindrome")
    else:
        print("not is palindrome")

if __name__ == "__main__":
    word = str(raw_input("Enter a word: "))
    palindrome(word)
