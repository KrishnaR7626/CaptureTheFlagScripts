#!/usr/bin/python3

firstPart = "543210"
secondPart = "1234"
validCards = []
for i in range(0,1000000):
	number = "{}{}{}".format(firstPart,str(i).zfill(6),secondPart)
	if int(number) % 123457 == 0:
		validCards.append(number)
for card in validCards:
	temp = card
	luhnCard = ""
	for char, i in zip(temp,range(len(temp))):
		if i%2 == 0:
			value = str(int(char)*2)
			counter = 0
			for i in value:
				counter+=int(i)
			luhnCard += str(counter)
		else:
			luhnCard+=char
	total = 0
	for number in luhnCard:
		total+=int(number)
	if total % 10 == 0:
		print("{} is a valid card".format(card))
