import string
import hashlib
import secrets
import time

MINIMUM_PASSWORD_LENGTH = 14

passlength = 0
specialcharacters = "!@#$'%^\"&*()[]{}-_"

while passlength < MINIMUM_PASSWORD_LENGTH:			#setting of the password minimum length
    print("\n==========================================================================================================================================================")
    print("Insert the random password desired LENGTH (minimum 14 characters required!): ", end='')
    passlength = input()
    try:
        int(passlength)
    except Exception as e:
        exit(f'Uupsi..The value you gave me is not a number.\n[Error]: {e}')
    passlength = int(passlength)
    if passlength < MINIMUM_PASSWORD_LENGTH:
        print("Too short password!\n")

    try:
        amount = int(input('How many do you want generated?: '))
    except Exception as e:
        print(f'\nUupsi..The value you gave me is not a number.\n[Error]: {e}')
        quit()
    

start_time = time.time()
number=1

with open('pass.txt', 'w') as f1:
    for x in range(amount):
        source = string.ascii_letters + string.digits + specialcharacters
        password = ''.join(secrets.choice(source) for i in range(passlength))
        with open('passwords.txt', "r") as f2:				#opening of the common password cheat sheet
            lines = f2.read().splitlines()

        for line in lines:
                if  line.rstrip() in password:			        #checking if the password contains an easily guessable word of the cheat sheet
                    exit("Password found in the cheat sheet, please try again")
        
        print(number, file=f1, end='')
        print(") Here the random password generated: ", file=f1,  end ='')
        print(password, file=f1)
        print("%d) Here is your newly generated random password: %s" % (number, password))
        
        encodedpwd = password.encode('utf-8')			    #password encoding
        hash = hashlib.sha512(encodedpwd).hexdigest()		#password hashing with SHA-512 algorithm

        print("\n   We can also hash the Password just for information purposes")
        print("   Random Password hash:", hash)
        
        print("   Here the hashing form: ", file=f1, end ='')
        print(hash, file=f1)

        print("\n==========================================================================================================================================================\n")
        number+=1

print("---EXECUTION TIME %s seconds ---\n" % (time.time() - start_time))











