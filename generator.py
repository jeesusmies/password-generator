import random
import json
import string
import sys
import os.path

passwordLengthConfirmed = False
chars = string.ascii_letters + string.digits + '!@#$%*'
digits = string.digits

print("TOTALLY NOT A RIPOFF FROM BYTE\nHello! Welcome to Ilhu's *REFINED* password generator.\nThis one includes a better interface, password storing and you can select if you want a really strong password, or a weak one!\n\nIf you want a STRONG password, type 1.\nIf you want a weak password, type 2.\nPlease note that weak passwords are more likely to be hacked.\n")

# Loops this loop until a number has been inputted.
# Same loop can be seen in every input, that requires a number.
while True:
    try:
        passwordChoice = int(input(">> "))
    except ValueError:
        print("Please type a number.")
    except:
        print("Something went wrong.. exiting.")
        sys.exit(0)
    else:
        break

# My stupid way to deal with adding the random numbers into an password.
# Turns a list into a string, as the name says.
def turn_list_into_string(list):
    result = ''
    for element in list:
        result += str(element)
    return result

# Here begins the generation of the strong password. Not very complex, atleast in my opinion.
if passwordChoice == 1:
    print("How lengthy of a password would you like? (suggested: 8)")

    while True:
        try:
            passwordLength = int(input(">> "))
        except ValueError:
            print("Please type a number.")
        except:
            print("Something went wrong.. exiting.")
            sys.exit(0)
        else:
            break

    # If password is shorter than 4, ask to confirm the decision, to reduce possible wasted time.
    if passwordLength < 4:
        print("This is a very short password.. Are you sure? (y/n)")
        if input(">> ").lower() == "y":
            print("Alright, continuing.")
        else:
            print("Okay, please enter your password length.")
            # Since user inputted 'n' (or something else) make the user be asked the password length, until the requirement has been achieved.
            while True:
                while True:
                    try:
                        passwordLength = int(input(">> "))
                    except ValueError:
                        print("Please type a number.")
                    except:
                        print("Something went wrong.. exiting.")
                        sys.exit(0)
                    else:
                        break
                notInputted = True
                if passwordLength < 4:
                    print("It's still too short. Enter a longer one.")
                else:
                    break

    print("Please type the service where you are going to use this password.")
    service = input(">> ")

    # Generate the strong password.
    password = ''.join(random.choice(chars) for i in range(passwordLength))
    print(f'This is your generated password: {password}\nIt has been also stored into a text file in this folder/directory.')

    with open('passwords.txt', 'a+') as file:
        file.write(f'Service: {service}\nPassword: {password}\n\n')
        file.close()

# Here begins the generation of the weak password. Although short, this might be a bit more complex for a beginner.
# (please forgive me if the comments are crap)
else:
    print("Alright, creating the weak password.")

    # PLEASE TAKE NOTE THAT THE WORDS USED IN THE WEAK PASSWORDS ARE COPY PASTED FROM A RANDOM WEBSITE AND MIGHT BE A LITTLE BIT BAD
    # Opens the 'words.json' file as a variable called 'wordFile', where all of the easy to remember words are.
    with open('words.json', 'r') as wordFile:
        words = json.load(wordFile)
        # Generates the weak password.
        password = random.choice(words) + turn_list_into_string([random.choice(digits) for i in range(4)])

        print("Please type the service where you are going to use this password.")
        service = input(">> ")

        print(f'This is your generated password: {password}\nIt has been also stored into a text file in this folder/directory.')

        with open('passwords.txt', 'a+') as file:
            file.write(f'Service: {service}\nPassword: {password}\n\n')
            file.close()
