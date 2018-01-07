
# Parse arguments likes:
# D:\Workspace\compile.py -e master  -r teacher -v 1.2.0.0

def getArgumentsFromString(str, splitFlag):
    "get argument array from string through splitFlag to split."

    if(splitFlag == ""):
        print("splitFlag is empty!")
        return ""

    data = str.split(splitFlag)
    result = []
    for item in data :
        item.strip()
        if(item != ""):
            result.append(item)

    return result;


def getValueFromArgument(flag, args):
    "get the argument value of the specific flag."

    count = len(args)
    for idx, item in enumerate(args):
        if(args[idx] == flag and idx < count - 1):
            return args[idx + 1]

    return ""


def testGetValue():
    args = getArgumentsFromString("D:\Workspace\compile.py -e master  -r teacher -v 1.2.0.0", ' ')
    value = getValueFromArgument('-r', args)
    print("value:" + value)
    # self.assertEqual(value, 'student', 'Result Fail')


testGetValue()