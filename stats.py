import statistics

numbers = input("Enter multiple numbers, seperate with a space: ")

#converting to float
num_letters = numbers.split()
number = []

for element in num_letters:
	number.append(float(element))


#obtaining highest number
max_no = max(number)
print("\n\nThe Highest Number is " + str(max_no))

#obtaining lowest number
min_no = min(number)
print("The lowest number is " + str(min_no))

#obtaining mode
mode = statistics.mode(number)
print("The most frequent number is " + str(mode))

#obtaining median
median = statistics.median(number)
print("The median is " + str(median))

#obtaining avg
	#obtaining total
total = sum(number)
def average():
	avg = total / len(number)
	return avg

print("The average is: " + str(average()))
print("Created by shriram siuu\n")