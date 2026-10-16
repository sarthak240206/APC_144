import re

print("Enter Python source code. Type END on a new line to finish:")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

source = "\\n".join(lines)
comments = re.findall(r"(?m)^\\s*#.*$", source)
print("Full-line comments:", comments)

print("Note: Regex alone cannot reliably identify every comment because # may occur inside strings.")
