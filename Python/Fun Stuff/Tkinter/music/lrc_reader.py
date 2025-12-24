'''I already know what I'm looking for, so lets just start.'''
import time
import sys

class LRCReader:
    def type(text, typing_speed):
        # Print tne text.
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(typing_speed) # Controls how fast the letters appear.

    def sing(lyrics, is_new_line=True): # Unless specified, the typing speed will be 0.08 sec.
        '''Types text character by character.'''

        continuous_lyrics = [lyrics.index(i) for i in lyrics if len(i) > 1 and i[-1] == 'False']
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
            