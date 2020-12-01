from extractor import _Xkeysym


# keyBindings[] holds:
#   binding[] which hold:
#       mod key,
#       key pressed,
#       function to be called(args to function)

# click event mask button function argument

def printTagKeys(element):
    element = list(element)
    strippedFunc = False
    gotKey = False
    key = []
    tag = 0
    while element:
        if not strippedFunc:
            if element[0] == '(':
                strippedFunc = True
            del element[0]
            continue
        if not gotKey:
            if element[0] == ',':
                gotKey = True
                del element[0]
                continue
            key.append(element[0])
            del element[0]
            continue
        tag = int(element[0])
        del element[0]
        del element[0]

    print(f"Key {_Xkeysym.xkeysym[''.join(key)]} corresponds to tag {tag}")


def extract_mouse(binding_list):
    for binding in binding_list:
        for position, element in enumerate(binding):
            if position == len(binding) - 1:
                print(element)
                continue
            if position == 0:
                print("Click on " + element + " with ", end="")
                continue
            if position == 1:
                if element == '0':
                    continue
                for letter in element:
                    print(letter if letter != '|' else ' + ', end="")
                print(" + ", end="")
                continue
            if "Button" in element:
                print(element + " -> ", end="")
                continue


def extract_key(binding_list):
    for binding in binding_list:
        for position, element in enumerate(binding):
            if position == 1 and "TAGKEYS" in element:
                printTagKeys(element)
                continue
            if position == len(binding) - 1:
                print(element)
                continue
            if position == 0:
                if element not in _Xkeysym.xkeysym:
                    for letter in element:
                        print(letter if letter != '|' else ' + ', end="")
                    print(" + ", end="")
                    continue
                continue
            if element in _Xkeysym.xkeysym:
                print(_Xkeysym.xkeysym[element] + " -> ", end="")
                continue

