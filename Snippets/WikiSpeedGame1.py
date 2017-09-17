import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def getNextURL(new_url): #Finds the first link/title (broken when it has a country)
    infile = opener.open(new_url)
    page = infile.read()
    #print page
    main_paragraph = page[page.find('<p>'):page.find('<p>')+500] #Find the first <p> tag for the main body
    print main_paragraph
    new_page = main_paragraph[main_paragraph.find('<a href="/wiki/')+15:main_paragraph.find('"',main_paragraph.find('<a href="/wiki/')+15)] #Find the first href for the link
    return new_page

start_page = raw_input('Enter the wikipedia page to start from: ')
start_url = 'http://en.wikipedia.org/w/index.php?title='+start_page
end_page = raw_input('Enter the wikipedia page to get to: ')
end_url = 'http://en.wikipedia.org/w/index.php?title='+end_page

#newURL = 'http://en.wikipedia.org/w/index.php?title=Special:Random' #URL for a random article

current_page = start_page

jumps = 0 #Keeps track of the jumps
    
while current_page != end_page:
    new_url = 'http://en.wikipedia.org/w/index.php?title=' + current_page #Creates the next link to go to based upon the first link
    current_page = getNextURL(new_url)
    print ('Now jumping to the ' + current_page + ' page.')
    jumps +=1

print (jumps) 
