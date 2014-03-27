import os
import re

def identify_by_filename(rom_filename):
    """
    Removes standard GoodTools naming convention tags.
    """

    #Remove the extension before passing in regex
    rom_name = os.path.splitext(rom_filename)[0]
    #Remove anything in brackets, parentheses
    return re.search(r'(\([^]]*\))*(\[[^]]*\])*([\w\.\-\s]+)', rom_name).group(3)