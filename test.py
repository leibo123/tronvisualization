import json
from datetime import datetime
import glob

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
                    print(d3)
                    tronResults += "<pre>" + d3 + "</pre>"
                tronResults += "</div>"
    bodyEnd = '</main></body><script src="test.js"></script></html>'
    html_results = header + bodyStart + tronResults + bodyEnd
    out_path = filename + ".html"
    with open(out_path, "w") as out:
        out.write(html_results)   
