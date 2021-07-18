'''
Parts construction
'''

'''
rotor1 = I (wirirng config : EKMFLGDQVZNTOWYHXUSPAIBRCJ; UWYGADFPVZBECKMTHXSLRINQOJ)
rotor2 = II (wiring config : AJDKSIRUXBLHWTMCQGZNPYFVOE; AJPCZWRLFBDKOTYUQGENHXMIVS)
rotor3 = III (wiring config : BDFHJLCPRTXVZNYEIWGAKMUSQO; TAGBPCSDQEUFVNZHYIXJWLRKOM)
'''

'''
notches:
rotor1 : Q
rotor2 : E
rotor3 : V
'''

'''
initial_key = ['K','C','M']
is a list of the starting character for each rotor
 *      as positioned on the spindle, where the nth character of
 *      [key] is the starting character for the nth rotor in
 *      [rotors].
'''

'''
reflector = B (wiring config :YRUHQSLDPXNGOKMIEBFZCWVJAT)
'''

ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    

class Rotor:
    def __init__(self, notch, key, fwiring, bwriring):
        self.notch = notch
        self.key = key
        self.fwiring = fwiring
        self.bwiring = bwriring



class Reflector:
    
    def __init__(self):
        
        self.wiring = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D',
                       'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I',
                       'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U': 'C', 'V':'W', 'W':'V', 'X':'J',
                       'Y':'A', 'Z':'T'
                      }



class Plugboard:

    def __init__(self) -> None:
        pass
    def caesar_cypher(self,ch):  
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

class Setup:
    def __init__(self, rotor1 : Rotor, rotor2 : Rotor ,rotor3 : Rotor ,plugboard : Plugboard ,reflector : Reflector) :
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        self.reflector = reflector

    def update (self, inp):

        #FORWARD

        # rotor1
        if(self.rotor1.key == self.rotor1.notch):
            key_index = ALPHABETS.index(self.rotor2.key)
            self.rotor2.key = ALPHABETS[(key_index + 1)%26]           #update the rotor2 key when key of rotor1 is equal to rotor1 notch

        key_index = ALPHABETS.index(self.rotor1.key)
        self.rotor1.key = ALPHABETS[(key_index + 1)%26]           #rotor1 key is always updated
    
        index = ALPHABETS.index(inp)
        key_index = ALPHABETS.index(self.rotor1.key)

        output_letter = self.rotor1.fwiring[(index +key_index )%26]
        print(f'input: {inp}, output {output_letter}')


#-----------------------------------------------------------------------------------------------------------------

        #rotor2
        if(self.rotor2.key == self.rotor2.notch):
            key_index = ALPHABETS.index(self.rotor3.key)
            self.rotor3.key = ALPHABETS[(key_index + 1)%26] 

        index = (ALPHABETS.index(output_letter) - key_index)%26
        key_index = ALPHABETS.index(self.rotor2.key)
 
        output_letter = self.rotor2.fwiring[(index + key_index )%26]
        print(f' output {output_letter}')
        
#-----------------------------------------------------------------------------------------------------------------

        #rotor3

        index = (ALPHABETS.index(output_letter) - key_index)%26
        key_index = ALPHABETS.index(self.rotor3.key)
        
        output_letter = self.rotor3.fwiring[(index + key_index )%26]
        print(f' output {output_letter}')
        print(self.rotor1.key, self.rotor2.key,self.rotor3.key)
#------------------------------------------------------------------------------------------------------------------

        #REFLECTOR
        print(output_letter)
        index = ALPHABETS.index(output_letter)
        ref_output = self.reflector.wiring[ALPHABETS[(index)%26]]
        print(ref_output)

#-------------------------------------------------------------------------------------------------------------------
        #BACKWARD

        #rotor3
        # if(self.rotor3.key == self.rotor3.notch):
        #     key_index = ALPHABETS.index(self.rotor2.key)
        #     self.rotor2.key = ALPHABETS[(key_index + 1)%26] 

        index = (ALPHABETS.index(ref_output) - key_index)%26
      
        output_letter = self.rotor3.bwiring[(index + key_index )%26]
        print(f' output {output_letter}')
#-----------------------------------------------------------------------------------------------------------------


        #rotor2
        if(self.rotor2.key == self.rotor2.notch):
            key_index = ALPHABETS.index(self.rotor3.key)
            self.rotor3.key = ALPHABETS[(key_index + 1)%26] 

        key_index = ALPHABETS.index(self.rotor2.key)
        index = (ALPHABETS.index(output_letter) - key_index)%26

        output_letter = self.rotor2.bwiring[(index +key_index )%26]
        print(f' output {output_letter}')
#----------------------------------------------------------------------------------------------------------------

        #rotor1
        key_index = ALPHABETS.index(self.rotor1.key)
        self.rotor1.key = ALPHABETS[(key_index + 1)%26]           #rotor1 key is always updated
        index = (ALPHABETS.index(output_letter) - key_index)%26
        key_index = ALPHABETS.index(self.rotor1.key)
        output_letter = self.rotor1.bwiring[(index +key_index )%26]
        
        print(f' output {output_letter}')
        print(self.rotor1.key, self.rotor2.key,self.rotor3.key)
#----------------------------------------------------------------------------------------------------------------
        
        return output_letter


class Enigma:
    def __init__(self, setup : Setup) -> None:
        self.setup = setup

    def cypher(self, inp):

        inp = self.setup.plugboard.caesar_cypher(inp)
        inp = self.setup.update(inp)
        inp = self.setup.plugboard.caesar_cypher(inp)

        return inp



'''main'''

rtr_f1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rtr_b1 = 'UWYGADFPVZBECKMTHXSLRINQOJ'

rtr_f2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rtr_b2 = 'AJPCZWRLFBDKOTYUQGENHXMIVS'

rtr_f3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
rtr_b3 = 'TAGBPCSDQEUFVNZHYIXJWLRKOM'

rotor1 = Rotor('Q', 'A', rtr_f1, rtr_b1)
rotor2 = Rotor('E', 'A', rtr_f2, rtr_b2)
rotor3 = Rotor('V', 'A', rtr_f3, rtr_b3)


plugboard = Plugboard()

reflector = Reflector()

setup = Setup(rotor1, rotor2, rotor3, plugboard, reflector)

enigma = Enigma(setup)

plain_text = input("Enter plain_text:")

cyphertext = []
for i in range(len(plain_text)):
    cyphertext.append(enigma.cypher(plain_text[i]))

print(cyphertext)
