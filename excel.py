import sys
import string

def excel(input):
    n=len(input)
    hasht={}
    idx=1;
    letters=string.lowercase[:26]
    input=input.lower()

    for letter in letters:
        hasht[letter]=idx
        idx+=1
        
    no=0
    for inp in input:
        no=no+(pow(26,n-1)*hasht[inp])
        n-=1

    return no

  
if __name__=='__main__':
    if len(sys.argv) <2:
        print "Provide command line arguments\n"
        exit(0)
    #elif any(char.isdigit() for char in sys.argv[1]):
    elif not sys.argv[1].isdigit():
        print "Column numbers cannot contain numbers\nProvide valid column number"
        exit(0)
    print excel(sys.argv[1])

    
