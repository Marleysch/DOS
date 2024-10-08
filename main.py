import copy


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
	# print(f'subls: {subls}')

	medians = []
	for subl in subls:
		subl.sort()
		medians.append(subl[len(subl)//2])

	M = Select(len(l) // 10, medians)
	l1 = []
	for num in l:
		if num < M:
			l1.append(num)
	# print(f'l1: {l1}')

	l3 = []
	for num in l:
		if num > M:
			l3.append(num)
	# print(f'l3: {l3}')
	# print(f'k: {k}')
	Mpos = len(l1) + 1
	# print(f'Mpos: {Mpos}')
	# print(f'M: {M}')

	if k == Mpos:
		# print('M won')
		return M
	elif k < Mpos:
		# print('m<k')
		return Select(k, l1)
	else:
		# print('m>k')
		return Select(k-len(l1) - 1, l3)




file = '7.txt'
kandl = getkandl(f"{file}.txt")
l = kandl[1]
k = kandl[0]

print(f'size: {len(l)}\nanswer: {Select(k,l)}')

