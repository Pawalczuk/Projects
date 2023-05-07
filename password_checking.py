password = input('Podaj hasło: ')

uppercase = False
lowercase = False
number = False
spaces = False
speacial = False


for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char.isspace():
        spaces = True
    elif char.isnumeric():
        number = True
    else:
        speacial = True


long = len(password) >= 8
check = long and uppercase and lowercase and number and speacial and not spaces


if check:
    print('Twoje hasło jest zgodne z wymogami') 
else:
    print('Twoje hasło jest mało bezpieczne, proszę się zastosować do poniższych reguł: ')
    if not long:
        print('-Twoje hasło zawiera mniej niż 8 znaków')
    if not uppercase:
        print('-Twoje hasło musi zawierać co najmniej 1 dużą literę!')
    if not lowercase:
        print('-Twoje hasło musi zawierać co najmniej 1 małą literę!')
    if not number:
        print('-Twoje hasło musi zawierać co najmniej 1 cyfrę!')
    if not speacial:
        print('-Twoje hasło musi zawierać co najmniej 1 znak specjalny')
    if spaces:
        print('-Twoje hasło nie może zawierać spacji')