#name: Dawood Imran ID: 100662594
from abc import ABC, abstractmethod


allorig = [] # holder for all decrypted messages
allenc = [] # holder for all encrypted messages

class Message(ABC): # Abstract base class
    """abstract base class message"""
    def __init__(self, message, opt, alphanm, key): # initializer method
        self.message = message # variables setting
        self.alphanm = alphanm
        self.key = key
        self.opt = opt

class plaintextMsg(Message): # plain text class used to encrypt
    def __init__(self, message, opt, alphanm, key): #
        super().__init__(message, opt, alphanm, key) # inherits from baseclass
        self.encrypted = []
    @property
    def msg(self):
        print(self.message)
    @msg.setter
    def msg(self, newmsg):
        self.message = newmsg

    def encrypt(self): # encrypts message
        if self.opt == 1: # if option is 1
            for char in self.message: # iterates through chars in word
                if char == " ": # if char is space adds space to keep original spacing
                    self.encrypted.append(" ") # adds space to list
                else: # else adds char to list
                    for keys, value in self.alphanm.items(): # iterates through keys and values in dictionary
                        if self.key[char] == value: # gets value of word in key dict
                            self.encrypted.append(keys) # adds word to list

            self.encrypted = ''.join(self.encrypted) # converts list to str

        elif self.opt == 2: # if option is 2
            for char in self.message: # iterates through chars in message
                if char == " ": # adds space if char = space to keep origianl spacing
                    self.encrypted.append(" ")  # saves spaces
                else: # else iterates through alphabet ldict
                    for k, v in self.alphanm.items():  # iterates through keys and values in dict
                        num = ((self.alphanm[char] + self.key) % 26)  # gets new num value for shifted char
                        if (num == v): # if new num = value adds key of new num to list
                            self.encrypted.append(k) #adds key to list

            self.encrypted = ''.join(self.encrypted) # converts to str

        elif self.opt == 3: # if option is 3
            self.message = self.message.split() # splits message
            for word in self.message: # iterates through words in message
                word = word[::self.key] # stores word backwards
                self.encrypted.append(word) # adds encrypted word to list
                self.encrypted.append(" ") # adds space between words for converting to str use
            self.encrypted = ''.join(self.encrypted) # converts back to str
        # print(self.encrypted)
        decrypter = ciphertextMsg(self.encrypted, self.opt, self.alphanm, self.key) # creates object to send encrypted message to decrypter
        decrypter.decrypt() # calls decrypt message
        decrypter.status()
    def __str__(self): # overlaods print function
        """overloads print operator for plaintxtmsg class"""
        return ("your encrypted message is: {}\n".format(self.encrypted)) # prints encrypted message
    def status(self): # polymorphic method displays current status of message
        print("current status of message = encrypting\n") # prints following



class ciphertextMsg(Message): # cipher text class to encrypt message
    """ciphertext class inherited from message class to encrypt message"""
    def __init__(self, message, opt, alphanm, key): # initializer for class
        super().__init__(message, opt, alphanm, key) # inherits attributes from superclass
        #self.message = message
        self.decrypted = [] # list for decrypted message
    def decrypt(self): # decryption method
        if self.opt == 1: # if options is 1

            for char in self.message: # iterates through chars in message
                if char == " ": # keeps spacing as original
                    self.decrypted.append(" ") # adds space to list
                else: # else iterates through keys adn values in in key dict
                    for keys, value in self.key.items():
                        if self.alphanm[char] == value: # if value match adds key of that value to list
                            self.decrypted.append(keys)
            self.decrypted = ''.join(self.decrypted) # converts to str


        elif self.opt == 2: # if option is 2

            for char in self.message:  # iterates through message
                if char == " ": # keeps original spacing
                    self.decrypted.append(" ")  # saves spaces
                else:
                    for k, v in self.alphanm.items():  # iterates through keys and values in dict
                        num = ((self.alphanm[char] - self.key) % 26)  # gets new num value for shifted char
                        if (num == v):
                            self.decrypted.append(k)
            self.decrypted = ''.join(self.decrypted)

        elif self.opt == 3: # if option is 3

            self.message2 = self.message.split() # split message for iterating through individual words
            for word in self.message2: # iterates through words in split message
                word = word[::-1] # iterates word backwords
                self.decrypted.append(word) # adds every decrypted word to decrypted list
                self.decrypted.append(" ") # adds space after every word for converting to string use
            self.decrypted = ''.join(self.decrypted) # joinswords to convert list to str
        #print(self.message)
        global allorig # global list
        global allenc # global list
        print("your original text was: ", self.decrypted) # prints original text for shift cipher
        allorig.append(self.decrypted) # stores decrypted message in list
        allenc.append(self.message) # stores encrypted message in list

    def status(self): # polymorphix method displays current status of message
        print("current status of message = decrypting\n") # prints following



