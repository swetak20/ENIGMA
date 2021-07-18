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
initial_key = ['A','A','A']
is a list of the starting character for each rotor
 *      as positioned on the spindle, where the nth character of
 *      [key] is the starting character for the nth rotor in
 *      [rotors].
'''

'''
reflector = B (wiring config :YRUHQSLDPXNGOKMIEBFZCWVJAT)
'''



############################################################  SPECIFICATIONS  ###########################################################

ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    

WIRINGS = {
    'I': {'forward':'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
          'backward':'UWYGADFPVZBECKMTHXSLRINQOJ'},
    'II':{'forward':'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          'backward':'AJPCZWRLFBDKOTYUQGENHXMIVS'},
    'III':{'forward':'BDFHJLCPRTXVZNYEIWGAKMUSQO',
           'backward':'TAGBPCSDQEUFVNZHYIXJWLRKOM'},
    }
NOTCHES = {
    'I':'Q',
    'II':'E', 
    'III':'V'
    }


################################################################## COMPONENETS  ###########################################################


class Rotor:

    def __init__(self, rotor_num, window_letter, next_rotor = None, prev_rotor = None):
        self.rotor_num = rotor_num
        self.wiring = WIRINGS[rotor_num]
        self.notch = NOTCHES[rotor_num]
        self.window = window_letter
        self.offset = ALPHABETS.index(self.window)
        self.next_rotor = next_rotor
        self.prev_rotor = prev_rotor

    def step(self):
        
        if self.next_rotor and self.window==self.notch:
            self.next_rotor.step()
        self.offset = (self.offset + 1)%26
        self.window = ALPHABETS[self.offset]

    def encode_letter(self, index, forward=True):
    

        if forward:
            i = 'forward'
            output_letter = self.wiring[i][(index + self.offset)%26]
        else:
            i = 'backward'
            output_letter = self.wiring[i][(index + self.offset)%26]

        

        output_index = (ALPHABETS.index(output_letter) - self.offset)%26


        if self.next_rotor and forward:
            return self.next_rotor.encode_letter(output_index, forward)
        elif self.prev_rotor and not forward:
            return self.prev_rotor.encode_letter(output_index, forward = False)

        else:
            return output_index


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
        elif(ch == "F"):
            ch = "A"
        elif(ch == "M"):    #2
            ch = "N"
        elif(ch == "N"):
            ch = "M"
        elif(ch == "O"):    #3
            ch = "T"
        elif(ch == "T"):
            ch = "O"
        elif(ch == "L"):    #4
            ch = "K"
        elif(ch == "K"):
            ch = "L"
        elif(ch == "R"):    #5
            ch = "Z"
        elif(ch == "Z"):
            ch = "R"
        elif(ch == "Q"):    #6
            ch = "W"
        elif(ch == "W"):
            ch = "Q"
        elif(ch == "I"):    #7
            ch = "C"
        elif(ch == "C"):
            ch = "I"
        elif(ch == "J"):    #8
            ch = "X"
        elif(ch == "X"):
            ch = "J"
        elif(ch == "D"):    #9
            ch = "V"
        elif(ch == "V"):
            ch = "D"
        elif(ch == "Y"):    #10
            ch = "E"
        elif(ch == "E"):
            ch = "Y"
        
        return ch


####################################################################  SETUP  ########################################################################

class Wehrmacht_Enigma:
    def __init__(self, key='AAA', rotor_order=['I', 'II', 'III']):

        self.key = key
        self.rotor_order = rotor_order

        self.rotor3 = Rotor(rotor_order[2], key[2])
        self.rotor2 = Rotor(rotor_order[1], key[1], self.rotor3)
        self.rotor1 = Rotor(rotor_order[0], key[0], self.rotor2)
        self.reflector = Reflector()
        self.plugboard = Plugboard()
        self.rotor2.prev_rotor = self.rotor1
        self.rotor3.prev_rotor = self.rotor2


    def encrypt(self, inp):


        '''STEP 1 - PLUGBOARD  '''
        inp = self.plugboard.caesar_cypher(inp)

        '''STEP 2 - ROTATE ROTOR'''
        self.rotor1.step()
        
        '''STEP 3 - FORWARD PASS'''
        forward_index = self.rotor1.encode_letter(ALPHABETS.index(inp))

        '''STEP 4 - REFLECTOR'''
        refl_output = self.reflector.wiring[ALPHABETS[(forward_index)%26]]
       
        '''STEP 5 - BACKWARD PASS'''
        final_letter = ALPHABETS[self.rotor3.encode_letter(ALPHABETS.index(refl_output), forward=False)]

        '''STEP 6 - PLUGBOARD'''
        final_letter = self.plugboard.caesar_cypher(final_letter)

        return final_letter

    def decrypt(self, inp):

        self.encrypt(inp)
        
        



#######################################################  MAIN  ##########################################################################


enigma = Wehrmacht_Enigma()


plain_text = input("Enter plain_text [ONLY IN UPPERCASE]:")

cyphertext = ""
for i in range(len(plain_text)):

    if(plain_text[i] == " "):
        print(cyphertext, end= " ")
        cyphertext = ""
    else:
        cyphertext += (enigma.encrypt(plain_text[i]))

print(cyphertext)

