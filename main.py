from music21 import note, stream, layout

# Create a music stream
s = stream.Stream()

# Add notes
s.append(note.Note("C4", quarterLength=1))
s.append(note.Note("D4", quarterLength=1))
s.append(note.Note("E4", quarterLength=1))
s.append(note.Note("F4", quarterLength=1))

# Configure the layout for larger staff and clearer notation
page_layout = layout.PageLayout(
    staffSize=80  # Increase staff size for larger notes
)

system_layout = layout.SystemLayout(
    systemMargins=(50, 50, 50, 50),  # Larger margins for centering on the page
    systemDistance=200               # Increased space between systems for clarity
)

# Insert layout configurations
s.insert(0, page_layout)
s.insert(0, system_layout)

# Output directly to a PDF using LilyPond
s.show("lily.pdf")
