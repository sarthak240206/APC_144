scores=[]
for i in range(10):
    scores.append(int(input(f"Score of match {i+1}: ")))
print("Highest score:",max(scores))
print("Lowest score:",min(scores))
print("Total runs:",sum(scores))
print("Average runs:",sum(scores)/10)
print("Centuries:",sum(x>=100 for x in scores))
print("Half-centuries:",sum(50<=x<100 for x in scores))
