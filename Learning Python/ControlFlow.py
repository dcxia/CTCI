##################################################
#    Control flow 
##################################################
# Tutorial can be found here. 
#https://docs.python.org/3/tutorial/controlflow.html
# 
##################################################


#input and wrapper Example
x = int(input("Please Enter an integer: "))

##################################################
# if Statements
if (x > 0) :
    print("positive")
elif (x==0) :
    print ("Zero")
else :
    print ("negative")

##################################################
# for Statements

# If you want to modify the array you're currently iterating over
# Create a copy using 'slicing'
words = [2,3,4]
for w in words:
    if w > 3 and len(words)<6:
        words.insert(0,0)

print(words)



#running through a copy of words using slicing
#original words is still kept
# words[:] creates a copy of words and allows it to be iterated through.
words = [2,3,4]
for w in words[:]:
    if w > 3:
        words.insert(0,0)

print(words)
##################################################