import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mem_store import load_hist, save_hist, add_user, add_ai, history_text
from helpers import fmt

load_dotenv()
k=os.getenv("OPENAI_API_KEY")
if not k: raise SystemExit("OPENAI_API_KEY missing")
llm=ChatOpenAI(model="gpt-4o-mini",api_key=k)
h=load_hist()
print("🤖 Chatbot ready. Type 'quit' to exit.")

while True:
    u=input("You: ").strip()
    if u.lower() in {"quit","exit","bye"}: print("🤖 Bye!"); break
    add_user(h,u); t=history_text(h)+f"User: {u}\nAssistant:"
    r=llm.invoke(t).content
    add_ai(h,r); save_hist(h)
    print("🤖",fmt(r))
