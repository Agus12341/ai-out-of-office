import os

TEXT = "I have read your email in 12,000 parallel timelines. In none of them do I reply before Tuesday."

assert 1 <= len(TEXT) < 160, f"entry is {len(TEXT)} code points, must be under 160"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
