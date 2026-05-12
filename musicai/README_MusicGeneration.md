# 🎵 CodeAlpha — Music Generation with AI

An AI that composes original piano music using a deep LSTM neural network trained on classical MIDI files by Bach, Beethoven, Chopin, Debussy and more.

## ✨ Features
- 🧠 Deep LSTM neural network trained on classical piano music
- 🎹 Generates original music never heard before
- 💾 Saves output as a playable .mid file
- 🚀 GPU accelerated training with CUDA support
- 🎼 Trained on 41 MIDI files — Bach, Beethoven, Chopin, Debussy, Liszt and more

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| PyTorch | LSTM model training |
| music21 | MIDI parsing and generation |
| NumPy | Data processing |

## ⚙️ Installation
1. Clone the repository
2. Create virtual environment: `py -3.11 -m venv env`
3. Activate: `env\Scripts\activate`
4. Install: `pip install -r requirements.txt`

## 🚀 How to Run

### Step 1 — Add MIDI files
Place `.mid` files inside `dataset/` folder.

### Step 2 — Preprocess
```bash
python preprocess.py
```

### Step 3 — Train
```bash
python train.py
```

### Step 4 — Generate
```bash
python generate.py
```
Output saved as `generated_music.mid`

## 🎧 Listen
Open `generated_music.mid` with VLC, Windows Media Player, or MuseScore.

## 📁 Project Structure
```
CodeAlpha_MusicGeneration/
├── dataset/            ← Place MIDI files here
├── preprocess.py       ← Extract notes from MIDI files
├── train.py            ← Build and train LSTM model
├── generate.py         ← Generate new music
├── requirements.txt
└── README.md
```

## 🧠 How It Works
1. Preprocessing — MIDI files parsed into note sequences
2. Training — LSTM learns patterns from 44,684 notes
3. Generation — Model predicts notes one by one to compose new music

## 👨‍💻 Author
Built as part of the **CodeAlpha AI Internship Program**
