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
    print("modifier                     key        function        argument")
    for binding in binding_list:
        for i, element in enumerate(binding):
            if i < len(binding) - 1:
                if i == 0:
                    for letter in element:
                        print(letter if letter != '|' else ' + ', end="")
                    print(" +", end="")
                elif element in _Xkeysym.xkeysym:
                    print(_Xkeysym.xkeysym[element] + " + ->", end="")
                print(end=" ")
            else:
                print(element)
