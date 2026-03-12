import sys
from subprocess import Popen, PIPE

history = []

def is_valid_input(text):
    #check if input contains only letters
    if not text.isalpha():
        print("ERROR Input must contain only letters.")
        return False
    return True

def print_history():
    #print history with an index to choose the string
    for i in range (len(history)):
        print(f"{i+1} {history[i]}")
            
def main():
    #error checking if user doesnt provide command line argument (log file)
    if len(sys.argv) < 2:
        print('Please provide a file name')
        sys.exit()

    #set command line argument to the log file
    filename = sys.argv[1]

    #open up pipes for logger and encrypter
    log_process = Popen(['python3', 'logger.py', filename], stdin=PIPE, encoding='utf8')
    encrypt_process = Popen(['python3', 'encrypter.py'], stdin=PIPE, stdout=PIPE, encoding='utf8')

    #log that the driver has started
    log_process.stdin.write("START Logging Started.\n")
    log_process.stdin.flush()

    while True:
        #display menu
        print('-'.center(80, '-'))
        print('MENU'.center(80, ' '))
        print('-'.center(80, '-'))
        print('\n\tpassword - set the password for encryption/decryption\n\tencrypt - encrypt a string\n\tdecrypt - decrypt a string\n\thistory - show history\n\tquit - quit program\n')
        print('-'.center(80, '-'))
        command = input('Enter Command: ').strip().lower()

        #handle menu options
        if command == "quit":
            #log that the driver has ended 
            log_process.stdin.write("STOPPED Logging Stopped.\n")
            log_process.stdin.flush()

            #stop logger program
            log_process.stdin.write("QUIT\n")
            log_process.stdin.flush()

            #stop encrypter program
            encrypt_process.stdin.write("QUIT\n")
            encrypt_process.stdin.flush()

            #exit while loop and program
            break
        elif command == "password":
            text = input("Would you like to use history? Y or N: ")

            if (text.upper() == "Y" and history):
                print_history()
                choice = input("Choose string:")

                #send command with history at chosen index
                i = int(choice)
                encrypt_process.stdin.write(f"PASSKEY {history[i-1].upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()
            else:
                #otherwise send command with user chosen string
                passkey = input("Enter new passkey: ")
                if not is_valid_input(passkey):
                    continue
                encrypt_process.stdin.write(f"PASSKEY {passkey.upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()

            #log only that passkey was set or not set
            print("Passkey set.")
        elif command == "encrypt":
            #prompt to use history
            text = input("Would you like to use history? Y or N: ")

            if (text.upper() == "Y" and history):
                print_history()
                choice = input("Choose string to encrypt:")

                #send command with history at chosen index
                i = int(choice)
                encrypt_process.stdin.write(f"ENCRYPT {history[i-1].upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()
                print(result)

                log_process.stdin.write(f"ENCRYPT {history[i-1]}\n")
                log_process.stdin.flush()
            else:
                #otherwise send command with user chosen string
                text = input("Enter text to encrypt: ")
                if not is_valid_input(text):
                    continue
                history.append(text.upper())
                encrypt_process.stdin.write(f"ENCRYPT {text.upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()
                print(result)

                #save result to history (strip RESULT prefix)
                if result.startswith("RESULT "):
                    history.append(result[7:])

                log_process.stdin.write(f"ENCRYPT {text.upper()}\n")
                log_process.stdin.flush()
            log_process.stdin.write(f"RESPONSE {result}\n")
            log_process.stdin.flush()
        elif command == "decrypt":
            #prompt to use history
            text = input("Would you like to use history? Y or N: ")
            if (text.upper() == "Y" and history):
                print_history()
                choice = input("Choose string to DECRYPT:")

                #send command with history at chosen index
                i = int(choice)
                encrypt_process.stdin.write(f"DECRYPT {history[i-1].upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()
                print(result)

                log_process.stdin.write(f"DECRYPT {history[i-1]}\n")
                log_process.stdin.flush()
            else:
                #otherwise send command with user chosen string
                text = input("Enter text to decrypt: ")
                if not is_valid_input(text):
                    continue
                history.append(text.upper())
                encrypt_process.stdin.write(f"DECRYPT {text.upper()}\n")
                encrypt_process.stdin.flush()
                result = encrypt_process.stdout.readline().strip()
                print(result)

                #save result to history (strip RESULT prefix)
                if result.startswith("RESULT "):
                    history.append(result[7:])

                log_process.stdin.write(f"DECRYPT {text.upper()}\n")
                log_process.stdin.flush()
            log_process.stdin.write(f"RESPONSE {result}\n")
            log_process.stdin.flush()
        elif command == "history":
            log_process.stdin.write("HISTORY History Checked\n")
            log_process.stdin.flush()
            print_history()
            #wait for user input to exit history menu
            print("Press enter to go back:")
            exit = input()
            continue
        else:
            print("ERROR Unknown Command")
            continue
        
    #wait for processes
    log_process.wait()
    encrypt_process.wait()
    history.clear()
    return

if __name__ == "__main__":
    main()


