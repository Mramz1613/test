def solve(equation):
	return -eval(equation[1:].replace("=", "-"))

print(solve("x + 43 = 50"))