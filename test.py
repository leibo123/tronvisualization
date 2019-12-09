import json
from datetime import datetime
import glob
import unicodedata


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
            b += "<div class='space'></div>"
        if char == "#":
            b += "<div class='wall'></div>"
        if char == "x":
            b += "<div class='barrier'></div>"
        if char == "1":
            b += "<div class='player1'><p>1</p></div>"
        if char == "2":
            b += "<div class='player2'><p>2</p></div>"
        if char == "*":
            b += "<div class='trap'><p>*</p></div>"
        if char == "@":
            b += "<div class='armor'><p>@</p></div>"
        if char == "^":
            b += "<div class='speed'><p>^</p></div>"
        if char == "!":
            b += "<div class='bomb'><p>!</p></div>"

    b += "</div></div>"
    return b
    



header = '<!doctype html><html><head><title>CS1410 &middot; TRON Results</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><link rel="stylesheet" href="./results.css"></head>'
bodyStart = '<body><header class="default-header"><h1>TRON-41</h1></header><main class="container">'
index = 0
for filename in glob.glob('*.txt'):
    tronResults = ""
    with open(filename) as f:
        print(filename)
        data = json.load(f)
        for d in data:
            print("===========CUT 1===============")
            for d2 in d:
                print("xxxxxxxxxxxxxxCUT 2xxxxxxxxxxxxx")
                tronResults += "<div class='tournament-container'>"
                for d3 in d2:
                    tronResults += boardToHTML(d3)
                tronResults += "</div>"
    bodyEnd = '</main></body><script src="test.js"></script></html>'
    html_results = header + bodyStart + tronResults + bodyEnd
    out_path = filename + ".html"
    with open(out_path, "w") as out:
        out.write(html_results)  


