#Supporting file for e7.4.py

def testme(input):
    length = len(input)
    if length < 6 or input.isalpha() or input.isdigit():
        return False
    elif length > 6 or input.isalpha() or input.isdigit():
        return True



