import sys
sys.path.insert(0, '../backend')

from keywordfinder import KeyWorderFinder


finder = KeyWorderFinder("https://en.wikipedia.org/wiki/Warhammer_40,000")
keywords = finder.get_summary(1,10)
print(keywords)

#Tokenizer does not work
"""keywords = finder.get_token_class()
print(keywords)"""