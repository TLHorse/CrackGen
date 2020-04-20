import base64
import random
import GlobalSettings
import CrackGenPaths

###############
# CM Settings #
###############

gAlgorithmsCount = GlobalSettings.GUIAlgorithmsCount

##############
# Algorithms #
##############

def b64(inputStr):
    """
    Encode the string to its base64 value.
    """
    if inputStr is bytes:
        return base64.b64encode(inputStr)
    else:
        return base64.b64encode(inputStr.encode('utf-8'))

def allint(inputStr):
    """
    Pick up all the numbers in the string.
    """
    result = ""
    for i in inputStr:
        if i is int:
            result = result + str(i)
    return result

def allalp(inputStr):
    """
    Pick up all the letters(a~z) in the string.
    """
    result = ""
    for i in inputStr:
        if not i is int:
            result = result + str(i)
    return result

def re(inputStr):
    """
    Reverse the string. (e.g. re('hello') -> olleh)
    """
    inputList = list(str(inputStr))
    inputList.reverse()
    return "".join(inputList)

def upc(inputStr):
    """
    Make the string uppercased.
    """
    return inputStr.upper()

def lwc(inputStr):
    """
    Make the string lowercased.
    """
    return inputStr.lower()

def rul(inputStr):
    """
    Swap the uppercased and the lowercased letter in the string. (e.g. re)
    """
    return inputStr.swapcase()

###################
# Assistant Funcs #
###################

def randomOpSeq(count):
    resultSeq = []
    operators = ['b64', 'allint', 'allalp', 're', 'upc', 'lwc', 'rul']
    for i in range(count):
        resultSeq.append(random.choice(operators))
    return resultSeq

###############
# Global Args #
###############

gSeq = randomOpSeq(gAlgorithmsCount)
gSeq = randomOpSeq(gAlgorithmsCount) # Refresh 'gSeq' once to keep this value random every time.

#############
# Main Func #
#############

def writeCode():
    with open(f"{CrackGenPaths.projectPath}/CrackGenCM/main.swift", 'w') as f:
        f.write('''
import Foundation

extension String {
    func b64() -> String {
        let strData = self.data(using: .utf8)
        return strData!.base64EncodedString()
    }

    func allint() -> String {
        var result = ""
        for i in self { if i.isNumber { result.append(i) } }
        return result
    }

    func allalp() -> String {
        var result = ""
        for i in self { if i.isLetter { result.append(i) } }
        return result
    }

    func re() -> String {
        return String(self.reversed())
    }

    func upc() -> String {
        return self.uppercased()
    }

    func lwc() -> String {
        return self.lowercased()
    }

    func rul() -> String {
        var result = ""
        for i in self {
            if i.isUppercase {
                result.append(i.lowercased())
            } else if i.isLowercase {
                result.append(i.uppercased())
            } else {
                result.append(i)
            }
        }
        return result
    }
}

func verify() {
    // Get the registration input.
    print("Enter username: ", terminator: "")
    let usernameInput = readLine()!
    print("Enter serial code: ", terminator: "")
    let serialInput = readLine()!
    
''')
    
    with open(f"{CrackGenPaths.projectPath}/CrackGenCM/main.swift", 'a') as f:
        f.write('    let correctSerial = usernameInput')
        for i in gSeq:
            f.write(f".{i}()")
        f.write('''
    
    if correctSerial == serialInput {
        print("Hooray! You carcked this CM successfully!")
    } else {
        print("Uh-oh, the serial is wrong. Try again.")
        verify()
    }
}

verify()
''')

def clearCode():
    with open(f"{CrackGenPaths.projectPath}/CrackGenCM/main.swift", 'w') as f:
        f.write('')