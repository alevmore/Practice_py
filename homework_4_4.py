def parse_input(user_input):               #function of command parcel        
    cmd, *args = user_input.split()     
    cmd = cmd.strip().lower()  
    return cmd, *args                             

def add_contact(args, contacts):        # function of adding of contacts
    name, phone = args                  
    contacts[name] = phone              #input argv to contacts  dict  with key name and value phone
    return "Contact added."             

def change_contact(args, contacts):     # function of contacts changing 
    name, phone = args
    for k in contacts.keys():          # cintacts iteration
        if k == name:                 # if key is name we give the name a new value (phone)
            contacts[name] = phone      
    return "Contact change"

def show_phone(args, contacts):         # function of presenting the phone by name
    name = args
    for key, value in contacts.items(): 
        if name == key:                 
            return value                
   
def show_all(contacts=None):       # fucntions return all contacts
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")  # entering the program
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:         # exit and stopping the program
            print("Good bye!")
            break 
        elif command == "hello":                 
            print("How can I help you?")
        elif command == "add":                   # adding the contact
            print(add_contact(args, contacts))
        elif command == "change":                # changing the contact
             print(change_contact(args, contacts))
        elif command == "phone":                 # show the phone by name
            print(show_phone(args, contacts))
        elif command in["all", "contacts"]:       # show all the contacts
            print(show_all(contacts)) 
        else:                                    
            print("Invalid command.")              # notification if the command is wrong

if __name__ == "__main__":
    main()
