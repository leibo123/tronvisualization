import json
from datetime import datetime
import glob
import unicodedata

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

def boardToHTML(board):
    unicodedata.normalize('NFKD', board).encode('ascii','ignore')

    b = "<div class='board-wrapper'><div class='board'>"
    start = False
    for char in board:
        if char == "#" and not start:
            start = True
        if not start:
            continue

        if char == " ":
            b += "<span class='space'></span>"
        if char == "#":
            b += "<span class='wall'></span>"
        if char == "x":
            b += "<span class='barrier'></span>"
        if char == "1":
            b += "<span class='player1'><p>1</p></span>"
        if char == "2":
            b += "<span class='player2'><p>2</p></span>"
        if char == "*":
            b += "<span class='trap'><p>*</p></span>"
        if char == "@":
            b += "<span class='armor'><p>@</p></span>"
        if char == "^":
            b += "<span class='speed'><p>^</p></span>"
        if char == "!":
            b += "<span class='bomb'><p>!</p></span>"

    b += "</div></div>"
    return b

header = '<!doctype html><html><head><title>CS1410 &middot; TRON Results</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><link rel="stylesheet" href="./results.css"></head>'
index = 0
for filename in glob.glob('*.txt'):
    tronResults = ""
    p1_ind = findnth(filename, '_', 3)
    p2_ind = findnth(filename, '_', 4)
    player1 = filename[p1_ind + 1:p2_ind]
    player2 = filename[p2_ind + 1:-4]
    bodyStart = '<body><header class="default-header"><h1>TRON-41</h1><h2>' + filename[:p1_ind].replace("_", " ") + ": " + player1 + " v. " + player2 + '</h2><img id="loading" src="https://media0.giphy.com/media/r09BeWEk9JZL2/source.gif"></header><main class="container">'

    with open(filename) as f:
        print("opening", filename, "for reading.")
        data = json.load(f)
        for d1, d2 in data:
            tronResults += "<div class='tournament-container'>"
            firstturn = True
            flip = False
            for d3, d4 in zip(d1, d2):
                if firstturn:
                    if "x" in d3:
                        flip = True
                    firstturn = False
                if flip:
                    tronResults += boardToHTML(d4)
                    tronResults += boardToHTML(d3)
                else:
                    tronResults += boardToHTML(d3)
                    tronResults += boardToHTML(d4)
            if len(d1) > len(d2):
                tronResults += boardToHTML(d1[len(d1) - 1])
            elif len(d2) > len(d1):
                tronResults += boardToHTML(d2[len(d2) - 1])
            tronResults += "</div>"
            if len(d1) == len(d2):
                if flip:
                    tronResults += "<p>Player 2 (" + player2 + ") wins.</p>"
                else:
                    tronResults += "<p>Player 1 (" + player1 + ") wins.</p>" 
            else:
                if flip:
                    tronResults += "<p>Player 1 (" + player1 + ") wins.</p>"
                else:
                    tronResults += "<p>Player 2 (" + player2 + ") wins.</p>"

    bodyEnd = '</main></body><script src="test.js"></script></html>'
    html_results = header + bodyStart + tronResults + bodyEnd
    out_path = filename[:-4] + ".html"
    with open(out_path, "w") as out:
        out.write(html_results)  


