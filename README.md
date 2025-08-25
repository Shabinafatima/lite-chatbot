# lite-chat-minimal

Minimal LangChain + OpenAI CLI chatbot with persistent memory.
- Optimized code, no inline comments
- API key via `.env` (never committed)
- New filenames

## Setup
1) Python 3.9+
2) Install deps:
   ```bash
   pip install -r requirements.txt
   ```
3) Copy `.env.example` to `.env` and set your key:
   ```env
   OPENAI_API_KEY=sk-proj-your_key_here
   ```

## Run
```bash
python main.py
```

## Publish to GitHub
```bash
git init
git add .
git commit -m "init: minimal LC chatbot"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
