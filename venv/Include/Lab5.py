import random
import string
import copy
from tkinter import messagebox





def generate_list_of_changes():
    s_random = string.ascii_lowercase
    n_max = 24
    n = random.randint(0, n_max)
    list_of_generated_chars = []
    list_of_chars = []
    i = 0
    while i<=n:
        random_char = random.choice(s_random)
        if random_char not in list_of_generated_chars:
            list_of_chars.append(random_char)
            i+=1
        else:
            continue
        list_of_generated_chars.append(random_char)
    return list_of_chars


def checking_s(s,list_of_chars):
    n = len(list_of_chars)
    result=n
    while n!=1:
        result=result*(n-1)
        n=n-1
    print(result)
    if s<=result:
        return True
    else:
        return False

s = int(input("Number of changings"))
list_of_chars = generate_list_of_changes()
FLAG = checking_s(s,list_of_chars)
print(list_of_chars, FLAG)
list_of_chars_summary=[]
list_of = copy.copy(list_of_chars)
list_of_chars_summary.append(list_of)
if FLAG:
    final=False
    while final==False or len(list_of_chars_summary)<=s:
        for i in range(len(list_of_chars),-1,-1):
            if list_of_chars[i-1]>list_of_chars[i-2]:
                i_remember = i-2
                print(i_remember,"-----")
                break
            final = True

        for i in range(len(list_of_chars),-1,-1):
            if list_of_chars[i_remember]<list_of_chars[i-1]:
                j_remember = i-1
        vrem = list_of_chars[i_remember]
        list_of_chars[i_remember]=list_of_chars[j_remember]
        list_of_chars[j_remember] = vrem
        list_of_chars[i_remember+1:] = reversed(list_of_chars[i_remember+1:])
        list_of_chars_copy=copy.copy(list_of_chars)
        list_of_chars_summary.append(list_of_chars_copy)

print(list_of_chars_summary)
text =""
for i in list_of_chars_summary:
    stroka = ", ".join(i)
    text+=stroka+"\n"
print(text)


