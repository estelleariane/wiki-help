import sys
sys.stdout.reconfigure(encoding="utf-8")
import wikipedia

result = wikipedia.page("Louisville Kentucky")
print(result.summary)