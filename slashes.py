import sys


def execute_code(code):
	mode = 0
	pat = ''
	sub = ''
	tex = ''
	
	while code:
		c, *code = code
		if mode == 0:
			if c == '/':
				mode += 1
			elif c == '\\':
				if code:
					c, *code = code
					print(c, end='')
			else:
				print(c, end='')

		elif mode == 1:
			if c == '/':
				mode += 1
			elif c == '\\':
				if code:
					c, *code = code
					pat += c
			else:
				pat += c

		elif mode == 2:
			if c == '/':
				mode += 1
			elif c == '\\':
				if code:
					c, *code = code
					sub += c
			else:
				sub += c

		elif mode == 3:
			tex += c

	
	if mode == 3:
		while pat in tex:
			idx = tex.index(pat)
			tex = list(tex)
			sub = list(sub)

			tex[idx:idx+len(pat)] = sub
			tex = ''.join(tex)

		if tex:
			execute_code(tex)



def main():
	if len(sys.argv) == 1:
		return
	with open(sys.argv[1]) as file:
		code = '\n'.join(line.rstrip('\n') for line in file)
	execute_code(code)

	

if __name__ == '__main__':
	main()
