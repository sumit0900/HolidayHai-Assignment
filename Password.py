import re

#################################
####function to check password
################################

def passwordCheck(password):
    
    lengthError = 8 - len(password)     #checkong length of password
    if lengthError < 0:
        lengthError = 0
    totalError = 0
    if re.search(r"\d", password) == None:  #if any digit is there in password
        totalError += 1                     #if not then incrementing the error in password    
        

    if re.search(r"[A-Z]", password) == None:   #if any uppercase char is there in password
        totalError += 1

    if re.search(r"[a-z]", password) == None:   #if any lowercase char is there in password
        totalError += 1

    if re.search(r"[!@#$%^&*()-+]", password) == None:  #check for special char
        totalError += 1
    
    finalError = lengthError - totalError
    #checks error. If total error is less than or equal to length error
    #then minimum error is length error other wise finalError.
    if finalError < 1:
        return -1 * finalError
    else:
        return lengthError
    
if __name__=='__main__':
    value = input()
    print(passwordCheck(value))