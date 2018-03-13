
import whois
import time
import sys
import os.path

if len(sys.argv) < 2:
    print(sys.exit("Filename with domains as as first argiment is requered"))

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    sys.exit("File {0} is not exists".format(filepath))

class Domain:
    def __init__(self, name):
        self.name = name
        self.available =  True
        self.checked = False

firstLevels = [".cc"]
domains = []

with open("checkdomain.txt", "r") as f:
    for line in f:
        for suffix in firstLevels:
            domains.append(
                Domain(
                    str(line + suffix)
                        .lower()
                        .replace("\n", "")
                        .replace("\r", "")
                )
            )

checkcount = 0
available = 0
for domain in domains:
    response = whois.whois(domain.name)
    domain.available = bool(response.name is None )
    domain.checked = True
    checkcount += 1
    if domain.available:
        available += 1
    if checkcount % 5 == 0:
        percent  = round(checkcount / len(domains) * 100, 2)
        print("Checked: {0} of {1} ({2}%). Available: {3}".format(checkcount, len(domains), percent, available))
    time.sleep(1)

saveresult = len(sys.argv) >= 2

if saveresult:
    f = open(sys.argv[2], "w")
for domain in domains:
    if domain.available is True:
        print(domain.name)
        if saveresult:
            f.write(domain.name + "\n")
if saveresult:
    f.close()

print("Done!")
