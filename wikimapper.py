#!/usr/bin/python
"""
Date 9/7/14
written by : Pramothini Dhandapany Kanchanamala
cmu id : pdhandap 
"""

import sys
import os

ext = ['.jpg','.gif','.png','.JPG','.GIF','.PNG','.txt','.ico']
spwrds = ['Media:','Special:','Talk:','User:','User_talk:','Project:','Project_talk:',
          'File:','File_talk:','MediaWiki:','MediaWiki_talk:','Template:','Template_talk:',
          'Help:','Help_talk:','Category:','Category_talk:','Portal:','Wikipedia:','Wikipedia_talk:']
bp_articles = ['404_error/','Main_Page','Hypertext_Transfer_Protocol','Favicon.ico','Search']


def not_restricted_words(linelist):
    """ 
       This function is used to check whether the title starts with any restricted words
       returns 1 when restricted words are not present
       returns 0 when restricted words are present 
    """
    flag = 1
    for wrds in spwrds:
        if linelist[1][0:len(wrds)] != wrds:
            continue
        else:
            flag = 0
            break
    return flag

def not_boiler_plate_articles(linelist):
    """
       This function is used to check whether the title is a boiler plate article
       returns 1 when the title is not a boiler plate article
       returns 0 when title is a boiler plate article
    """
    flag = 1
    for article in bp_articles:
        if linelist[1] != article:
            continue
        else:
            flag = 0
            break
    return flag

def not_restricted_pics(linelist):
    """ 
      This function is used to check whether the title contains any restricted extentions
      returns 1 when restricted extentions are not present
      returns 0 when restricted extentions are present 
    """
    extflag = 1
    for ex in ext:
        if ex != linelist[1][-4:]:
            continue
        else:
            extflag = 0
            break
    return extflag


def main():
    """
     This function is used to read the input file, eliminate the restricted lines
     and write the tab separated output 
    """
    #file_name = os.environ["mapreduce_map_input_file"]
    #file_name = "pagecounts-20140701-000000"
    #day = file_name.split('-')[1][-2:]
    for line in sys.stdin:
        file_name = os.environ["mapreduce_map_input_file"] if os.environ.has_key("mapreduce_map_input_file") else os.environ.get("map_input_file", None)
        if file_name:
            day = file_name.split('-')[1][-2:]
        else:
            continue
        linelist = []
        linelist.extend(line.split())
	#to eliminate non - english
	if line[0:3] == 'en ':
	    if not_restricted_words(linelist): #restricted words filter 
                if not linelist[1][0].islower(): #case filter
                    if not_restricted_pics(linelist):#restricted extentions filter
		        if not_boiler_plate_articles(linelist): #restricted articles filter
			    print line.split()[1],'\t',line.split()[2],'\t',day
  

if __name__ == "__main__":
   main()
