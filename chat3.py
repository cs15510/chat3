#讀取檔案
def read_file(filename):
	lines = []
	content = []
	with open(filename,"r", encoding="utf-8-sig") as f:
		for line in f:
			line_cut = line.strip().split(" ")
			time = line_cut[0][:5]
			name = line_cut[0][5:]
			content = " ".join(line_cut[1:])
			lines.append([time, name, content])
	return lines


#寫入檔案
def write_file(filename, lines):
	with open(filename, "w", encoding = "utf-8") as f:
		for line in lines:
			f.write(line[1] + ": " + line[2] + "\n")
		

lines = read_file("3.txt")
write_file("3-2.txt", lines)