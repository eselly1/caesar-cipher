
print('welcome to the caesar cipher')
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encode_or_decode= input('type "encode" to encode a message, or type "decode" to decode a message: ').lower()
while encode_or_decode != 'encode' and encode_or_decode != 'decode':
    encode_or_decode= input('type "encode" to encode a message, or type "decode" to decode a message: ').lower()

message=input('type your message: ')

shift=int(input('how many letters do you want to shift it by?: '))

def encode():
    code=''
    for i in range(0,len(message)):
        for j in range(0,len(alphabet)):
            if message[i] == alphabet[j]:
                if j+shift>= len(alphabet)-1:
                    t=((j+shift)-(len(alphabet)-1))-1
                    y=alphabet[t]
                else:    
                    y=alphabet[j+shift]
                code += y
    print(code)

def decode():
    ans=''
    for i in range(0,len(message)):
        for j in range(0,len(alphabet)):
            if message[i] == alphabet[j]:
                # if j-shift<= len(alphabet)-1:
                #     t=(j+shift)-(len(alphabet)-1)
                #     y=alphabet[t]
                # else:    
                #     y=alphabet[j+shift]
                y=alphabet[j-shift]
                ans += y
    print(ans)

if encode_or_decode == "encode":
    encode()
else:
    decode()
               
goagain=input('Do you want input another message?: ').lower()
while goagain == "yes" or goagain == "y":
    encode_or_decode= input('type "encode" to encode a message, or type "decode" to decode a message: ').lower()
    while encode_or_decode != 'encode' and encode_or_decode != 'decode':
        encode_or_decode= input('type "encode" to encode a message, or type "decode" to decode a message: ').lower()
    message=input('type your message: ').lower()
    shift=int(input('how many letters do you want to shift it by?: '))
    if encode_or_decode=='encode':
        encode()
    else:
        decode()
    goagain = input("Do you want to input another message?: ").lower()

print("Thanks for using the caesar cypher")





