import winsound 

print "Binary Sounddd"
print "Enter the duration of a note in ms"
print "E.g 200"
rate = int(input(">"))

print "Enter a 4bit Binary note"
print "Or more than one note seperated by spaces"

print "Notes"
print "0000 = no sound"
print "0001 = Low C"
print "0010 = D"
print "0011 = E"
print "0100 = F"
print "0101 = G"
print "0110 = A"
print "0111 = B"
print "1000 = C"

print("e.g: ")
print("0101 0101 0101 0010 0011 0011 0010 0000 0111 0111 0110 0110 0101")

soundB = raw_input(">")

#split() seperates the string using a seperator
for note in soundB.split():

	if note == "0000":
		freq = 37

	elif note =="0001":
		freq = 262

	elif note =="0010":
		freq = 294

	elif note =="0011":
		freq = 330

	elif note =="0100":
		freq = 349

	elif note == "0101":
		freq = 392

	elif note == "0110":
		freq = 440

	elif note == "0111":
		freq = 494

	elif note == "1000":
		freq = 523

	winsound.Beep(freq, rate)		
