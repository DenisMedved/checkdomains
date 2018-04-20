
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
        self.scope = 0

    def calculate(self):
        for char in self.name:
            dotPosition = self.name.find(".")
            self.scope += self.name[:dotPosition].count(char)

domains = []

with open(filepath, "r") as f:
    for line in f:
        domain = Domain(
                line
                    .replace("\n", "")
                    .replace("\r", "")
        )
        domain.calculate()
        domains.append(domain)

position = 1;

print("Top 50")
for domain in sorted(domains, key=lambda domain: domain.scope, reverse=True)[:50]:
    print("{0}) {1} ({2})".format(position, domain.name, domain.scope))
    position += 1


print("Done!")
