with open("artifacts.txt", "r") as f:
    txt = f.read()

with open("artifacts.txt", "w") as f:
    txt = f.write(txt + " added new line...")

print(txt)
print("It is end of stage3..")
