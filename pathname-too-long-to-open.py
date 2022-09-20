(출처)https://stackoverflow.com/questions/36219317/pathname-too-long-to-open

# below is Python 3 version regarding @Eryk Sun's solution.

import os

def winapi_path(dos_path, encoding=None):
    if (not isinstance(dos_path, str) and encoding is not None): 
        dos_path = dos_path.decode(encoding)
    path = os.path.abspath(dos_path)
    if path.startswith(u"\\\\"):
        return u"\\\\?\\UNC\\" + path[2:]
    return u"\\\\?\\" + path
    
    
>>> path = winapi_path("C:\\Temp\\test.txt")
>>> print path
\\?\C:\Temp\test.txt

  
  
  
