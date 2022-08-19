numbers=[float(input()) for i in range(int(input()))]
def taghrib(n):return f"{int(n*1000)/1000:.3f}"
print(f'Max: '+taghrib(max(numbers)),f'Min: '+taghrib(min(numbers)),'Avg: '+taghrib(sum(numbers)/len(numbers)),sep='\n')