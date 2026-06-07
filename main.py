import csv

charNames = []
charWinrates = []

with open("input/characters.csv") as charFile:
    reader = csv.DictReader(charFile)
    for row in reader:
        charNames.append(row["Character"])
        charWinrates.append(float(row["Win Rate"]))

print(charNames)
print(charWinrates)

## Begin drawing the bar graph

with open("output/charChart.html", "w") as outputFile:
    outputFile.write('<svg width="1080" height="400">')
    outputFile.write(f'<rect x="50" y="500" width="50" height="{charWinrates[0]*4}" fill="red" />')
    outputFile.write('</svg>')