fin = open("form.txt");
loc = {};
for rline in fin:
	line = rline[0:-1];
	while (line[len(line) - 1] == " "):
		line = line[0:-1];
	words = line.split(" ");
	loc[words[0]] = [];
	loc[words[0]].append(float(words[1]));
	loc[words[0]].append(float(words[2]));
	if (len(words) > 3):
		loc[words[3]] =[];
		loc[words[3]].append(float(words[4]));
		loc[words[3]].append(float(words[5]));
fin = open("city.txt", encoding = "utf-8");
fout = open("city-loc.txt", "w");
foutcity = open("hascity.txt", "w", encoding = "utf-8");
cnt = 0;
for rline in fin:
	words = rline[0:-1].split('=');
	if (len(words) == 0):
		continue;
	if (words[0] in loc.keys()):
		line = str(words[1]) + "\t" + str(loc[words[0]][0]) + "\t" + str(loc[words[0]][1]) + '\n';
		fout.write(line);
		foutcity.write(words[0] + '=' + words[1] + '\n');
	else:
		cnt += 1;
print(cnt);