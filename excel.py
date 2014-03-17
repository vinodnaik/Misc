import sys
import string

def excel(input):
    n=len(input)
    hasht={}
    i=0;
    letters=string.lowercase[:26]
    input=input.lower()

    while i!= 26:
        hasht[letters[i]]=i+1
        i+=1
        
    no=0
    while(n!=0):
        no=no+(pow(26,(n-1))*hasht[input[-n]])
        n-=1

    return no

  
if __name__=='__main__':
    if len(sys.argv) <2:
        print "Provide command line arguments\n"
        exit(0)
    elif any(char.isdigit() for char in sys.argv[1]):
        print "Column numbers cannot contain numbers\nProvide valid column number"
        exit(0)
    print excel(sys.argv[1])

    
