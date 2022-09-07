import sys

def to_binary(char):
	return '{0:08b}'.format(ord(char))

def to_whitespace(inp_file, out_file):
    with open(inp_file, 'r') as file:
        lines = file.read().replace('\r','').split('\n')
    lines = [line.strip() for line in lines if line]
    out = []
    for line in lines:
        for char in line:
            out.append(to_binary(char))
        out.append(to_binary("\n"))
    write = ''
    out_str = ''.join(out)
    for a in out_str:
        if a == '0':
            write += " "
        elif a == '1':
            write += "\t"
    with open(out_file, 'w') as f:
	    f.write(write)


def from_whitespace(fileName):
	message = open(fileName, 'r').read()
	bin_val = ""
	dec_msg = ""
	for a in message:
		if a == ' ':
			bin_val += "0"
		elif a == '\t':
			bin_val += "1"

		if len(bin_val) == 8:
			dec_msg += chr(int(bin_val, 2))
			bin_val = ""
	print(dec_msg)


if len(sys.argv) == 2:
	from_whitespace(sys.argv[1])
elif len(sys.argv) == 3:
    to_whitespace(sys.argv[1], sys.argv[2])