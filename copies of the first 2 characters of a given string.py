def copy_string(text,n):
    x=2
    if x>len(text):
        x=len(text)
    substr=text[: x]
    result=""
    
    for i in range(n):
        result=result+substr
        
    return result

copy_string("bangladesh", 3)