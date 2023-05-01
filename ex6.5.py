text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
spos = text.find("5")
num = text[pos : spos+1]
fnum = float(num)
print(fnum)
