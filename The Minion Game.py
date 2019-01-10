def minion_game(String):
    kevin_score = stuart_score = 0
    for i in range(len(s)):
        if String[i] in 'AEIOU':
            kevin_score += len(s) - i
        else:
            stuart_score += len(s) - i

    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
# Though Computationally Heavy Highly Accurate
import re
def subStrings(String):
	return set([String[i:j+1] for i in range(len(String)) for j in range(i, len(String))])


def occurences(sub, String):
	search = "(?=" + sub +")"
	return len([occ.start() for occ in re.finditer(search, String)])

def score(sub_strings, String):
	score = 0
	for i in sub_strings: score += occurences(i, String)
	return score

def minion_game(String):
    kevin = [sub for sub in subStrings(String) if sub[0] in 'AEIOU']
    stuart = [sub for sub in subStrings(String) if sub[0] not in 'AEIOU']
    kevin_score = score(kevin, String)
    stuart_score = score(stuart, String)
    if stuart_score > kevin_score: print("Stuart {}".format(stuart_score))
    elif kevin_score > stuart_score: print("Kevin {}".format(kevin_score))
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
"""
