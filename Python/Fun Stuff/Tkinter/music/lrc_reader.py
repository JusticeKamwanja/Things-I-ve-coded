'''I already know what I'm looking for, so lets just start.'''
import time
import sys


def type(text, typing_speed):
    # Print tne text.
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed) # Controls how fast the letters appear.

def sing(lyrics, continuous_lyrics, is_new_line=True): # Unless specified, the typing speed will be 0.08 sec.
    '''Types text character by character.'''
    lines_printed = 1

    intro = '--------SONG LYRICS--------\n\n'
    intro +="Press 'Enter' to start. \n"
    
    input(intro)
    
 
    for line in lyrics:
        if len(line) > 1:
            is_new_line = line[-1] if bool(line[-1]) == 'False' else True
        current_line = lyrics.index(line) + 1
        
        # If the index of the line is an argument in the function. (if it is to be continuous) then index[0] will be a the index carrying the lyrics.
        if current_line in continuous_lyrics:
            is_new_line = False
        else:
            is_new_line =True
            
        text = line[0]
        typing_speed = 0.08 or float(line[1])
        wait_for_next_line = 0.5 or float(line[2])
            
        # 2. Print the text in lyrics data in one line
        if is_new_line:
            type(text, typing_speed)
            print() # Continue the lyrics on anew line.
        else:
            type(text, typing_speed)
            
    
        lines_printed += 1
        time.sleep(wait_for_next_line) # 3. Wait before typing the next line.
        
        
lyrics = [
    # ['Wanasemaga mapenzi safari', 0.08, 0.3],
    # ['Unavyopipta ndo jinsi unajongea', 0.07, 0.6],
    # ['Ila niendapo ni mbali sijui ka ntafika sababu natembea', 0.07, 0.8],
    # ['Niliposikiaga habari, ', 0.08, 0.05],
    # ['yakisifika nkakesha nangojea', 0.07, 0.6, 'False'],
    # ['Akabariki Jalali, ', 0.07, 0.805,],
    # [ 'na nikawika mziki nkauotea', 0.08, 0.6, 'False'],
    # ['Ile pruu mpaka Macca',],
    # ['Nikadandiaga Bongo movie',],
    ['Kumbe mapenzi hayataki haraka',],
    ['Ni kama tango natia tu chumyi',],
    ['Mwenzenu nikaoza haswa',],
    ['Na kujitia kitandani mjuzi',],
    ['Eti nataka fukuza paka', 0.08, 0.05],
    ['Badala ya mbwa ', 0.08, 0.05],
    ['nkafuga mbuzi ',  0.08, 0.05, 'False'],
    ['mmmh', 0.08, 0.03,  'False'],
    ['Wivu ukanifanya nkagombana ', 0.08, 0.03],
    ['na marafiki', 0.08, 0.3,  'False'],
    ['Ugomvi na mamangu, ',  0.07, 0.01],
    ['akiniambia siambiliki',  0.07, 0.01,  'False'],
]

continuous_lyrics = [lyrics.index(i) for i in lyrics if len(i) > 1 and i[-1] == 'False']

sing(lyrics, continuous_lyrics)