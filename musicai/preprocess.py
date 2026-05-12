import os
import glob
import pickle
from music21 import converter, instrument, note, chord

def get_notes(file_path):
    notes = []
    midi = converter.parse(file_path)

    try:
        parts = instrument.partitionByInstrument(midi)
        notes_to_parse = parts.parts[0].recurse()
    except:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append(".".join(str(n) for n in element.normalOrder))

    return notes


def preprocess():
    all_notes = []
    files = glob.glob("dataset/*.mid")

    print(f"Found {len(files)} MIDI files")

    for i, file in enumerate(files):
        print(f"Processing {i+1}/{len(files)}: {file}")
        try:
            notes = get_notes(file)
            all_notes.extend(notes)
        except Exception as e:
            print(f"Skipping {file}: {e}")

    print(f"\nTotal notes extracted: {len(all_notes)}")
    print(f"Unique notes: {len(set(all_notes))}")

    with open("notes.pkl", "wb") as f:
        pickle.dump(all_notes, f)

    print("Saved to notes.pkl ✅")

preprocess()