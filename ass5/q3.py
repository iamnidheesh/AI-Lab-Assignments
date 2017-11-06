from queue import heappush,heappop
def issafe(grid,x,y) :
	if(x >= 0 and x < m and y >= 0 and y < n) :
		if(grid[x][y] == 0 or grid[x][y] == 1) :
			return True
		else :
			return False
	else :
		return False
def turnanticlock(x) :
	if(x == 0) :
		return 7
	else :
		return x - 1

def turnclock(x) :
	if(x == 7) :
		return 0
	else :
		return x + 1

def solve(grid,sx,sy) :


	heap = []
	dis = [[-1]*n for i in range(m)]
	par = [[(-1,-1)]*n for i in range(m)]
	direction = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
	heappush(heap,(0,0,(sx,sy)))
	dis[sx][sy] = 0
	dest = (-1,-1)
	while(len(heap) != 0) :
		top = heappop(heap)
		(ux,uy) = top[2]
		go = top[1]
		curr_cost = top[0]
		if(grid[ux][uy] == 1) :
			dest = (ux,uy)
			break
		#go in direction
		vx = ux + direction[go][0]
		vy = uy + direction[go][1]
		if(abs(direction[go][0]) == 1 and abs(direction[go][1]) == 1) :
			cost = 1.414
		else :
			cost = 1
		if(issafe(grid,vx,vy) and dis[vx][vy] == -1 ) :
			dis[vx][vy] = curr_cost + cost
			heappush(heap,(dis[vx][vy],go,(vx,vy)))
			par[vx][vy] = (ux,uy)
		
		#change direction clockwise
		heappush(heap,(curr_cost+5,turnclock(go),(ux,uy)))
		#change direction anticlockwise
		heappush(heap,(curr_cost+5,turnanticlock(go),(ux,uy)))

	return (par,dest)

m = 0
n = 0
t = int(input())
while(t != 0) :
	t -= 1
	m,n = map(int,input().split())
	grid = [list(map(int,input().split())) for i in range(m)]
	sx,sy = map(int,input().split())
	(par,dest) = solve(grid,sx,sy)
	temp  = dest
	path = []
	while(par[temp[0]][temp[1]] != (-1,-1)) :
		path.append(temp)
		temp = par[temp[0]][temp[1]]
	path.append(temp)
	path.reverse()
	for i in path :
		print(i[0],i[1],end = " ")
	print()


