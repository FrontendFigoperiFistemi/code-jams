

f = open("i1.txt")
cases = int(f.readline().strip())

for i in range(cases):
	result = "Yes"
	l = []
	pair = {}
	num = int(f.readline().strip())
	for j in range(num):
		(a,b) = f.readline().strip().split(" ")
		l.append(a)
		l.append(b)
		if a in pair:
			pair[a].append(b)
		else:
			pair[a] = [b]
		if b in pair:
			pair[b].append(a)
		else:
			pair[b] = [a]
	s = set(l)
	for p in s:
		if result == "No":
			break
		enemy = pair[p]
		for e in enemy:
			if result == "No":
				break
			aganist = pair[e]
			for a in aganist:
				if a in enemy:
					result = "No"
					break
	print "Case #"+str(i+1) + " " + result