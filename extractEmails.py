import re

fileInput = 'input.html'
fileOutput = 'email_output.txt'

f = open(fileInput)
content = f.read()

# email regex
regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

# set makes them unique
results = set(regex.findall(content))

emails = ""
count = len(results)
for x in results:
    emails += str(x[0])+"\n"

print("Reading " + fileInput + ":\n------------------------------------------")
print(emails)
print("unique user: " + str(count))
print("------------------------------------------")

# function to write file
def writefile():
    f = open(fileOutput, 'w')
    f.write(emails)
    f.close()
    print("File written: " + fileOutput)

writefile()
