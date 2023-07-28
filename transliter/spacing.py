import os

def spacing_file(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_rmspace.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line.replace(" ", "")
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def spacing(text):
    result = text.replace(" ", "")
    print(result)