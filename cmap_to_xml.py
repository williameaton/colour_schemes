import sys
from hex import Hexes
# Script to generate an XML file from the command line
# Example: $ python3 cmap_to_xml.py Vibrant_PT
# TODO: Edit cmd line inputs to take in output directory

# Get input args - if 1 then will use Iridescent_PT as example
inargs = sys.argv
nargs = len(inargs)
if nargs==1:
    print('No colourmap entered via cmd line. Using Iridescent_PT as example.')
    cmap = 'Iridescent_PT'
elif nargs==2:
    cmap = inargs[1]
else:
    raise ValueError('Calling hex directly only works ')

# Write:
Hexes().write_to_xml(cmap)

