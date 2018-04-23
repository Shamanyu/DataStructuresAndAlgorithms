from collections import defaultdict

class SubdomainVisitCount(object):

    def subdomainVisitCount(self, cpdomains):
        visit = {}
        for pair in cpdomains:
            count, domain = pair.split(" ")   #count and domain, seperated by whitespace

            subs = []
            subs = domain.split(".")          #split the domain

            subs[0] = domain                  #redefine the domains according to question
            index   = domain.find(".")
            subs[1] = domain[index+1:]


            for d in subs:                    #set the count for each domain/subdomain
                if d not in visit:
                    visit[d]  = int(count)
                else:
                    visit[d] += int(count)

        pairs = []                            #create a list of strings from the hashmap
        for s in visit:
            temp = str(visit[s]) + " " + str(s)
            pairs.append(temp)

        return set(pairs)


from nose.tools import assert_equals, assert_raises

class TestSubdomainVisitCount(object):

  def testSubdomainVisitCount(self):
    subdomainVisitCount = SubdomainVisitCount()

    assert_equals(subdomainVisitCount.subdomainVisitCount(["9001 discuss.leetcode.com"]),
        set(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]))

    assert_equals(subdomainVisitCount.subdomainVisitCount(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]),
        set(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]))

    print ("All test cases passed!")


def main():
  testSubdomainVisitCount = TestSubdomainVisitCount()
  testSubdomainVisitCount.testSubdomainVisitCount()

if __name__ == '__main__':
  main()
