# Letter Boxed Word Chain Generator

This project implements a constrained English word-pair generator inspired by *The New York Times'* game **Letter Boxed**. It identifies valid two-word chains that:

- Use a fixed set of letters (typically 12, divided into four 3-letter groups)
- Use **each letter at least once**
- Chain such that the **last letter of the first word** matches the **first letter of the second word**
- Enforce adjacency constraints (no adjacent letters come from the same 3-letter group)

---

## Problem Description

In NYT's *Letter Boxed*, the player is given 12 letters, arranged on the four sides of a square (three letters per side). A valid solution must:

1. Form one or more English words.
2. Only use the provided letters.
3. Avoid using adjacent letters from the same side.
4. Use all the letters at least once.

This implementation attempts to solve a variant of the problem by generating **two-word chains** from the given letters that satisfy the chaining and adjacency rules.

---

## How It Works

1. The user provides four triplets (e.g., `aro`, `seu`, `nti`, `lch`) representing the 12 available letters.
2. The script:
   - Builds all permutations of valid English words from the letters.
   - Filters words such that no two adjacent letters come from the same triplet.
   - Pairs words (`w1`, `w2`) such that `w1[-1] == w2[0]` and all letters from the original input are used across both words.
3. The result is a list of `(word1, word2)` pairs that satisfy all the above constraints.

---

## Sample Input

```python
triplets = ["aro", "seu", "nti", "lch"]
