"""
an app gives and array of direction with ["n","s","e","w"]
determine if the app can make us walk 10 mn and return to the 
starting point...codewars

"""

def isValidWalk(walk):
    #determine if walk is valid
    if len(walk)==10:
        return walk.count("n")==walk.count("s") and walk.count("e")==walk.count("w")
    else: return False
    #return len(walk)==10 and walk.count("n")==walk.count("s") and walk.count("e")==walk.count("w")