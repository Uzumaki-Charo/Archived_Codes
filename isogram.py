def is_isogram(string):
    #your code here
    #return len(string) == len(set(string.lower()))
    string=string.lower()
    array=[0]*26
    alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i,v in enumerate(alp):
        array[i]=string.count(v)
        #return string.count(v)<=2
    #print(array)
    for i in range(0,len(array)):
        if array[i]>=2:
            return False
    return True

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))