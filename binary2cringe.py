def normal(string):
    val = 0
    for i in range(len(string)):
        val += int(string[i])*(2**(7-i))
    return chr(int(val))
ff = open("output", "w")
with open("output.txt", "r") as f:
    text = f.read()
    for s in text.split():
        nr = normal(s)
        ff.write(str(nr))