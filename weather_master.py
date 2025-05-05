"""
File: weather_master.py
Name:yangziting
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


def main():
	"""
	When the user enters some temperatures, this file can
	find the maximum, minimum temperature, calculate the
	average temperature, and show how many day(s)'s
	temperature is lower than 16 degree
	"""

	EXIT = -100  # This constant controls when to stop
	tem = int(input('Next temperature: (or ' + str(EXIT) + ' to quit) '))
	if tem == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = tem
		minimum = tem
		mean = tem
		# "cold" is used to calculate how many days the temperatures are lower than 16 degrees
		cold = 0
		# "num" is used to calculate how many temperatures the user enters
		num = 1
		while True:
			if tem < 16:
				cold = cold + 1
			tem = int(input('Next temperature: (or ' + str(EXIT) + ' to quit) '))
			if tem == EXIT:
				break
			mean = mean + tem
			num = num + 1
			if tem > maximum:
				maximum = tem
			if tem < minimum:
				minimum = tem
		average = mean / num
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
