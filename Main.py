"""
This is the file where we read data from 4 different web pages using
urllib library and we do it using threads
"""
import urllib
from threading import Thread
from bs4 import BeautifulSoup


def fetch_and_display(url, keys, thread):
    """
    this function is real performer which will get all the data and convert it
    to readable form using beautiful soup and give us matching headings
    according to our keywords
    :param url: page to read data from
    :param keys: keywords that we want to match headings with
    :param thread: page to show from where we got this heading
    """
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # iterating through all the anchor tags (headings)
    for link in soup.find_all('a'):

        # checking headings that have matching keywords as of input
        if any(word.lower() in link.get_text().lower() for word in keys):
            print (link.get_text()) + " [From %s] \n " % thread

if __name__ == "__main__":

    print "Enter Space Separated Keywords To Search"
    KEYWORDS = raw_input('>')
    KEYWORDS = KEYWORDS.split(" ")

    # Making thread objects to read data from multiple links parallel
    REDDIT = Thread(target=fetch_and_display,
                    args=('https://www.reddit.com/r/programming',
                          KEYWORDS, 'Reddit'))
    REDDIT.start()

    YCOMB = Thread(target=fetch_and_display,
                   args=('https://news.ycombinator.com/',
                         KEYWORDS, 'Y Combinator'))
    YCOMB.start()

    GUARDIAN = Thread(target=fetch_and_display,
                      args=('https://www.theguardian.com/us/technology',
                            KEYWORDS, 'Guardian'))
    GUARDIAN.start()

    NYTIMES = Thread(target=fetch_and_display,
                     args=('http://www.nytimes.com/pages/technology/index.html',
                           KEYWORDS, 'NY Times'))
    NYTIMES.start()
