from queue import heappush,heappop
def issafe(grid,x,y) :
	if(x >= 0 and x < m and y >= 0 and y < n) :
		if(grid[x][y] == 0 or grid[x][y] == 1) :
			return True
		else :
			return False
	else :
		return False

def solve(grid,sx,sy) :

	row = [0,-1,-1,-1,0,1,1,1]
	col = [1,1,0,-1,-1,-1,0,1]
	heap = []
	dis = [[-1]*n for i in range(m)]
	par = [[(-1,-1)]*n for i in range(m)]
	heappush(heap,(0,(sx,sy)))
	dis[sx][sy] = 0
	dest = (-1,-1)
	while(len(heap) != 0) :
		(ux,uy) = heappop(heap)[1]
		if(grid[ux][uy] == 1) :
			dest = (ux,uy)
			break
		for i in range(8) :
			vx = ux + row[i]
			vy = uy + col[i]
			cost = 1
			if(abs(vx) == 1 and abs(vy == 1)) :
				cost = 1.414
			if(issafe(grid,vx,vy) ) :
				if(dis[vx][vy] == -1 or dis[vx][vy] > cost + dis[ux][uy]) :
					dis[vx][vy] = cost + dis[ux][uy]
					heappush(heap,(dis[vx][vy],(vx,vy)))
					par[vx][vy] = (ux,uy)
	return (par,dest)

m = 0
n = 0
t = int(input())
while(t != 0) :
	t -= 1
	m,n = map(int,input().split())
	grid = [list(map(int,input().split())) for i in range(m)]
	sx,sy = map(int,input().split())
	(par,dest) = solve(grid,sx-1,sy-1)
	temp  = dest
	path = []
	while(par[temp[0]][temp[1]] != (-1,-1)) :
		path.append(temp)
		temp = par[temp[0]][temp[1]]

	path.reverse()
	for i in path :
		print(i[0]+1,i[0]+1,end = " ")
	print()


