# string1= input("write 1st string: ")
# string2= input("write the 2nd string: ")

# if(len(string1)!=len(string1)):
#     print("the two strings are not anagram")
# else:
#     if sorted(string1)==sorted(string2):
#         print("the 2 strings are anagram")
#     else:
#         print("2 strings are not anagram")

# string1=["earth","knee","there","ether","three","eat","tea","fried","silent","state","elbow","below","taste","race","care","fired","heart","keen"]
string1=["a gentleman","elegant man","william Shakespeare","ill make a wise phrase","the oil pinky","i like python","whitehat loves you","who outlay thieves"]
dict={}
for i in string1:
    # print(i)
    w=sorted(i)
    # print(w)

    b="".join(w)
    # print(b)

    if(b in dict):
        dict[b].append(i)
    else:
        dict[b]=[i]

print(list(dict.values()))


