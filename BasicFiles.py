g = open("guests.txt", "w")
i_g = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in i_g:
    g.write(i + "\n")

g.close()

with open("guests.txt") as g:
    for i in g:
        print(i)


ng = ["Sam","Danielle","Jacob"]

with open("guests.txt","a") as g:
    for i in ng:
        g.write(i + "\n")


co = ["Andrea","Manuel","Khalid"]
temp = []

with open("guests.txt", "r") as g:
    for i in g:
        temp.append(i.strip()) #strip to remove \n

print(temp)

with open("guests.txt","w") as g:
    for i in temp:
        if i not in co:
            g.write(i+"\n")

with open("guests.txt") as g:
    for i in g:
        print(i)
        
ck = ["Bob","Andrea"]

ci = []

with open("guests.txt") as g:
    for i in g:
        ci.append(i.strip())
    for j in ck:
        if j in ci:
            print(j,"checked in")
        else:
            print(j,"not checked in")

print(ci)
