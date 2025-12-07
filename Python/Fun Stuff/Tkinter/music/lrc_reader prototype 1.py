'''I already know what I'm looking for, so lets just start.'''
import time
import sys

def type_lyrics(text, typing_speed=0.08): # Unless specified, the typing speed will be 0.08 sec.
    '''Types text character by character.
    the "typing_speed" arg shows the sseconds to wait btwn each char.'''
    for char in text:
        print(char, end='')
        time.sleep(typing_speed)
        
    print()
        
lyrics = [
    ('I took so long'),
    ('I know believe me')
]
for lyric in lyrics:
    type_lyrics(lyric)