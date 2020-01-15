#Class Names
classNames = []
while True:
    print('Type class name: ' + str(len(classNames) + 1) +
        ' (Or enter nothing to stop.):')
    name = input()
    if name == "":
        break
    classNames = classNames + [name]
    print('The class names are:')
    for name in classNames:
        print('  ' + name)
