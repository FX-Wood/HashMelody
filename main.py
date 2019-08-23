from musical.theory import Note, Scale, Chord
from musical.audio import playback
from timeline import Hit, Timeline

import os

import hashlib

# open a file, or input some text
textInput = input('please input some text: ')
print('textInput:', textInput)

# encode in a bytearray
textBytes = textInput.encode()
print('textBytes', textBytes)

# hash the text
textHash = hashlib.md5()
textHash.update(textBytes)
digest = textHash.digest()
print('digest:', digest)

# convert bytes to integers
integers = [n for n in digest]
print(integers)
for char in digest:
    print(char)


# play the notes
time = 0.0
timeline = Timeline()

for pitch in integers:
    print(pitch)
    timeline.add(time, Hit(Note(pitch % 32 + 24), 0.6))
    time += 0.6


data = timeline.render()

playback.play(data)