
# + poly[1]b(a-2) + .. + poly[a-1]
def x(poly, a, b):

	# Initialize result
	result = poly[0]

	# Evaluate value of polynomial
	# using Horner's method
	for i in range(1, a):

		result = result*b + poly[i]

	return result

# Driver program to
# test above function.


# Let us evaluate value of
# 2x3 - 6x2 + 2x - 1 for x = 3
poly = [18, -663 , 1 , 79854]
b = 3
a = len(poly)

print("Value of polynomial is:", x(poly, a, b))
