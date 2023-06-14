import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <filename of a C module>")
    sys.exit(1)

filename = sys.argv[1]

to_remove = ['\r', '\n', '"', "'", "/*", "*/", "%" ]

text = ""
level = 0
next_line_add = False
with open(filename, 'r') as file:
    line_num = 0
    buffer = ''
    for line in file:
        line_num += 1
        buffer += line
        if next_line_add:
            next_line_add = False
            level+=1
        if "{" in line:  next_line_add = True
        if "}" in line:  level-=1
        #print(level, line, end='')
        if level==0: 
           text += buffer
           buffer = ""
           continue
        if ';' in line:
            condensed_line  = buffer
            for x in to_remove:
                condensed_line = condensed_line.replace(x,"")
            if len(condensed_line)>67: condensed_line = condensed_line[:67]+"..."
            bs = buffer.strip()
            if not bs.startswith("else") and not bs.startswith("{") and not bs.startswith("unsigned"):
                num_white_space_at_start = len(buffer) - len(buffer.lstrip())
                white_space_at_start = buffer[:num_white_space_at_start]   #.replace("\t", \\t)
                text += f'{white_space_at_start}printf("About to exec line num {line_num}: {condensed_line}\\n");\n'
            text += buffer
            buffer = ''
text += buffer
print(text)
