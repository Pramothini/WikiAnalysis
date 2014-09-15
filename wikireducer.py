#!/usr/bin/python
"""
Date 9/12/14
written by : Pramothini Dhandapany Kanchanamala
cmu id : pdhandap
"""

import sys

"""
This function is used to print the output
"""

def print_func(dict_of_pgviews,current_article):
     print sum(dict_of_pgviews.itervalues())  , '\t' , current_article , '\t', '2014-07-01:' , dict_of_pgviews[1] ,'\t', '2014-07-02:' , dict_of_pgviews[2] ,'\t' , '2014-07-03:' , dict_of_pgviews[3],'\t'  , '2014-07-04:' , dict_of_pgviews[4] ,'\t', '2014-07-05:' , dict_of_pgviews[5] ,'\t' , '2014-07-06:' , dict_of_pgviews[6],'\t'  , '2014-07-07:' , dict_of_pgviews[7] ,'\t' , '2014-07-08:' , dict_of_pgviews[8] ,'\t' , '2014-07-09:' , dict_of_pgviews[9],'\t'  , '2014-07-10:' , dict_of_pgviews[10],'\t', '2014-07-11:' , dict_of_pgviews[11],'\t' , '2014-07-12:' , dict_of_pgviews[12],'\t','2014-07-013:' ,dict_of_pgviews[13],'\t'  , '2014-07-014:' , dict_of_pgviews[14] ,'\t', '2014-07-15:' , dict_of_pgviews[15] ,'\t' , '2014-07-16:' , dict_of_pgviews[16],'\t'  , '2014-07-17:' , dict_of_pgviews[17] ,'\t' , '2014-07-18:' , dict_of_pgviews[18] ,'\t' , '2014-07-19:' , dict_of_pgviews[19],'\t'  , '2014-07-20:' , dict_of_pgviews[20],'\t', '2014-07-21:' , dict_of_pgviews[21],'\t' , '2014-07-22:' , dict_of_pgviews[22],'\t','2014-07-23:' ,dict_of_pgviews[23],'\t'  , '2014-07-24:' , dict_of_pgviews[24] ,'\t', '2014-07-25:' , dict_of_pgviews[25] ,'\t' , '2014-07-26:' , dict_of_pgviews[26],'\t'  , '2014-07-27:' , dict_of_pgviews[27] ,'\t' , '2014-07-28:' , dict_of_pgviews[28] ,'\t' , '2014-07-29:' , dict_of_pgviews[29],'\t'  , '2014-07-30:' , dict_of_pgviews[30],'\t', '2014-07-31:' , dict_of_pgviews[31],'\t'

def main():
    #print "started wiki_reducer1"
    current_article = None
    current_day = 0
    article = None
    #dict_of_articles = {}
    dict_of_pgviews = {}
    for days in range(1,32):
        dict_of_pgviews[days] = 0
    """
     iterate over each line and get the article name, page view and the day.
    """
    for line in sys.stdin:
        line = line.strip()
        article,pgview,day = line.split('\t')
        try:
            pgview = int(pgview)
            day = int(day)
        except ValueError:
            continue
        """
         if the article name has not changed(i.e, the article is the same as the previous article),add the pageview in the corresponding day
        """
        if current_article == article:
            dict_of_pgviews[day] += pgview
        else:
            # the current article is over and next article has started.
            if current_article:
                # if the total page view of the previous aricle is > 100000, print the article.
                if sum(dict_of_pgviews.itervalues()) > 100000:
                    #dict_of_articles[current_article] = dict_of_pgviews
                    print_func(dict_of_pgviews,current_article) 
            current_article = article
            #clear the page view values of the previous article, so that the pageview of the next article can be stored.
            dict_of_pgviews = {}
	    for days in range(1,32):
    	        dict_of_pgviews[days] = 0
	    dict_of_pgviews[day] = pgview
    #print the last article if its total pageview is > 100000
    if current_article == article:
        if sum(dict_of_pgviews.itervalues()) > 100000:
            print_func(dict_of_pgviews,current_article)
    #print "finished wiki_reducer1"

if __name__ == "__main__":
   main()
