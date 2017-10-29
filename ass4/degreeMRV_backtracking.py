from queue import heappush, heappop
def pprint(grid) :
	for i in range(m) :
		for j in range(n) :
			print(grid[i][j],end = " ")
		print()

def issafe(x,y) :
	if(x >= 0 and x < m and y >= 0 and y < n):
		return True
	else :
		return False
def degreeMRV(grid,x,y) :

	row = [-1,-1,-1,1,1,1,0,0]
	col = [0,1,-1,0,1,-1,1,-1]
	for i in range(8) :
		xindex = x + row[i]
		yindex = y + col[i]
		pos = m*n - count
		if(not issafe(xindex,yindex) or grid[xindex][yindex] != " ") :
			continue
		for member in slist :
			if(not mark[member]) :
				for j in range(8) :
					fxindex = xindex + row[j]
					fyindex = yindex + col[j]
					if(issafe(fxindex,fyindex)) :
						if(grid[fxindex][fyindex] != " " and not mark[grid[fxindex][fyindex]] and grid[fxindex][fyindex] not in adj[member]) :
							pos -= 1
							break
		degree = 0
		for j in range(8) :
			fxindex = xindex + row[j]
			fyindex = yindex + col[j]
			if(issafe(fxindex,fyindex) and grid[fxindex][fyindex] == " ") :
				degree += 1

		heappush(myheap,(pos,degree,(xindex,yindex)))
	return heappop(myheap)[2]

def solve(grid,x,y) :
	
	global count
	if(count == m*n) :
		return True

	available = set()
	notavailable = set()
	for student in slist :
		if(not mark[student]) :
			available.add(student)
	row = [-1,-1,-1,1,1,1,0,0]
	col = [0,1,-1,0,1,-1,1,-1]
	for student in available :
		for i in range(8) :
			xindex = x + row[i]
			yindex = y + col[i]
			if(issafe(xindex,yindex)) :
				if(grid[xindex][yindex] != " " and grid[xindex][yindex] not in adj[student] and grid[xindex][yindex]  != student) :
					notavailable.add(student)
					break

	available = sorted(list(available.difference(notavailable)))

	if(len(available) == 0) :
		return False
	for student in available :
		grid[x][y] = student
		count += 1
		mark[student] = True
		(xnext,ynext) = degreeMRV(grid,x,y)
		if(solve(grid,xnext,ynext) == True) :
			return True

		grid[x][y] = " "
		count -= 1
		mark[student] = False
				
	return False			



t = int(input())
m = 0
n = 0
adj = {}
slist = []
mark = {}
count = 0
while(t != 0) :
	t -= 1
	m,n = map(int,input().split())
	adj = {}
	slist = []
	for i in range(m*n) :
		temp = input().split()
		roll = temp[0]
		slist.append(roll)
		a = temp[1]
		adj[roll] = temp[2:]

	slist = sorted(slist)
	grid = [[" "]*n for i in range(m)]

	for i in slist :
		mark[i] = False
	count = 0
	myheap = []
	if(solve(grid,0,0)) :
		pprint(grid)
	else :
		print("not possible")

