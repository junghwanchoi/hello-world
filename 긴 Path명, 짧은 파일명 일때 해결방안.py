
# (출처) https://www.daniweb.com/programming/software-development/threads/124812/long-paths-file-names-ext-s

# You probably syntaxed the the file incorrectly :P
# Copy and paste the full directory name, replacing my string. Then simply add a forward slash to escape the ones already there!

import os

filepath = "C:\\Documents and Settings\\Username\\Desktop\\coolapps\\pythonprograms\\zomglongfilename.file"

info = os.path.split(filepath)

os.chdir(info[0])  # change directory 

print os.path.getsize(info[-1])



