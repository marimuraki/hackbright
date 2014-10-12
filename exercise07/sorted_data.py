# Source: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise07

"""
Description
-------
In this directory, you will find a text file, scores.txt, containing a series of local restaurant ratings. Each line looks like this:
    
    Restaurant Name:Rating

Your job is to write a program named 'sorted_data.py' reads the file, then spits out the ratings in alphabetical order by restaurant.

  """

from sys import argv

def create_dict(filetext):

	scores_dict = {}

	for line in filetext:
		stripline = line.strip()
		splitline = stripline.split(':')
		scores_dict[splitline[0]] = int(splitline[1])

	return scores_dict

def print_scores(scores_dict):
	for key in sorted(scores_dict.iterkeys()):
		print "Restaurant '%s' is rated at %d." %(key, scores_dict[key])

def main():

	script, filename = argv

	f = open(filename)
	filetext = f.readlines()

	scores_dict = create_dict(filetext)

	print_scores(scores_dict)

if __name__ == "__main__":
	main()
