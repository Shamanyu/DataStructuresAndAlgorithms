import urllib2
import re
from random import randint
import webbrowser
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def getNextPage(current_url): #Finds the first link/title (broken when it has a country)
    infile = opener.open(current_url)
    page_data = infile.read()
    wiki_links_positions_temp = [link.start() for link in re.finditer('<a href="/wiki/', page_data)]
    wiki_links_positions = [link+15 for link in wiki_links_positions_temp]
    next_random_page_link_position = wiki_links_positions[randint(0, len(wiki_links_positions)-1)]
    next_page = page_data[next_random_page_link_position:len(page_data)].split('"')[0]
    return next_page

start_page = raw_input('Enter the wikipedia page to start from: ')
start_url = 'http://en.wikipedia.org/w/index.php?title='+start_page
end_page = raw_input('Enter the wikipedia page to get to: ')
end_url = 'http://en.wikipedia.org/w/index.php?title='+end_page

#newURL = 'http://en.wikipedia.org/w/index.php?title=Special:Random' #URL for a random article

current_page = next_page = start_page

jumps = -1
    
while current_page != end_page:
    jumps += 1
    print('At page ' + next_page + ' presently.')
    url = 'http://en.wikipedia.org/w/index.php?title=' + current_page
    webbrowser.open_new_tab(url)
    next_page = getNextPage(url)
    if current_page == next_page:
    	print "Help! Stuck at "+current_page
	break
    else:
        current_page = next_page

if current_page == end_page:
    print "Yay! Goal reached in " + jumps + " jumps"
