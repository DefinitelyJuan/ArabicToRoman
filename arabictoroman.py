#Function that takes an arabic number and returns its roman equivalent
from numpy import intp


def getRoman(arabic):
    arabics = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans =  ["M", "CM", "D" , "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    i = 0
    roman = ""
    while(arabic > 0):
        quot = arabic // arabics[i] #Floor division, so it gets the integer part of the division
        arabic = arabic % arabics[i]
        while(quot > 0):
            roman = roman + romans[i]
            quot = quot - 1
        i = i + 1
    return roman
    
#Takes an string and returns true if it can be converted to integer.    
def isInteger(string):
    try:
        int(string) 
        return True
    
    except: 
        return False



if (__name__ == "__main__"):
    #Main block
    print("Welcome to the arabic-to-roman conversion app!\nMade by Juan Avila, 1100378")
    while(True):
        arabic = input("Enter the arabic number you want to convert: ")
        if(isInteger(arabic)):
            print(f"The roman number for {arabic} is: {getRoman(int(arabic))}")
        else:
            print("Entered value is not an integer")

        resp = input("Do you want to try another number (Y/N): ")
        if(resp.upper() == "N"):
            print("Thanks for using my program! Have a nice day!")
            input("Pres ENTER to exit...")
            break

