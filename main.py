from music21 import note, stream, layout

# Create a music stream
s = stream.Stream()

# Add notes
s.append(note.Note("C4", quarterLength=1))
s.append(note.Note("D4", quarterLength=1))
s.append(note.Note("E4", quarterLength=1))
s.append(note.Note("F4", quarterLength=1))

# Configure an extremely large layout
# The staffSize is huge, and the page size is gigantic to prevent shrinking.
page_layout = layout.PageLayout(
    staffSize=640,      # 8x the original already large size.
    pageWidth=2000,     # Very large page width in points
    pageHeight=2000,    # Very large page height in points
    lineWidth=1800      # Large line width so LilyPond doesn't wrap or shrink
)

system_layout = layout.SystemLayout(
    systemMargins=(400, 400, 400, 400),  # Very large margins
    systemDistance=1600                  # Very large system distance
)

# Insert layout configurations
s.insert(0, page_layout)
s.insert(0, system_layout)

# Write the score to a LilyPond (.ly) file
lilypond_filename = "score.ly"
s.write("lilypond", lilypond_filename)

print(f"LilyPond file has been saved as {lilypond_filename}")
