import pickle
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


SEQUENCE_LEN = 100
BATCH_SIZE   = 64
EPOCHS       = 50
LEARNING_RATE = 0.001


# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Create mapping
unique_notes = sorted(set(notes))
n_vocab = len(unique_notes)
note_to_int = {note: num for num, note in enumerate(unique_notes)}
int_to_note = {num: note for note, num in note_to_int.items()}

# Save mappings for generate.py
with open("note_mappings.pkl", "wb") as f:
    pickle.dump((note_to_int, int_to_note), f)

print(f"Vocabulary size: {n_vocab}")
print(f"Total notes: {len(notes)}")

# Prepare sequences
inputs, outputs = [], []
for i in range(len(notes) - SEQUENCE_LEN):
    seq_in  = notes[i:i + SEQUENCE_LEN]
    seq_out = notes[i + SEQUENCE_LEN]
    inputs.append([note_to_int[n] for n in seq_in])
    outputs.append(note_to_int[seq_out])

X = torch.tensor(inputs, dtype=torch.float32) / n_vocab
y = torch.tensor(outputs, dtype=torch.long)

dataset = TensorDataset(X, y)
loader  = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

print(f"Training sequences: {len(inputs)}")

with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

unique_notes = sorted(set(notes))
n_vocab = len(unique_notes)

note_to_int = {note: num for num, note in enumerate(unique_notes)}
int_to_note = {num: note for note, num in note_to_int.items()}

with open("note_to_int.pkl", "wb") as f:
    pickle.dump(note_to_int, f)

print(f"Total notes: {len(notes)}")
print(f"Unique notes: {n_vocab}")


inputs = []
outputs = []

for i in range(len(notes) - SEQUENCE_LEN):
    seq_in = notes[i:i + SEQUENCE_LEN]
    seq_out = notes[i + SEQUENCE_LEN]
    inputs.append([note_to_int[n] for n in seq_in])
    outputs.append(note_to_int[seq_out])

X = np.array(inputs) / float(n_vocab)
X = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)
y = torch.tensor(outputs, dtype=torch.long)

dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

print(f"Training sequences: {len(inputs)}")


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
model = MusicLSTM(1, 512, n_vocab).to(device)
print(model)


criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

print("\n🚀 Training started...\n")

for epoch in range(EPOCHS):
    total_loss = 0

    for batch_X, batch_y in loader:
        batch_X = batch_X.to(device)
        batch_y = batch_y.to(device)
        optimizer.zero_grad()
        output = model(batch_X)
        loss = criterion(output, batch_y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(loader)
    print(f"Epoch {epoch+1}/{EPOCHS} — Loss: {avg_loss:.4f}")

torch.save(model.state_dict(), "model.pth")
print("\n✅ Model saved to model.pth")

