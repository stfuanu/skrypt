with open("/root/sectra/domains/xaa") as file_in:
    lines = []
    for line in file_in:
        line=line.rstrip('\n')
        lines.append(line)

print(lines)