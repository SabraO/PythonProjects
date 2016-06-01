import sys, math
nums = []
for line in sys.stdin:
    if line == "x\n":
        break
    else:
        for word in line.split():
            nums.append(float(word))

nums.reverse()
for num in nums:
   print("%.4f" % math.sqrt(num))