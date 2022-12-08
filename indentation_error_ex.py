if True:
    print("Inside True")
     print("Will throw error because of extra whitespace")
else:
    print("False")

''''It will throw an IndentationError because the second print statement is written with one 
level indent, but it has extra whitespace, which is not allowed in Python.'''
