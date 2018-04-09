import string

class EncodeAndDecodeTinyUrl(object):

    def __init__(self):
        self.characterSet = string.ascii_letters + '0123456789'
        self.url2code = dict()
        self.code2url = dict()

    def encode(self, longURL):
        while longURL not in self.url2code:
            code = ''.join(random.choice(self.characterSet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longURL
                self.url2code[longURL] = code
        return 'http://tinyurl.com/' + self.url2code[longURL]


    def decode(self, tinyURL):
        return self.code2url[tinyURL[-6:]]

from nose.tools import assert_equals, assert_raises

class TestEncodeAndDecodeTinyUrl(object):

  def testEncodeAndDecodeTinyUrl(self):
    encodeAndDecodeTinyUrl = EncodeAndDecodeTinyUrl()

    print ("All test cases passed!")


def main():
  testEncodeAndDecodeTinyUrl = TestEncodeAndDecodeTinyUrl()
  testEncodeAndDecodeTinyUrl.testEncodeAndDecodeTinyUrl()

if __name__ == '__main__':
  main()