def main(): # main function
    """main function prompts user for neccessary attributes required for classes before creating object of type class"""
    alphanum = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                "m": 12,"n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,  # contains alphabet numbered 0-25
                "y": 24, "z": 25}

    alphanumkey = {"l": 0,"b": 1,"f": 2,"d": 3,"a": 4,"t": 5,"r": 6,"n": 7,"w": 8,"x": 9,"e": 10,"m": 11,"h": 12,"k": 13,"p": 14, # contains shuffled alphabet numbered 0-25
            "s": 15,"y": 16,"o": 17,"u": 18,"j": 19,"g": 20,"c": 21,"v": 22,"z": 23, "i": 24, "q": 25}
    temp1 = False # temp1 = flase default

    while True: # runs while true
        try: # tries following
            while temp1 == False:
                temp2 = True # sets temp2 to true so option menu displays again after this
                option = 0 # resets opttion value everytime reruns
                msg = str(input("\nWhat message would you like to encrypt")) # message to be encrypted
                msg = msg.lower() # message converted to lowercase
                if msg.replace(" ","").isalpha() == False: # makes sure message is only alphabetical if not runs following
                    print("please enter a valid alphabetical string\n") # prints error message
                else: # else changes temp1 value to True so program continues
                    temp1 = True
        except: # catches any other errors adn prints following message
            print("please enter a valid alphabetical string")


        if msg == "stop": # breaks from while loop if user enters stop
            break


        while (option != 1 and option != 2 and option != 3 and option != 4): # only allows ints 1-3 to be entered else while loop repeats
            try: # tries following
                option = int(input("\n1. Substitution Cipher\n2. Caesar Cipher\n3. Transposition Cipher\n4. getter substitution method(extra for properties)\n")) # option menu
            except: # excepts any errors
                print("please enter a valid value")


        if option == 1: # if option 1 is selected applies substitution cipher
            key = alphanumkey # key for substitution cipher
            enc = plaintextMsg(msg, option, alphanum, key) # creates object with original message


        elif option == 2: # else if option is 2 applies caeser shift
            while temp2 == True: # runs while temp2 is true
                try: # tries following
                    key = int(input("\nwhat would you like the shift value ot be for the Caeser cipher\n")) # prompts for shift key
                    temp2 = False # changes temp2 value to false if no errors
                except: # handles any errors
                    print("please enter a valid value")
            enc = plaintextMsg(msg, option, alphanum, key) # creates object with original message

        elif option == 3: # else if opttion is 3 applies transposition cipher
            key = -1 # key is -1 to encrypt word
            enc = plaintextMsg(msg, option, alphanum,key) # creates object with original message
        elif option == 4: # extra option for properties uses substitution
            option = 1 # acts as substituion when passed to class
            key = alphanumkey  # key for substitution cipher
            enc = plaintextMsg(msg, option, alphanum, key) # creates object
            enc.msg = "random message" # setter sets new message

        enc.status() # prints current status
        enc.encrypt() # encrypt message
        print (enc) # prints encrypted message using overloaded method from plaintextmsg class
        temp1 = False # changes temp1 to false so repeats
    print("\n\n\n") # formatting
    for i in range (len(allorig)): # for loop to print encrypted adn decrypted messages
        print(i+1, "decrypted : {} | encrypted : {}".format(allorig[i], allenc[i]))
        i+=1 # numbering

main()