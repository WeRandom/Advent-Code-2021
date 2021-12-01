x = 0
num1 = 0
num2 = 0
readnum2 = 2

f = open("nums.txt", "r")
num1 = f.readline(1)

while True:
  num2 = f.readline(readnum2)
  if num2 > num1:
    x += 1
    num1 = num2
    readnum2 += 1
    d = open("num.txt", "a")
    d.write(str(x))
    d.write("\n")
    d.close()
  else:
    num1 = num2
    readnum2 += 1