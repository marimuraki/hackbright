# 1. All the words that begin with the letter a, independent of case (17096 words)

egrep -c '^[Aa]' words

# 2. All the words that contain the sequence 'ing' (8852 words)

egrep -c 'ing' words

# 3. All the words end in the sequence 'ing' (5539 words)

egrep -c 'ing$' words

# 4. All the words exactly 7 letters long (23869 words)

egrep -c '^.......$' words

# 5. All words with two adjacent 'a's (124 words)

egrep -c 'aa' words

# 6. All words that end in either 'vark' or 'wolf' (8 words)

egrep -c 'vark$|wolf$' words