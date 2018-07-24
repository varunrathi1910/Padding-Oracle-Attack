from pador import encr, decr
import os
# from ciphertextgenerator import original
# from padOrdefinition import padOr
# padOr() definition
def padOr(block2,intermediateblocks,blocksize):
  blockcountreducer=1 #Value increases till 16.used i looping as well as XORing values to intermediate bytes
  intermediatebits=[] #Place holder for intermediate bits
  for i in range(blocksize):
    intermediatebits.append("ValueNotFound")

  for z in range(blocksize):
    prefix ="B"*(blocksize-blockcountreducer) #Arbitrary text eg: 15 Bs for last value, 14 for second last and so on....
    suffix="" 

    # Hardcoding the values in the ciphertext for which the intermediate bytes have already been found out.
    for i in range(len(intermediatebits)):
      if intermediatebits[i]=="ValueNotFound":
        continue
      suffix+=chr(intermediatebits[i]^blockcountreducer)
    # ####################################################################

    # Appending the ciphertext for which intermediate bytes have to be found out
    suffix+=block2
    # ##########################################################################

    # Finding the intermediate byte .
    for i in range(256):
      mod = prefix + chr(i) +suffix 
      if decr(mod) != "PADDING ERROR":
        intermediatebits[blocksize-blockcountreducer]=(i^blockcountreducer)
    # ###############################################################

    # Increasing the count of blockcount reducer to move over the next byte
    blockcountreducer+=1
    # ###################################################################
  print intermediatebits
  # Appending the obtained results in the intermediate blocks
  intermediateblocks.append(intermediatebits)
  # #######################################################

  return

  #######################################################
original1=raw_input('Enter the cipher text:\n')
original=""
for i in xrange(0,len(original1),2):
  original=original+chr(int((original1[i]+original1[i+1]),16))
blocksize=int(raw_input('Enter the block size:\n'))
print "What do you want to do ?\n1-Know the plain text\n2-Generate a new ciphertext\n"
choice=int(raw_input())
blocks=[];intermediateblocks=[]
j=0;k=blocksize
lim=len(original)/blocksize
# Converting the cipher into blocks
for i in range(lim):
  blocks.append(original[j:k])
  j+=blocksize
  k+=blocksize
print "The intermediate bytes of all the blocks(in order from block 1 to block 6  ) are:\n"
# ########################################################################################
# Calculating intermediates
for i in range(lim):
  padOr(blocks[i],intermediateblocks,blocksize)
# ##########################################
# Data in character format.
if(choice==1):
  print "\nPrinting the plaintext of each block(except the first one) in character format.\n A new line represents a new block.\n"
  for i in range(1,lim):
    for j in range(blocksize):
      print chr(ord(blocks[i-1][j])^intermediateblocks[i][j]),
    print "\n"
  ############################################################
  # Data in ASCII format
  print "\nData in ASCII format.\n"
  for i in range(1,lim):
    for j in range(blocksize):
      print (ord(blocks[i-1][j])^intermediateblocks[i][j]),
    print "\n"
  ############################################################
  #Data in Hex format
  print "\nData in HEX format.\n "
  for i in range(1,lim):
    for j in range(blocksize):
      print chr(ord(blocks[i-1][j])^intermediateblocks[i][j]).encode("hex"),
    print "\n"
  ############################################################
elif(choice==2):
  # Taking the plaintext and converting it into hex
  plaintext=raw_input("Enter the plaintext that is to be encrypted:\n").encode("hex")
  originalplaintext=""
  for i in xrange(0,len(plaintext),2):
    originalplaintext=originalplaintext+chr(int((plaintext[i]+plaintext[i+1]),16)) 
  # #################################################################
  # Padding the text
  padbytes = blocksize - len(originalplaintext) % blocksize
  pad = padbytes * chr(padbytes)
  originalplaintext+=pad 
  # #################################
  # Converting text to blocks
  lim=len(originalplaintext)/16  
  originalplaintextblock=[]
  j=0;k=blocksize
  for i in range(lim):
    originalplaintextblock.append(originalplaintext[j:k])
    j+=blocksize
    k+=blocksize
############################################################
# Finding original plaintext intermediate bytes
  originalplaintextintermediateblock=[]
  blocktobeappended=intermediateblocks[-1]
  originalplaintextintermediateblock.append(blocktobeappended)
  count=len(originalplaintextblock)-1

  for i in range(lim):
    originalplaintextblock2=""
    for j in range(blocksize):
      originalplaintextblock2+=chr(ord(originalplaintextblock[count][j])^originalplaintextintermediateblock[i][j])    
    padOr(originalplaintextblock2,originalplaintextintermediateblock,blocksize)
    count-=1
  originalplaintextintermediateblock.reverse()
# ############################################################
# new intermediateblocks and new plain text
  newintermediateblocks=[]
  newplaintext=[]
  for i in range(lim+1):
    for j in range(blocksize):
      newintermediateblocks.append(originalplaintextintermediateblock[i][j])
  for i in range(lim):
    for j in range(blocksize):
      newplaintext.append(originalplaintextblock[i][j])
################################################################
# Declaring the new ciphertext string
  newciphertext=""
# ####################################
# Creating the new ciphertext by the formula C[i]=P[i]^I[blocksize+i]
  for i in range(len(originalplaintext)):
    newciphertext+=chr(ord(newplaintext[i])^newintermediateblocks[blocksize+i])
# ###################################################################
# Appending the last 16 bytes from the original ciphertext
  newciphertext+=blocks[-1]
# #######################################################
# Display the ciphertext
  print newciphertext.encode("hex")
else:
  print "Invalid choice"