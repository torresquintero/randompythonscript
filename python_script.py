import sys

print "I work"

myfile = sys.argv[1]

with open(myfile) as f:
    content = f.readlines()

counter  = 1

for x in content:
    print counter, x
    counter = counter + 1
