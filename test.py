my_dict = {
'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110', 'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100', 'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010', 's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000', 'y': '01111001', 'z': '01111010', 'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110', 'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100', 'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010', 'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000', 'Y': '01011001', 'Z': '01011010'}


# a = '1234567890'
# for i in range(0,len(a),8):
#     print(a[i:i+8])

def encoder():
    try:
        string = input("Enter a string: ")
        output = ""
        for char in string:
            if char == " ":
                output += " "
            elif char in my_dict:
                output += my_dict[char]
        print(output)
    except Exception as e:
        return f"error: {e}"

try1 = '01101011011100100110100101110011011010000110111001100001'
# try2 = 01101011 01110010 01101001 01110011 01101000 01101110 01100001

def decoder():
    try:
        string = input("Enter a code: ")
        output = ""
        value:str
        # value.replace(" ","")
        
        for i in range(0, len(string),8):
            
            value = string[i:i+8]
            value.replace(" ","")
            
            for key in my_dict:
                # value.replace(" ","")
                if my_dict[key] == value:
                    output += key
        print(output)
    except Exception as e:
        return f"error: {e}"

# encoder()
decoder()


def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    binary_values = binary_str.split()
    return ''.join(chr(int(b, 2)) for b in binary_values)

# # Convert text to binary
# # text = input("Enter a string: ")
# binary = text_to_binary(text)
# print(binary)

# # Convert binary back to text
# binary_input = input("Enter a string: ")
# text_output = binary_to_text(binary_input)
# print(text_output)
