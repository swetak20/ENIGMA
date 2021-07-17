#THREE PARTS OF ENIGMA:
#PlugBoard
#Rotors
#Refelctor

'''
    PlugBoard - This part of the machine added the most number of combinations. 
    We have 10 of these wires. And each of these wires connect two letters into a 
    pair. Two letters in a pair will swap over.
'''

class Plugboard:
    def __init__(self) -> None:
        pass
    def caesar_cipher(self,ch):  
        if(ch == "A"):    #1
            ch = "F"
        if(ch == "F"):
            ch = "A"
        if(ch == "M"):    #2
            ch = "N"
        if(ch == "N"):
            ch = "M"
        if(ch == "O"):    #3
            ch = "T"
        if(ch == "T"):
            ch = "O"
        if(ch == "L"):    #4
            ch = "K"
        if(ch == "K"):
            ch = "L"
        if(ch == "R"):    #5
            ch = "Z"
        if(ch == "Z"):
            ch = "R"
        if(ch == "Q"):    #6
            ch = "W"
        if(ch == "W"):
            ch = "Q"
        if(ch == "I"):    #7
            ch = "C"
        if(ch == "C"):
            ch = "I"
        if(ch == "J"):    #8
            ch = "X"
        if(ch == "X"):
            ch = "J"
        if(ch == "D"):    #9
            ch = "V"
        if(ch == "V"):
            ch = "D"
        if(ch == "Y"):    #10
            ch = "E"
        if(ch == "E"):
            ch = "Y"
        
        return ch

class Reflector:
    def __init__(self):
        pass

'''
    Fast rotor, Medium rotor, Slow rotor - Each of these rotos act like clock, 
    where the faster rotor is seconds hand, the medium rotor is minutes hand and 
    slow rotor is the hour hands.
'''

'''
    Each rotor has a rate which is after how many turns of previous rotor, the current rotor takes a turn.
    Key refers to the state at which the rotors were initally, the initial keys are important for decrypting
    the messages, while the current key(curr) keeps the count and rorates the rotor once it becomes equal
    to a multiple of the rate of the current rotor.
'''

class Rotor:
    def __init__(self, rate, key, curr):
        self.rate = rate
        self.key = key
        self.curr = curr

class Setup:
    def __init__(self, rotor1 : Rotor, rotor2 : Rotor ,rotor3 : Rotor ,plugboard : Plugboard ,reflector : Reflector) :
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        self.reflector = reflector

    def update (self, inp):
       
        # self.rotor1.key += 1
        # self.rotor1.key %= 26
        inp = chr(ord(inp) + 1)
        self.rotor1.curr += 1


        if(self.rotor2.curr % self.rotor2.rate == 0):            
            # self.rotor2.key += 1
            # self.rotor2.key %= 26
            inp = chr(ord(inp) + 1)
        self.rotor2.curr += 1
        


        if(self.rotor3.curr % self.rotor3.rate == 0):             
            # self.rotor3.key += 1
            # self.rotor3.key %= 26
            inp = chr(ord(inp) + 1)
        self.rotor3.curr += 1
        
        
        # Reflector


    
        if(self.rotor3.curr % self.rotor3.rate == 0):              
            # self.rotor3.key += 1
            # self.rotor3.key %= 26
            inp = chr(ord(inp) + 1)
        self.rotor3.curr += 1
        


        if(self.rotor2.curr % self.rotor2.rate == 0):              
            # self.rotor2.key += 1
            # self.rotor2.key %= 26
            inp = chr(ord(inp) + 1)
        self.rotor2.curr += 1
        
        


        # self.rotor1.key += 1
        # self.rotor1.key %= 26
        inp = chr(ord(inp) + 1)
        self.rotor1.curr += 1
    
        return inp


    
class Enigma:
    def __init__(self, setup : Setup) -> None:
        self.setup = setup


    def cipher(self, inp):
        inp = self.setup.plugboard.caesar_cipher(inp)
        inp = self.setup.update(inp)
        inp = self.setup.plugboard.caesar_cipher(inp)

        return inp


    




#main



rotor1 = Rotor(1,0,0)
rotor2 = Rotor(3,5,5)
rotor3 = Rotor(5,3,3)
 
plugboard = Plugboard()

reflector = Reflector()

setup = Setup(rotor1, rotor2, rotor3, plugboard, reflector)

enigma = Enigma(setup)



text =  input("Enter message:") 

for i in range(len(text)):
    print(enigma.cipher(text[i]))

