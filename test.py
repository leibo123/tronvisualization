import json
from datetime import datetime

header = '<!doctype html><html><head><title>CS1410 &middot; TRON Results</title><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"><meta http-equiv="x-ua-compatible" content="ie=edge"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"><link rel="stylesheet" href="./results.css"></head>'
bodyStart = '<body><header class="default-header"><h1>TRON-41</h1></header><main class="container"><div id="tournament-container">'
tronResults = ""
index = 0
with open("test1.txt") as f:
	data = json.load(f)
	for d in data:
		# print("===========CUT 1===============")
		for d2 in d:
			# print("xxxxxxxxxxxxxxCUT 2xxxxxxxxxxxxx")
			for d3 in d2:
				print(d3)
				tronResults += "<pre>" + d3 + "</pre>"
        

bodyEnd = '</div><p id="date">Published on {0}</p></main></body><script src="./test.js"></script></html>'.format(
    datetime.today().strftime("%b %d at %I:%M %p")
)

html_results = header + bodyStart + tronResults + bodyEnd
out_path = "tron_results.html"
with open(out_path, "w") as out:
    out.write(html_results)


# def boardToHTML(board) {
# 	for i in range()
# }