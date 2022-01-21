
import ast
from itertools import product
from tabnanny import check
import re


def replace_num(s, start, end, newnum):
	return s[:start] + str(newnum) + s[end:]

def add_num(s, start, end, toadd):
	other = int(s[start:end])
	return replace_num(s, start, end, other + toadd)

def explode(fish):
	depth = 0
	s = re.sub(' ', '', str(fish))
	#print(s)
	for i, c in enumerate(s):
		if c == '[':
			depth += 1
			if depth == 5:
				for j in range(i + 1, len(s)):
					if not s[j].isdigit():
						#print(i, j, s[j], s[j+1])
						assert s[j] == ','
						assert s[j + 1].isdigit()
						break

				for k in range(j + 1, len(s)):
					if not s[k].isdigit():
						# print(i, j, s[j], s[i:])
						assert s[k] == ']'
						break

				a = int(s[i + 1:j])
				b = int(s[j + 1:k])
				# print(a, b)

				# replace pair with 0
				# eprint('      ', s)
				s = replace_num(s, i, k + 1, 0)
				# eprint('ab->0 ', s)

				# go left
				for j in range(i - 1, -1, -1):
					if s[j].isdigit():
						break

				if j != 0: # left number found
					for k in range(j - 1, -1, -1):
						if not s[k].isdigit():
							break

					# eprint(k, j, s[k:j])
					s = add_num(s, k + 1, j + 1, a)
					# eprint('left+ ', s)

				# go right
				for j in range(i + 2, len(s)):
					if s[j].isdigit():
						break

				if j != len(s) - 1: # right number found
					for k in range(j + 1, len(s)):
						if not s[k].isdigit():
							break

					# eprint(j, k, s[j:k])
					s = add_num(s, j, k, b)
					# eprint('right+', s)

				return s, True

		elif c == ']':
			depth -= 1

	return s, False

def split(fish):
	s = fish
	for i, c in enumerate(s):
		if not c.isdigit():
			continue

		for j in range(i + 1, len(s)):
			if not s[j].isdigit():
				break

		n = int(s[i:j])
		if n >= 10:
			a = n // 2
			b = n - a

			s = replace_num(s, i, j, '[{},{}]'.format(a,b))
			return s, True

	return s, False

            
def convert_to_list(fish):
    list_fish = []
    list_fish =ast.literal_eval(fish)
    return list_fish

def snail_addition(first,second):
    return [first, second]   

def check_height(fish): 
    if type(fish) == list:
        return 1 + max(check_height(fish[0]),check_height(fish[1]))
    return 0 

def check_bigger(fish): 
    if type(fish) == list:
        return max(check_bigger(fish[0]),check_bigger(fish[1]))
    return fish 

def check_rules(fish):
    if  check_height(fish) > 4 or check_bigger(fish) >=10:
        return True
    return False

def calculate_magnitude(fish):
	if type(fish) is int:
		return fish

	left, right = fish
	return 3 * calculate_magnitude(left) + 2 * calculate_magnitude(right)

def clean_up(fish):
	while(check_rules(fish)):
		fish, performed =explode(fish)
		if performed:
			continue
		#fish = convert_to_list(fish)
		fish, _ = split(fish)
		fish = convert_to_list(fish)
	return fish 

def calculate(a,b):
    res = convert_to_list(a)
    res = snail_addition(res,convert_to_list(b))
    res = clean_up(res)
    return calculate_magnitude(res)

if __name__ == "__main__":
    file = open("input18.txt", "r")
    all_fish = file.read().split()
    res = convert_to_list(all_fish[0])
    print(check_height(res))
    for fish in all_fish[1:]:
        res = snail_addition(res,convert_to_list(fish))
        res = clean_up(res)
        #print(res)
    print(calculate_magnitude(res))

    best = 0
    for a, b in product(all_fish, all_fish):
        if a is b:
            continue
        m = calculate(a,b)
        if m > best:
            best = m

        m = calculate(a,b)
        if m > best:
            best = m
    
    print(best)
