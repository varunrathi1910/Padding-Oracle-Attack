from pador import decr, encr
a = "This statement cleaarly says that I'M A LOSER."
original=encr(a).encode("hex") 
print original
print len(original)

print type(original[1])
print ord(original[1])
print chr(ord(original[1]))
print original[1]
print "chr:",chr(182)
# print original
# print "Original is:",original.encode("base64")
# print "Original is:",original.encode("ASCII")
# print "Original is:",original.encode("utf-8")
# print original.encode("hex")