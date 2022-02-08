class CipherCesar:
    esp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    eng = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    dict_cesar = {}
    encoder = []
    decoder = []
    LANGUAGE = eng
    ROT = 3
    letter_to_number = []
    key_number = 0

    def __init__(self):
        for x in range(len(self.LANGUAGE)):
            if self.LANGUAGE == self.esp:
                x = (x+self.ROT) % 27
                self.letter_to_number.append(x)
            elif self.LANGUAGE == self.eng:
                x = (x+self.ROT) % 25
                self.letter_to_number.append(x)

        for number_letter in self.letter_to_number:
            if self.LANGUAGE == self.esp:
                self.dict_cesar[self.esp[self.key_number]] = self.esp[number_letter]
            elif self.LANGUAGE == self.eng:
                self.dict_cesar[self.eng[self.key_number]] = self.eng[number_letter]
            self.key_number += 1

    def encoder_text(self,text):
        print(text)
        for letter_encode in text.upper():   
            for k,v in self.dict_cesar.items():
                if letter_encode == k:
                    self.encoder.append(v)
                elif letter_encode == " ":
                    self.encoder.append(" ")
                    break
        return self.encoder

    def decode_text(self, text):
        self.text = text
        for letter_decoder in self.encoder:   
            for k,v in self.dict_cesar.items():
                if letter_decoder == v:
                    self.decoder.append(k)
                elif letter_decoder == " ":
                    self.decoder.append(" ")
                    break



c = CipherCesar()
print(*c.encoder_text("my dog"),sep='')