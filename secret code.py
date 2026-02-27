import random
import string

choice=input("type encode or decode: ")
message=input("enter your message: ")
words=message.split()
result=[]

for word in words:
    if choice == "encode":
        if len(word) > 3:
            word=word[1:]+word[0]
            rand1=random.choice(string.ascii_letters)
            rand2=random.choice(string.ascii_letters)
            rand3=random.choice(string.ascii_letters)

            start=rand1+rand2+rand3
            end=rand1+rand2+rand3

            word=start+word+end

        else:
            word=word[::-1]

    if choice == "decode":
        if len(word) < 3:
            word=word[::-1]
        
        else:
            word=word[3:-3]
            # word = word[-1] + word[:-1]
        
result.append(word)
print("result: "," ".join(result))