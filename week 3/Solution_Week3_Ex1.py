
# Solution to Week 3 Exercise 1

# Question 5
print('Solution 1')
Words = "Hello World"
for i in range(len(Words)):
	print('Letter ' + Words[i] + ' (Position ' + str(i+1) + ')')

print('\n Solution 2')
# Question 6
Words = "Hello World"
for i, letter in enumerate(Words):
	print('Letter ' + letter + ' (Position ' + str(i+1) + ')')
