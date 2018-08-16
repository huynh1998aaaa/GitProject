import stdio
n=stdio.readInt()
t1=1
t2=1
for i in range(2,n):
	t=t1+t2
	t2=t1
	t1=t
	stdio.writeln(str(i))