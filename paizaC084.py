campain_str = input()
print(len(campain_str))
for j in range(0,2):
    if j == 1:
            print("+" +campain_str+ "+")
    for i in range(0,len(campain_str)+2):
        print("+", end = "")
    print("")