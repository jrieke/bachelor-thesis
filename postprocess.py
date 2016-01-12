# Do some custom postprocessing on the tex file

import re
import sys

filename = sys.argv[1]

with open(filename, 'r+') as f:
	print "Postprocessing {0}...".format(filename), 
	text = f.read()
	new_text = re.sub('caption\{\{\[}(.*?)\{\]\}', r'caption[\1]{\1', text, flags=re.DOTALL)  # set short figure captions
	f.seek(0)
	f.write(new_text)
	f.truncate()
	print "Done"