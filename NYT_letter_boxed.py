import itertools
from collections import defaultdict

# Step 1: Setup triplets and triplet lookup
triplets = ["aie", "rtk", "mul", "boh"]
letter_to_triplet = {}
for i, triplet in enumerate(triplets):
    for ch in triplet:
        letter_to_triplet[ch] = i

allowed_letters = set(letter_to_triplet.keys())

# Step 2: Load words and apply all constraints
valid_words = set()

with open("/Users/sourabhsurana/Desktop/Python101/words_alpha.txt") as f:
    for line in f:
        word = line.strip().lower()
        if len(word) < 6:
            continue
        if not set(word).issubset(allowed_letters):
            continue

        # Check adjacency constraint
        valid = True
        prev_triplet = None
        for ch in word:
            current_triplet = letter_to_triplet.get(ch)
            if current_triplet == prev_triplet:
                valid = False
                break
            prev_triplet = current_triplet
        if valid:
            valid_words.add(word)

# Step 3: Group words by starting letter
words_by_start = defaultdict(list)
for word in valid_words:
    words_by_start[word[0]].append(word)

# Step 4: Generate valid pairs where w1[-1] == w2[0]

valid_pairs = []

for w1 in valid_words:
    for w2 in valid_words:
        combined = w1 + w2
            if ((w1 != w2)
                    and (allowed_letters.issubset(set(combined)) == True)
                    and (w1[-1] == w2[0])):
                valid_pairs.append((w1, w2))


# Step 5: Sort and print
valid_pairs.sort(key=lambda x: (len(x[0])+len(x[1]), x[0], x[1]))

valid_pairs[:100]

