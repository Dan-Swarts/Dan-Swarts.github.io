#
#

s = "  There... are... a... lot ...of: deliminters,,, Ryan?!!!"
p = s

for ch in ".:,?!":
    p = p.replace(ch, "")
p = p.lstrip()

idx = p.find(' ')

my_list = []

while idx != -1:
    my_list.append(p[ : idx])
    p = p[idx: ].lstrip()
    idx = p.find(' ')

print(my_list)
