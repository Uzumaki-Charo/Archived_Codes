def duplicate_count(text):
    # Your code goes here
    text=text.lower()
    s=set(text)
    m=0
    for x in s:
        if text.count(x)>=2:
            m+=1
    return m
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])