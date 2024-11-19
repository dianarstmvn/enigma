import string
abc = list(string.ascii_uppercase)

firstLetter = int(input('Шифр первого ротора(число): '))
secondLetter = int(input('Шифр второго ротора(число): '))
thirdLetter = int(input('Шифр третьего ротора(число): '))

inputString = input('Your text: ')
inputString = inputString.upper().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")


def encrypt_word(word):
    '''преобразует буквенную фразу в численную послледовательность'''
    result = []
    for letter in word:
        result.append(abc.index(letter))
    return result

class firstRotor():
    def __init__(self, position):
        self.dictionary = [(0, 4), (1, 10), (2, 12), (3, 5), (4, 11), (5, 6),
                           (6, 3), (7, 16), (8, 21), (9, 25), (10, 13),
                           (11, 19), (12, 14), (13, 22), (14, 24), (15, 7),
                           (16, 23), (17, 20), (18, 18), (19, 15), (20, 0),
                           (21, 8), (22, 1), (23, 17), (24, 2), (25, 9)]
        self.position = (position + 1) % 26
    def work(self, nl):
        ''' ищем соответствие из алфавита в роторе'''
        nl = (nl + self.position) % 26
        for i in range(0, 26):
            if self.dictionary[i][0] == nl:
                result = self.dictionary[i][1]
        return result

    def workwork(self, nl):
        '''ищем соответствие из ротора в алфавите'''
        for key, value in self.dictionary:
            if value == nl:
                result = key
                break
        result = (result - self.position) % 26
        return result

class secondRotor():
    def __init__(self, position):
        self.dictionary = [(0, 0), (1, 9), (2, 3), (3, 10), (4, 18), (5, 8),
                           (6, 17), (7, 20), (8, 23), (9, 1), (10, 11),
                           (11, 7), (12, 22), (13, 19), (14, 12), (15, 2),
                           (16, 16), (17, 6), (18, 25), (19, 13), (20, 15),
                           (21, 24), (22, 5), (23, 21), (24, 14), (25, 4)]
        self.position = (position + 1) % 26

    def work(self, nl):
        ''' ищем соответствие из алфавита в роторе'''
        nl = (nl + (self.position - a.position)) % 26
        for i in range(0, 26):
            if self.dictionary[i][0] == nl:
                result = self.dictionary[i][1]
        return result

    def workwork(self, nl):
        for key, value in self.dictionary:
            if value == nl:
                result = key
                break
        result = (result - (self.position - a.position)) % 26
        return result

class thirdRotor():
    def __init__(self, position):
        self.dictionary = [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9), (5, 11),
                           (6, 2), (7, 15), (8, 17), (9, 19), (10, 23),
                           (11, 21), (12, 25), (13, 13), (14, 24), (15, 4),
                           (16, 8), (17, 22), (18, 6), (19, 0), (20, 10),
                           (21, 12), (22, 20), (23, 18), (24, 16), (25, 14)]
        self.position = position

    def work(self, nl):
        ''' ищем соответствие из алфавита в роторе'''
        nl = (nl + (self.position - b.position)) % 26
        for i in range(0, 26):
            if self.dictionary[i][0] == nl:
                result = self.dictionary[i][1]
        return result

    def workwork(self, nl):
        for key, value in self.dictionary:
            if value == nl:
                result = key
                break
        result = (result - (self.position - b.position)) % 26
        return result

class reflector():
    def __init__(self):
        self.dictionary = [(0, 24), (1, 17), (2, 20), (3, 7), (4, 16), (5, 18),
                           (6, 11), (7, 3), (8, 15), (9, 23), (10, 13),
                           (11, 6), (12, 14), (13, 10), (14, 12), (15, 8),
                           (16, 4), (17, 1), (18, 5), (19, 25), (20, 2),
                           (21, 22), (22, 21), (23, 9), (24, 0), (25, 19)]
    def work(self, nl):
        nl = (nl - c.position) % 26
        for i in range(0, 26):
            if self.dictionary[i][0] == nl:
                result = self.dictionary[i][1]
        result = (result + c.position) % 26
        return result

def encodeEnigma(stringByNumber): #алгоритм кодирования
    encode = list()
    for number in stringByNumber:
        nl = a.work(number)
        nl = b.work(nl)
        nl = c.work(nl)
        nl = ref.work(nl)
        nl = c.workwork(nl)
        nl = b.workwork(nl)
        encode.append(a.workwork(nl))
    return encode

def decodeEnigma(message): #алгорит раскодирования, чтобы сразу проверить
    messageByNumber = encrypt_word(message)
    decode = list()
    for number in messageByNumber:
        nl = a.work(number)
        nl = b.work(nl)
        nl = c.work(nl)
        nl = ref.work(nl)
        nl = c.workwork(nl)
        nl = b.workwork(nl)
        decode.append(a.workwork(nl))
    return decode

def PrintPhrase(stroka): #преобразовывает шифр из численной последовательности в буквенную
    code = ''
    for num in stroka:
        code = code + abc[num]
    return code


a = firstRotor(firstLetter)
b = secondRotor(secondLetter)
c = thirdRotor(thirdLetter)
ref = reflector()

stringByNumber = encrypt_word(inputString)
enigmaByNumber = encodeEnigma(stringByNumber)

message = PrintPhrase(enigmaByNumber) #текстовое зашифрованная фраза
message = decodeEnigma(message) #числовая расшифрованная фраза


print('Исходная фраза числами: ' + ', '.join(map(str, stringByNumber)))
print('Зашифрованная фраза числами: ' + ', '.join(map(str, enigmaByNumber)))

print('Зашифрованная фраза: ' + PrintPhrase(enigmaByNumber))
print('Расшифрованная фраза: ' + PrintPhrase(message))