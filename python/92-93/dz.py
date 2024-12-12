# def high_and_low(numbers:str):
#     new = numbers.split(" ")
#     new = list(map(int,new))
#     numbers = str(max(new))+" "+str(min(new))
#     return numbers
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
def digital_root(n):
	return n%9 or n and 9

print(digital_root(132189))