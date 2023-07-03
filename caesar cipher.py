# Data import
from data import logo
from data import alphabet
print(logo)

# RUN flag(restarts program if necessary)
restart_flag=True


while restart_flag:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction=='encode' or 'decode':
        print('Option Not Found')
        restart=False
        
# Cipher Function
    def caesar(text_input,shift_num,direction):
        result=''
        for char in text:
            if char not in alphabet:
                result+=str(char)
            
            elif direction=='encode':
                position=alphabet.index(char)+(shift_num)       
                
                if position+1>len(alphabet):
                    position=position%len(alphabet)
                    char=alphabet[position]
                    result+=char        
                
                else:
                    char=alphabet[position]
                    result+=char        
            
            elif direction=='decode':    
                position=alphabet.index(char)-(shift_num)             
                char=alphabet[position]
                result+=char
        
        return result
#Main program:
    while restart_flag:
        #ENCODE
        if direction=='encode':
          text = input("Type your message:\n").lower()
          #User error check
          try:
              shift = int(input("Type the shift number:\n"))
          except:
              print("That's not a number")
              restart_flag==False
          print(f'The encoded message is {caesar(text,shift,direction)}')

        # Decode
        elif direction=='decode':
          text = input("Type your message:\n").lower()
          shift = int(input("Type the shift number:\n"))
          print(f'The decoded message is {caesar(text,shift,direction)}')
        
        restart=input("\nType in 'Restart' for more options or 'end' to exit.").lower()
        if restart=='restart':
            print("Will do ;)")
            direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            
        elif restart=='end':
            restart_flag=False
            
        else:
            print("not an option")
            restart_flag=False            
restart=input("\nType in 'Restart' for more options or 'end' to exit.").lower()
if restart=='restart':
    print("Will do ;)")
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction=='decode'or'encode':
        restart_flag==True
          
      
