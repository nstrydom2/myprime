



def is_prime(num):
	mmax = 0
	if num < 5:
		mmax = num
	else:
		mmax = int(num / 2)

	for i in range(2, mmax):
		if num % i == 0:
			return False
	return True

print(is_prime(7))
print(is_prime(12))


