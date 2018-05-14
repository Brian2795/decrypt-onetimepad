def hex_to_nums( msg ):
	"""
	Converts input message of hexadecimals to a list of numbers.
	
	Takes a message str of bytes in the form of hex pairs and translates it to
	their decimal integer equivalents. Outputs translated stream as a list.

	Parameters
    ----------
	msg : str
		string containing stream of hexadecimal bytes

	Returns
    -------
	int
		stream of integers

	"""
	len_msg = int((len(msg)/2))
	bytes_array = [0] * len_msg
	for i in range(len_msg):
		digit1 = hex_num_helper(msg[2*i])
		digit2 = hex_num_helper(msg[2*i + 1])
		bytes_array[i] = 16*digit1 + digit2
	return bytes_array


def nums_to_hex( nums ):
	""" takes in a list of ints and outputs a str list of their 2-digit hex vals """
	return [hex(n).upper()[2:] for n in nums]


def hex_num_helper( hexVal ):
	""" Determines decimal equivalent of hex digit passed in as a chr. """
	if ord(hexVal) < 65:
		val = int(hexVal)
	else:
		val = ord(hexVal.upper()) - 55
	return val


# Converts a list of bytes represented as numbers to a list of characters
def bytes_to_chars( bytesArray ):
	""" returns a list of chr """
	char_list = []
	for b in bytesArray:
		char_list.append(chr(b))
	return char_list


def xor_chrs( chrs ):
	""" returns and XOR of all characters in the input list """
	val = 0
	for c in chrs:
		val ^= ord(c)
	return chr(val)

