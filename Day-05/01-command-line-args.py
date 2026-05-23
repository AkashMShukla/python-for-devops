import sys

def add(x,y):
    return(x+y)

num1=int(sys.argv[1])
operation=(sys.argv[2])
num2=int(sys.argv[3])

if operation == "add":
    print(add(num1,num2))
    
#print(operation(num1,num2))
"""
sys.argv[2] returns the command-line argument as a string datatype. A string only stores text data and does not contain executable behavior.
Therefore, when you assign:
operation = sys.argv[2]
operation stores text like "add" instead of the actual add function reference.
"""