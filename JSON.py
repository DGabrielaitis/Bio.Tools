

#----------Dovydas Gabrielaitis 28 Dec 2018-----------

import json
import urllib2

#----- This fuction calculates the total sum of the citations of the primary publications-----
#----- It returns 'Total_Sum' as the list with the citation count.----------------------------

def sum_primary_citation_counts(biotoolsID):
    url = 'https://bio.tools/api/' + biotoolsID + '?format=json'
    try:
        data = json.load(urllib2.urlopen(url))
        Number_Of_Papers = len(data['publication'])
        Total_Sum = 0
        for i in range(Number_Of_Papers):
            if data['publication'][i]['metadata']== None:
                pass
            else:
                if data['publication'][i]['type'] == 'Primary':
                    CitCount_tool = data['publication'][i]['metadata']['citationCount']
                    Total_Sum += CitCount_tool
        return Total_Sum

    except:
        return None

#----- This fuction returns the latest primary publication------------------------------------


def latest_primary_publication(biotoolsID):
    url = 'https://bio.tools/api/' + biotoolsID + '?format=json'

    #Get the list of the publication dates of the Primary Publications

    try:
        Latest_date = []
        Latest_Publication_Is = []
        data = json.load(urllib2.urlopen(url))
        Number_Of_Papers = len(data['publication'])

        #Iterate through all of the publications
        for i in range(Number_Of_Papers):
            #If no meta data
            if data['publication'][i]['metadata'] == None:
                pass

            #If it has a Primary Publication
            else:

                if data['publication'][i]['type'] == 'Primary':
                    Date_of_paper = data['publication'][i]['metadata']['date']
                    # Add the first publication to the list, if the list is empty
                    if Latest_date == []:
                        Latest_date = Date_of_paper

                    #If it is not the first publication that is being iterated, check if it is not older than the one that is already in the list,
                    elif Date_of_paper >= Latest_date:
                        Latest_date = Date_of_paper

        return Latest_date


    # If the 'biotoolID' does not exist, return None
    except:
        return None



# Note- A lot of publications do not have the 'type'='Primary. Thus for this to function properly, I would suggest changing
#the type of those publications from 'none' to 'primary' :)

# The functions were tested on both 'jaspar' and 'bioconductor'. Personaly, 'clustalw' is the best fopr this testing, because it has two publications, both primary and with dates.
