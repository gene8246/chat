
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

new = []
for line in lines:
	s = line.split( )
	time = s[0][:5]
	name = s[0][5:]
	new.append(time + ' ' + name + ':' + s[1])
print(new)