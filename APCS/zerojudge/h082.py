# https://zerojudge.tw/ShowProblem?problemid=h081
'''
留意編號、勝負判斷、>=、淘汰判斷
'''
n, m = map(int, input().split())
S = [0] + [int(x) for x in input().split()]
T = [0] + [int(x) for x in input().split()]
idx = [int(x) for x in input().split()]

fail_times = [0] * (n + 1)

while len(idx) > 1:
	winner_lists = []
	loser_lists = []
	for i in range(0, len(idx)-1, 2):
		first, second = idx[i], idx[i+1]
		a,b,c,d = S[first], T[first], S[second], T[second]
		if a*b >= c*d:
			winner = first
			S[first] += c*d//(2*b)
			T[first] += c*d//(2*a)
			loser = second
			# fail_times[second] += 1
			S[second] *= 1.5
			T[second] *= 1.5
			

		else:
			winner = second
			S[first] *= 1.5 
			T[first] *= 1.5
			loser = first
			# fail_times[first] += 1
			S[second] += a*b//(2*d)
			T[second] += a*b//(2*c)
			

		winner_lists.append(winner)
		fail_times[loser] += 1
		
		if fail_times[loser] < m:
			loser_lists.append(loser)

	if len(idx) % 2 != 0:
		winner_lists.append(idx[-1])
	idx = winner_lists + loser_lists
print(idx[0]) # final one must be the winner.
