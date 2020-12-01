from extractor import _Xkeysym


# keyBindings[] holds:
#   binding[] which hold:
#       mod key,
#       key pressed,
#       function to be called(args to function)

# click event mask button function argument


def extract_mouse(binding_list):
    for i in binding_list:
        print(i)


def extract_key(binding_list):
    for binding in binding_list:
        for position, element in enumerate(binding):
            if position == len(binding) - 1:
                print(element)
                continue
            if position == 0:
                for letter in element:
                    print(letter if letter != '|' else ' + ', end="")
                print(" + ", end="")
                continue
            if element in _Xkeysym.xkeysym:
                print(_Xkeysym.xkeysym[element] + " + -> ", end="")
                continue
            print(end=" ")
