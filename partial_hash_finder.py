import string
import hashlib

# This program is written in Python 3
# This program generates MD5 hashes from a wordlist and compares to a partial
# hash you provide.

words_to_hash = []

# Describe program and prompt for input.
print('*******************')

print('This program looks for hash collisions.')
print('Make sure there is wordlist.txt is in the same folder where you run this.\n')

print('*******************')

partial_hash = input('What is the partial hash you want to match? ')

# Save the partial hash input by user; note there is no error checking on this.
partial_hash_len = len(partial_hash)
	
with open('wordlist.txt') as f:
    words_to_hash = f.read().splitlines()
	
i =0 #counter
num_words=len(words_to_hash) # store number of words in wordlist to loop through

# Provide information on wordlist
print ("Number of Words in wordlist.txt to check: " + str(num_words))

print('*******************')

# Set flag if you only want find one match.
found_hash = 0

while i < num_words:
	current_hash = hashlib.md5(words_to_hash[i].encode()).hexdigest()
	
	j = 0 # reset counter to check each character of partial hash
	while j < partial_hash_len:
		if(current_hash[j]== partial_hash[j]):
			if j == partial_hash_len - 1:
				# print headers for output
				print ("Word: MD5")
				print (words_to_hash[i] + ": " + current_hash)
				found_hash = 1
			j = j+ 1
		else:
			break
	
	if found_hash:
		break
	else:
		i = i+1

if found_hash == 0:
	print('No hashes found. Try a larger wordlist.')