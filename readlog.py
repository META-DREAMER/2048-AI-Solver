import sys

with open('log.txt', 'r') as f:
	logs = f.readlines()

output = ""
for line in logs:
	output += line[11]


with open("log_stripped.txt", "w") as log_stripped:
  	log_stripped.write(output)