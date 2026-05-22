"""
VibeDetect
---
A simple rulebased app which detects if a code is Vibe coded or not.
It also shows it's confidence.
Then it shows the reason.

It's useful for maintainers who want pure human written code for their projects.
It works best in python, while it MAY work for other langs I haven't really tested it.

It's mostly a fun little experiment, but it works pretty great (in python atleast)
"""

reason = []
confidence = 0
matchedWords = []
repeats = 0
def checkClassicWords(inputs):
    global confidence, matchedWords, repeats
    with open("classicAIWords.vd", encoding="utf-8") as r:
        lines = r.readlines()
        for line in lines:
            for lineInput in inputs:
                repeats += 0.4 # Idk why but ts works best
                if lineInput in line:
                    reason.append(1)
                    confidence += 1
                    matchedWords.append(lineInput)
def checkIfSimilar(inputs):
    global confidence, matchedWords, repeats
    inside = False
    comment = "#" # Yea if you want to use it on other langs maybe change this
    for line in inputs:
        repeats += 0.4
        if comment in line:
            confidence += 0.5
        if line == '""""': # And also this
            inside = not inside
            continue
        if inside:
            confidence += 1

inputs = open("Input.vd", "r", encoding="utf-8").readlines()
checkClassicWords(inputs)
checkIfSimilar(inputs)
confidence = round((confidence/repeats)*100, 2)
print()
if confidence > 100: # Kinda dumb fix ikik
    confidence = 99.99
if confidence < 50:
    print("Likely not ai generated.")
else:
    print("Likely ai generated.")
print("|---------------------------------------------------------------------------|")
print(str(confidence) + "%" + " Confident it's ai generated")
reason = max([0, 1], key=lambda x: reason.count(x))
if reason == 1 and confidence > 50:
    reason = "Matched a lot of classic AI words."
elif reason == 0 and confidence > 50:
    reason = "It contains a lot of comments"
else:
    reason = "It does not contain much classic AI words nor comments."
print("Reason: " + reason)
confidence = 0