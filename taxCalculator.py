"""This is a rough tax calculator for the year 2015. It asks for your income, state tax rate and standard
deduction, and then calculates your approximate tax. If standard deduction is zero, it assumes you are
self-employed and applies the full tax burden upon the income declared (the additional Social Security)
tax that your employer would otherwise pay. If any standard deduction is present, then it calculates
Social Security tax at half the full rate."""
def calculateFed(amount):
	if amount <= 9225:
		result= amount*0.1;
	if 9225 < amount <= 37450:
		result = 922.50 + (amount-9225)*0.15
	if 37450 < amount <= 90750:
		result = 5156.25 + (amount-37450)*0.25
	if 90750 < amount <=189300:
		result = 18481.25 + (amount-90750)*0.28
	if 189300 < amount <= 411500:
		result = 46075.25 + (amount-189300)*0.33
	if 411500 < amount <= 413200:
		result = 119401 + (amount-411500)*0.35
	if amount > 413200:
		result = 119996.25 + (amount-413200)*0.396
	return result

def calculateSS(amount,sd):
	if sd == 0:
		rate = 0.124
	if sd > 0:
		rate = 0.062
	if amount<=118500:
		result = amount*rate
	if amount>118500:
		result = 118500*rate
	return result

def calculateMC(amount):
	result = amount*0.029
	return result

def calculateState(amount, rate):
	result = amount*rate
	return result

def main():
	amount=int(input('Please enter your income: '))
	stateRate=float(input('Please enter your state tax rate as decimal: '))
	stdDed = int(input('Please enter your standard deduction if any: '))
	federaltax=calculateFed(amount-stdDed)
	socialsecurity=calculateSS(amount, stdDed)
	medicare=calculateMC(amount)
	statetax=calculateState(amount,stateRate)

	total=federaltax+socialsecurity+medicare+statetax
	percentage = total/amount*100

	print('===============================================')
	print('INCOME: $', amount)
	print('TAXES: ')
	print('  Federal income tax: ', federaltax)
	print('  Social Security tax:', socialsecurity)
	print('  Medicare tax:       ', medicare)
	print('  State income tax:   ', statetax)
	print('                       ----------')
	print('      TOTAL TAXES:    ', total)
	print(' ')
	print('You pay {0}% percent of your income in taxes'.format(str(round(percentage, 2))))
	print('===============================================\n')

if __name__=='__main__':
	main()