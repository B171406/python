input_string = input()
l1 = input_string.split(",")

curFolder = None
d1 = {}
result = []
isValidString = "isValid"
for i in l1:
    statement = i.split()
    if statement[0] == "goto":
        curFolder = statement[1]
        d1[curFolder] = {}
    else:
        if d1[curFolder].get(i) is None:
            d1[curFolder][i] = 1
        else:
            d1[curFolder][isValidString] = False

for folder, operations in d1.items():
    if len(operations) > 0 and operations.get(isValidString) is None:
        print(folder)
#goto folderA,create fileA,create fileB,create fileA,goto folderB,goto folderC,create fileA,create fileB,create fileC
#goto folderA,create fileA,create fileB,create fileA,create fileB,goto folderB,goto folderC,create fileA,create fileB,create fileB
# goto folderA,goto folderB,goto folderC,create fileA,create fileB,create fileC



# Time Complexity: O(n * m + k)
# Space Complexity: O(n)