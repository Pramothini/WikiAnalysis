#i!/usr/bin/python
"""
Date 9/7/14
written by : Pramothini Dhandapany Kanchanamala
cmu id : pdhandap 
"""

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
     This function is used to read the input file, eliminate the restricted lines and
     write the unsorted output to a file named unsorted_restrictedlines.
     Then we read from this unsorted_restrictedlines, sort the file according to the page views and
     write the tab separated output to a file named sorted_restrictedlines.
    """
    output = open("unsorted_restrictedlines.txt","w")
    final_output = open("sorted_restrictedlines.txt","w")
    myfile = open("pagecounts-20140701-000000").readlines()
    input_lines = 0
    output_lines = 0
    input_requests = 0
    for line in myfile:
        input_lines += 1
        linelist = []
        linelist.extend(line.split())
        input_requests += int(linelist[2])
	#to eliminate non - english
	if line[0:3] == 'en ':
	    if not_restricted_words(linelist): #restricted words filter 
                if not linelist[1][0].islower(): #case filter
                    if not_restricted_pics(linelist):#restricted extentions filter
		        if not_boiler_plate_articles(linelist): #restricted articles filter
		            output.write(line)
			    output_lines += 1
    output.close()
    print "Total input lines = ", input_lines
    print "Total output lines before sorting = ", output_lines
    print "Total input request = ", input_requests
    intermediate_file = open("unsorted_restrictedlines.txt").readlines()
    intermediate_file.sort(key=lambda l: float(l.split()[2]),reverse=True)
    print "writing the sorted lines to file sorted_restrictedlines.txt"
    for full_line in intermediate_file:
        final_output.write(full_line.split()[1]+'\t'+full_line.split()[2]+'\n')
    final_output.close()
    print "final output is available at sorted_restrictedlines.txt"

if __name__ == "__main__":
   main()
