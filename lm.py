import requests
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import chromadb
from typing import List
import time

# ── Configuration ──────────────────────────────────────
LM_STUDIO_URL  = 'http://localhost:1234/v1/chat/completions'
MODEL_NAME     = 'local-model'   # LM Studio ignores this
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
CHUNK_SIZE     = 500             # words per chunk
TEMPERATURE    = 0.7
MAX_TOKENS     = 500
TOP_K_RESULTS  = 3

# ── 1. LM Studio Interface ─────────────────────────────
def ask_local_model(prompt: str, context: str = '') -> str:
    start = time.time()
    print(f'Connecting to LM Studio...')
    messages = []
    if context.strip():
        messages.append({
            'role': 'system',
            'content': f'Answer using ONLY this context:\n\n{context}'
        })
    messages.append({'role': 'user', 'content': prompt})
    try:
        response = requests.post(
            LM_STUDIO_URL,
            json={
                'model': MODEL_NAME,
                'messages': messages,
                'temperature': TEMPERATURE,
                'max_tokens': MAX_TOKENS
            },
            timeout=150
        )
        elapsed = time.time() - start
        print(f'Response received in {elapsed:.1f}s')
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.Timeout:
        return 'Timeout: try a smaller model or increase timeout.'
    except requests.exceptions.ConnectionError:
        return 'Connection refused: is LM Studio running on port 1234?'
    except Exception as e:
        return f'Unexpected error: {type(e).__name__}: {e}'

# ── 2. Document Processing ─────────────────────────────
def read_pdf(filepath: str) -> str:
    doc = fitz.open(filepath)
    text = ''
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    words = text.split()
    chunks = []
    overlap = int(chunk_size * 0.1)  # 10% overlap
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk.strip())
    return chunks

# ── 3. Vector Index ────────────────────────────────────
class DocumentIndex:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.client = chromadb.Client()
        self.collection = self.client.create_collection('docs')

    def index_chunks(self, chunks: List[str]) -> None:
        embeddings = self.model.encode(chunks,
                         show_progress_bar=False).tolist()
        ids = [f'chunk_{i}' for i in range(len(chunks))]
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query: str, top_k: int = TOP_K_RESULTS) -> List[str]:
        q_embed = self.model.encode([query],
                      show_progress_bar=False).tolist()
        results = self.collection.query(
            query_embeddings=q_embed,
            n_results=min(top_k, len(self.collection.get()['ids']))
        )
        return results['documents'][0] if results['documents'] else []

# ── 4. Main Pipeline ───────────────────────────────────
def answer_question_from_pdf(pdf_path: str, question: str) -> str:
    print('Reading PDF...')
    text   = read_pdf(pdf_path)
    chunks = chunk_text(text)
    print(f'Split into {len(chunks)} chunks')

    print('Building vector index...')
    index = DocumentIndex()
    index.index_chunks(chunks)

    print('Searching for relevant context...')
    relevant = index.search(question)
    context  = '\n\n---\n\n'.join(relevant)

    print('Generating answer...')
    return ask_local_model(question, context)

# ── Entry Point ────────────────────────────────────────
if __name__ == '__main__':
    PDF_FILE = r"C:\Users\rocks\Documents\Books\[Raymond_A.(Raymond_A._Serway)_Serway,_John_W._Jew_Physics.pdf"  # <-- change this
    QUESTION = 'What is Newton\'s first law of motion?'
    print(f"Asking: '{QUESTION}'\n")
    result = answer_question_from_pdf(PDF_FILE, QUESTION)
    print(f'\nAnswer:\n{result}\n')
