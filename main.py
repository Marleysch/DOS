

def getkandl(file):
	with open(file,"r") as file:
		contents = file.read()
	contents = contents.replace(" ", "")
	contents = contents.replace("{", "")
	contents = contents.replace("}", "")

	firstcomma = contents.index(',')
	k = int(contents[:firstcomma])

	l = []
	num = ''
	for char in contents[firstcomma + 1:]:
		if char ==',':
			l.append(int(num))
			num =''
		else:
			num += char
	l.append(int(num))

	return [k, l]

def Select(k,l):
	# Base
	if len(l) < 5:
		l.sort()
		return l[k-1]

	subls = []
	for i in range(len(l)//5):
		row = [x for x in l[5*i:5*(i+1)]]
		subls.append(row)
	leftover = len(l) % 5
	if leftover != 0:
		subls.append([x for x in l[5 * (len(l)//5):]])

	medians = []
	for subl in subls:
		subl.sort()
		medians.append(subl[len(subl)//2])

	M = Select(len(l) // 10, medians)
	l1 = []
	for num in l:
		if num < M:
			l1.append(num)

	l3 = []
	for num in l:
		if num > M:
			l3.append(num)

	Mpos = len(l1) + 1


	if k == Mpos:
		return M
	elif k < Mpos:
		return Select(k, l1)
	else:
		return Select(k-len(l1) - 1, l3)

if __name__ == "__main__":
	file = '7.txt'
	kandl = getkandl(f"{file}")
	l = kandl[1]
	k = kandl[0]
	print(f'k: {k}')

	print(f'size: {len(l)}\nanswer: {Select(k,l)}')

