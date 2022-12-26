
sign = input("Signup or Login?")
if sign == 'signup':
    global l
    global p    
    l = input("Username: ")
    p = input("Password: ")
    print(l, "\n")
    print(p, "\n")
    file1 = open("login.txt", "w")
    file2 = open("login2.txt", "w")
    str1 = repr(l)
    str2 = repr(p)
    file1.write(str1)
    file2.write(str2)
    file1.close()
    file2.close()
elif sign == 'login':
    user = input("Username: ")
    psword = input("Password: ")
    ps = open('login.txt','r')
    ps2 = open('login2.txt','r')
    if user == ps and psword == ps2:
        print('Access granted')
    else:
        print("Wrong username or password.")