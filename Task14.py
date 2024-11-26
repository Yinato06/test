calls = 0


def countCalls():
    global calls
    calls += 1


def stringInfo(string):
    countCalls()
    return len(string), string.upper(), string.lower()


def isContains(string, listSearch):
    countCalls()
    lowerString = string.lower()
    for element in listSearch:
        if element.lower() == lowerString:
            return True
    return False


print(stringInfo('Aboltys'))
print(stringInfo('Ratatatata'))
print(isContains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(isContains('Alexa', ['AlEXEy', 'aLESha', 'aLExa', 'AleXANDer']))
print(isContains('Denis', ['Denchik', 'Vasiliy', 'AleXANDer', 'Evsegney']))
print(calls)
