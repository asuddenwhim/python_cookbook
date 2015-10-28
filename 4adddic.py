#use the entry if present else add to dictionary

def addWord(word, page):
	theIndex.setdefault(word, page)
theIndex = {'Intro': 1, 'Content': 3}

addWord('Conclusion', 5)

print theIndex