import random
from math import ceil

def sum_frac_list(sum_list, denom): # frac - fraction, denom - denominator
	sec = int(ceil(len(sum_list)/denom)) # sec - section, ceiling allows complete partitions of list
	totals = []

	for i in range(0,denom):
		total = sum(sum_list[sec*i:sec*(i+1)])
		totals.append(total)
	print_totals_sec(totals)
	return totals

def sum_every_other(sum_list, gap):
	totals = []
	for j in range(0, gap):
		total = 0
		for i in range(j,len(sum_list), gap):
			total = sum_list[i] + total
		totals.append(total)
	print_totals_oth(totals, gap)
	return totals

def print_totals_sec(totals_list): # section
	for i in range(0,len(totals_list)):
		if(i % 10 == 0):
			print(f"{i+1}st section sum: {totals_list[i]}")
		elif(i % 10 == 1):
			print(f"{i+1}nd section sum: {totals_list[i]}")
		elif(i % 10 == 2):
			print(f"{i+1}rd section sum: {totals_list[i]}")
		else:
			print(f"{i+1}th section sum: {totals_list[i]}")

def print_totals_oth(totals_list, gap): # every other
	for i in range(0, len(totals_list)):
		print(f"Sum every other {gap} with offset {i}: {totals_list[i]}")

newlist = [i for i in range(1,10)] # Starting numbers
print(newlist)

random.shuffle(newlist) # Hidden list, newlist is now shuffled

hidden_sec_totals = sum_frac_list(newlist, 3)
hidden_oth_totals = sum_every_other(newlist, 3)

message = input("Press s for the solution, or any thing else to quit: ")
if(message == 's'):
	print(newlist)
