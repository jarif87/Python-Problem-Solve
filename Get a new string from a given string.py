def New_string(text):
    if len(text)>=2 and text[: 2]=="Is":
        return text
    return "Is"+text

print(New_string("America"))
print(New_string("IsEmpty")) 


    