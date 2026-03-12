import sys
from datetime import datetime
import re

#error checking if user doesnt provide command line argument (log file)
if len(sys.argv) < 2:
    print('Please provide a file name')
    sys.exit()

filename = sys.argv[1]

while True:
    message = input()
    time = datetime.now()
    format_time = time.strftime("%Y-%m-%d %H:%M ")
    
    #seperate action from message
    tokenized_message = re.split(r'(\s+)', message)
    action = tokenized_message[0]
    tokenized_message.remove(action)
    message = "".join(tokenized_message)

    if action.lower() == 'quit':
        sys.exit()

    #open in append mode
    with open(filename, 'a') as file:
        file.write(format_time + '[' + action + ']'+ message + '\n')
     








    
