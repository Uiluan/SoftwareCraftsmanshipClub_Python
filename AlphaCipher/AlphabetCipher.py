import string

#TODO: Add deciphering
class AlphabetCipher():
    def __init__(self) -> None:
        self.subTable = self.__initializeSubstitutionTable()

    def SetKeyword(self, keyword):
        self.keyword = keyword

    #TODO: Handle spaces in message
    def EncipherMessage(self, message):
        encodedMessage = ''
        keyword = self.__SetupKeywordForMessage(self.keyword, message)
        for index in range(len(message)):
            messageValue = self.__GetValueForLetter(message[index])
            keywordValue = self.__GetValueForLetter(keyword[index])
            encodedMessage = encodedMessage + self.__EncodeLetter(keywordValue, messageValue)
        return encodedMessage

    # Private helpers
    def __initializeSubstitutionTable(self):
        alphabet = string.ascii_lowercase
        substitutionChart = [[0 for i in range(len(alphabet))] for j in range(len(alphabet))]
        for letter in alphabet:
            location = self.__GetValueForLetter(letter)
            substitutionChart[location] = alphabet[location:] + alphabet[:location]
        return substitutionChart

    def __EncodeLetter(self, keyValue, messageValue):
        return self.subTable[keyValue][messageValue]

    def __GetValueForLetter(self, letter):
        letter = letter.lower()
        return ord(letter)-97

    def __SetupKeywordForMessage(self, keyword, message):
        while(len(keyword) < len(message)):
            keyword = keyword + keyword
        return keyword[0:len(message)]