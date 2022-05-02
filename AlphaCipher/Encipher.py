from AlphabetCipher import *

cipher = AlphabetCipher()

#TODO Have test take user input
# Test 1
keyword = 'scones'
message = 'meetmebythetree'
cipher.SetKeyword(keyword)
encodedMessage = cipher.EncipherMessage(message)

print("Test 1")
print("Keyword: " + keyword)
print("Message: " + message)
print("Encoded Message: " + encodedMessage)


# Test 2
keyword = 'scones'
message = 'testencipheringthismessage'
cipher.SetKeyword(keyword)
encodedMessage = cipher.EncipherMessage(message)

print("Test 2")
print("Keyword: " + keyword)
print("Message: " + message)
print("Encoded Message: " + encodedMessage)

# Test 3
keyword = 'cleancode'
message = 'testencipheringthismessage'
cipher.SetKeyword(keyword)
encodedMessage = cipher.EncipherMessage(message)

print("Test 3")
print("Keyword: " + keyword)
print("Message: " + message)
print("Encoded Message: " + encodedMessage)