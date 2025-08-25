import json, os

F="chat_history.json"

def load_hist():
    if os.path.exists(F):
        with open(F,"r",encoding="utf-8") as f: return json.load(f)
    return []

def save_hist(h):
    with open(F,"w",encoding="utf-8") as f: json.dump(h,f,ensure_ascii=False,indent=0)

def add_user(h, m): h.append({"role":"user","content":m})
def add_ai(h, m): h.append({"role":"assistant","content":m})

def history_text(h):
    return "".join([("User: " if x["role"]=="user" else "Assistant: ")+x["content"]+"\n" for x in h])
