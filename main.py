from music21 import note, stream, layout, meter, key, tempo, environment

def create_g_major_scale_three_octaves(start_pitch='G4', octaves=3):
    """
    Creates a musical score of the G Major scale spanning three octaves.
    If the scale exceeds the line or page width, it wraps to the next line.

    :param start_pitch: The starting pitch of the scale (default is 'G4')
    :param octaves: Number of octaves to span (default is 3)
    :return: music21.stream.Score object
    """
    # Create a Score object
    s = stream.Score()

    # Set up the key signature for G Major (1 sharp)
    key_sig = key.KeySignature(1)  # G Major has one sharp
    s.insert(0, key_sig)

    # Set up the time signature (e.g., 4/4)
    ts = meter.TimeSignature('4/4')
    s.insert(0, ts)

    # Optional: Add a tempo marking
    tempo_mark = tempo.MetronomeMark(number=120)
    s.insert(0, tempo_mark)

    # Create a Part (instrument)
    p = stream.Part()
    p.insert(0, key_sig)
    p.insert(0, ts)
    p.insert(0, tempo_mark)

    # Define the G Major scale over the specified number of octaves
    scale_pitches = []
    current_pitch = note.Note(start_pitch)
    for _ in range(octaves):
        # Add ascending scale
        scale = current_pitch.getScale('major')
        for p_pitch in scale.getPitches(current_pitch.pitch, current_pitch.pitch.transpose('P8')):
            scale_pitches.append(p_pitch.nameWithOctave)
        # Move to the next octave
        current_pitch = current_pitch.transpose('P8')

    # Organize notes into measures
    measure_number = 1
    current_measure = stream.Measure(number=measure_number)
    for i, pitch in enumerate(scale_pitches):
        n = note.Note(pitch, quarterLength=1)  # Each note is a quarter note
        current_measure.append(n)
        # After filling the measure (4 quarter notes), add it to the part
        if (i + 1) % 4 == 0:
            p.append(current_measure)
            measure_number += 1
            current_measure = stream.Measure(number=measure_number)
    
    # Append any remaining notes in the last measure
    if len(current_measure.notes) > 0:
        p.append(current_measure)

    # Add the Part to the Score
    s.append(p)

    # Configure standard page layout
    page_layout = layout.PageLayout(
        pageWidth=595,      # A4 width in points (approx.)
        pageHeight=842,     # A4 height in points (approx.)
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=50
    )
    s.insert(0, page_layout)

    # Optional: Configure system layout for better control
    system_layout = layout.SystemLayout(
        systemMargins=(20, 20, 20, 20),
        systemDistance=100
    )
    s.insert(0, system_layout)

    return s

if __name__ == "__main__":
    # Create the score
    score = create_g_major_scale_three_octaves(start_pitch='G4', octaves=3)

    # Optional: Specify the path to LilyPond if it's not in the system PATH
    # env = environment.UserSettings()
    # env['lilypondPath'] = '/path/to/lilypond'

    # Show the score as a PDF using LilyPond
    # This will generate a PDF and open it using the default PDF viewer
    score.show('lily.pdf')

    # Alternatively, to write the LilyPond file without opening it:
    # score.write('lily.pdf', fp='g_major_scale_three_octaves.pdf')
    print("G Major scale over three octaves has been generated and saved as 'g_major_scale_three_octaves.pdf'.")
