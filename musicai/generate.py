import pickle
import random
import numpy as np
import torch
import torch.nn as nn
from music21 import instrument, note, chord, stream


SEQUENCE_LEN = 100
NUM_NOTES    = 300

class MusicLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MusicLSTM, self).__init__()
        self.lstm1 = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.lstm2 = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.fc1   = nn.Linear(hidden_size, 256)
        self.drop  = nn.Dropout(0.3)
        self.fc2   = nn.Linear(256, output_size)

    def forward(self, x):
        out, _ = self.lstm1(x)
        out, _ = self.lstm2(out)
        out     = out[:, -1, :]
        out     = self.fc1(out)
        out     = self.drop(out)
        out     = self.fc2(out)
        return out


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

with open("note_to_int.pkl", "rb") as f:
    note_to_int = pickle.load(f)

n_vocab    = len(set(notes))
int_to_note = {num: note for note, num in note_to_int.items()}

model = MusicLSTM(1, 512, n_vocab).to(device)
model.load_weights = model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

print(f"✅ Model loaded! Vocabulary size: {n_vocab}")


def generate_notes():
    start_idx = random.randint(0, len(notes) - SEQUENCE_LEN - 1)
    pattern = [note_to_int[n] for n in notes[start_idx:start_idx + SEQUENCE_LEN]]
    generated = []

    print(f"\n🎼 Generating {NUM_NOTES} notes...")

    for i in range(NUM_NOTES):
        x = np.array(pattern) / float(n_vocab)
        x = torch.tensor(x, dtype=torch.float32).unsqueeze(0).unsqueeze(-1).to(device)

        with torch.no_grad():
            output = model(x)

        probs = torch.softmax(output, dim=1).cpu().numpy()[0]
        index = np.random.choice(len(probs), p=probs)

        generated.append(int_to_note[index])
        pattern.append(index)
        pattern = pattern[1:]

        if (i + 1) % 50 == 0:
            print(f"   {i+1}/{NUM_NOTES} notes generated...")

    return generated


def notes_to_midi(generated_notes):
    output_notes = []
    offset = 0

    for pattern in generated_notes:
        if "." in pattern or pattern.isdigit():
            chord_notes = []
            for n in pattern.split("."):
                new_note = note.Note(int(n))
                new_note.storedInstrument = instrument.Piano()
                chord_notes.append(new_note)
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    midi_stream.write("midi", fp="generated_music.mid")
    print("\n🎵 Saved as generated_music.mid!")


# Run everything
generated = generate_notes()
notes_to_midi(generated)

