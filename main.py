from music21 import note, stream

s = stream.Stream()
s.append(note.Note("C4", quarterLength=1))
s.append(note.Note("D4", quarterLength=1))
s.append(note.Note("E4", quarterLength=1))
s.append(note.Note("F4", quarterLength=1))

s.show("lily")
