
import whois
import time

class Domain:
    def __init__(self, name):
        self.name = name
        self.available =  True
        self.checked = False

firstLevels = [".cc"];
domains = [];


with open("checkdomain.txt", "r") as f:
    for line in f:
        for suffix in firstLevels:
            domains.append(Domain(str(line + suffix).lower()))

checkcount = 0

for domain in domains:
    response = whois.whois(domain.name)
    domain.available = bool(response.name is None )
    domain.checked = True
    checkcount += 1
    if checkcount % 10 == 0:
        percent  = round(checkcount / len(domains) * 100, 2)
        print("{0} of {1} {2}%".format(checkcount, len(domains), percent))
    time.sleep(1)

for domain in domains:
    if domain.available is True:
        print(domain.name)

print("Done!")