#THREE PARTS OF ENIGMA:
#PlugBoard
#Rotors
#Storing 

'''PlugBoard - This part of the machine added the most number of combinations. 
We have 10 of these wires. And each of these wires connect two letters into a 
pair. Two letters in a pair will swap over.'''

def caesar_cipher(char):  
    if(char == "A"):    #1
        char = "F"
    if(char == "F"):
        char = "A"
    if(char == "M"):    #2
        char = "N"
    if(char == "N"):
        char = "M"
    if(char == "O"):    #3
        char = "T"
    if(char == "T"):
        char = "O"
    if(char == "L"):    #4
        char = "K"
    if(char == "K"):
        char = "L"
    if(char == "R"):    #5
        char = "Z"
    if(char == "Z"):
        char = "R"
    if(char == "Q"):    #6
        char = "W"
    if(char == "W"):
        char = "Q"
    if(char == "I"):    #7
        char = "C"
    if(char == "C"):
        char = "I"
    if(char == "J"):    #8
        char = "X"
    if(char == "X"):
        char = "J"
    if(char == "D"):    #9
        char = "V"
    if(char == "V"):
        char = "D"
    if(char == "Y"):    #10
        char = "E"
    if(char == "E"):
        char = "Y"
    
    return char 


  
 

'''Fast rotor, Medium rotor, Slow rotor - Each of these rotos act like clock, 
where the faster rotor is seconds hand, the medium rotor is minutes hand and 
slow rotor is the hour hands.'''


'''Each rotor has a rate which is after how many turns of previous rotor, the current rotor takes a turn.
    Key refers to the state at which the rotors were initally, the initial keys are important for decrypting
    the messages, while the current key(curr) keeps the count and rorates the rotor once it becomes equal
    to a multiple of the rate of the current rotor.
'''
class Rotor:
    def __init__(self, rate, key, curr):
        self.rate = rate
        self.key = key
        self.curr = curr


class Update_rotor:
    def __init__(self, rotor1 : Rotor, rotor2 : Rotor, rotor3 : Rotor, inp) :
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.inp = inp
    
    def update(self):
       
        # self.rotor1.key += 1
        # self.rotor1.key %= 26
        self.inp = chr(ord(self.inp) + 1)
        self.rotor1.curr += 1


        


        if(self.rotor2.curr % self.rotor2.rate == 0):            
            # self.rotor2.key += 1
            # self.rotor2.key %= 26
            self.inp = chr(ord(self.inp) + 1)
        self.rotor2.curr += 1
        


        if(self.rotor3.curr % self.rotor3.rate == 0):             
            # self.rotor3.key += 1
            # self.rotor3.key %= 26
            self.inp = chr(ord(self.inp) + 1)
        self.rotor3.curr += 1
        

    
        if(self.rotor3.curr % self.rotor3.rate == 0):              
            # self.rotor3.key += 1
            # self.rotor3.key %= 26
            self.inp = chr(ord(self.inp) + 1)
        self.rotor3.curr += 1
        


        if(self.rotor2.curr % self.rotor2.rate == 0):              
            # self.rotor2.key += 1
            # self.rotor2.key %= 26
            self.inp = chr(ord(self.inp) + 1)
        self.rotor2.curr += 1
        


        # self.rotor1.key += 1
        # self.rotor1.key %= 26
        self.rotor1.curr += 1
    
        return chr(ord(self.inp) + 1)




#main

rotor1 = Rotor(1, 0, 0)
rotor2 = Rotor(3, 4, 4)
rotor3 = Rotor(5, 17,17)




enigma = []
rev = []
cont = 'y'

while(cont == 'y'):

    text =  input("Enter message:") 

    for i in range(len(text)):
     
        cipher_char = caesar_cipher(text[i]) 
        set = Update_rotor(rotor1, rotor2, rotor3, cipher_char)
        output = set.update()
        enigma.append(caesar_cipher(output))
    print(*enigma)


    cont = input("Do you want to continue[y/n]:")
