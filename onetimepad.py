"""
Jung S. Lee
UID: 112973353
CMSC456-0201
"""

import texthelper as th

# XOR all messages together
# Identify the space characters (assume there is at least one space)
# Determine the key at that postition
# Use determined key to decipher other messages

len_msg = 31
num_msgs = 7

def main():
	with open('./ctexts.txt') as fin:
		ctexts = fin.readlines()
		ctexts = [th.hex_to_nums(l.strip()) for l in ctexts]
		key_pred = predict_key(ctexts)
		ptexts = apply_key_to_all(ctexts,key_pred)
		ptexts_eng = clean_ptexts(ptexts)
		for text in ptexts_eng:
			print(text)

		# Manual adjustment of key based on guessed valued
		key = key_pred.copy()
		key[0] = ctexts[0][0] ^ ord('I')
		key[6] = ctexts[0][6] ^ ord('l')
		key[8] = ctexts[0][8] ^ ord('n')
		key[10] = ctexts[0][10] ^ ord('i')
		key[17] = ctexts[0][17] ^ ord('e')
		key[20] = ctexts[0][20] ^ ord('e')
		key[29] = ctexts[0][29] ^ ord('n')
		key[30] = ctexts[0][30] ^ ord('.')

		# Reapply new key
		ptexts = apply_key_to_all(ctexts,key)
		ptexts_eng = clean_ptexts(ptexts)
		print()
		for text in ptexts_eng:
			print(text)



def predict_key( ctexts ):
	""" determine known vals of the pad using the predicted spaces in the texts """ 
	space_locs = predict_space_locs(ctexts)
	key_pred = [None]*len_msg
	
	for i in range(len_msg):
		id_msg = space_locs[i]
		if id_msg == -1:
			char_key_pred = None
		else:
			cipher_char = ctexts[id_msg][i]
			char_key_pred = cipher_char ^ ord(' ')
		key_pred[i] = char_key_pred
	return key_pred


def apply_key_to_all( ctexts, key ):
	""" applies the input key to the input cipher texts to return ptexts """
	ptexts = []
	for ctext in ctexts:
		ptext = apply_key(ctext,key)
		ptexts.append(ptext)
	return ptexts


def clean_ptexts( ptexts_ascii ):
	ptexts = []
	for ptext_ascii in ptexts_ascii:
		ptext = clean_ptext(ptext_ascii)
		ptexts.append(ptext)
	return ptexts


def predict_space_locs( ctexts ):
	""" predicts a text # a space is contained in for each index, -1 if unsure """
	space_locs = []
	for i in range(31):
		scores = compare_index(ctexts, i)
		try:
			loc = scores.index(num_msgs)
		except:
			loc = -1
		space_locs.append(loc)
	return space_locs


def clean_ptext( ptext_ascii ):
	""" converts a list of ascii characters to  """  
	ptext = [chr(c) if c != 0 else '_' for c in ptext_ascii]
	return ''.join(ptext)


def apply_key( ctext, key ):
	ptext = [0]*len_msg
	#print(ctext)
	for i in range(len_msg):
		if key[i] != None:
			ptext[i] = ctext[i] ^ key[i]
	return ptext


def compare_index( ctexts, i ):
	""" compares the ith character of all ciphertexts in the input list """
	""" outputs a list of scores indicating each chars liklihood of being a spcace """
	scores = []
	for j in range(num_msgs):
		list_xors = []
		for k in range(num_msgs):			
			xor = ctexts[j][i] ^ ctexts[k][i]
			#print('\t\t(%d, %d): %d' % (j, k, xor))
			list_xors.append(xor)
		score = space_score(list_xors)
		scores.append(score)
	return scores


def space_score( list_xors ):
	""" determines if this char is likely a space based on its xor collision with """
	score = 0
	for xor in list_xors:
		if (xor > 64) or (xor == 0):
			score += 1
	return score


main()
