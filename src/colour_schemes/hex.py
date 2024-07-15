import numpy as np
import sys

###

# PT indictates from https://personal.sron.nl/~pault/

class Hexes():

    def __init__(self):

        self.hex=\
          {'Iridescent_PT':   ['#FEFBE9', '#FCF7D5', '#F5F3C1', '#EAF0B5', '#DDECBF', '#D0E7CA', '#C2E3D2', '#B5DDD8',
                               '#A8D8DC', '#9BD2E1', '#8DCBE4', '#81C4E7', '#7BBCE7', '#7EB2E4', '#88A5DD', '#9398D2',
                               '#9B8AC4', '#9D7DB2', '#9A709E', '#906388', '#805770', '#684957', '#46353A'],
           'Incandescent_PT': ['#CEFFFF', '#C6F7D6', '#A2F49B', '#BBE453', '#D5CE04', '#E7B503', '#F19903', '#F6790B',
                               '#F94902', '#E40515', '#A80003'],
           'Vibrant_PT':      ['#EE7733', '#0077BB', '#33BBEE', '#EE3377', '#CC3311', '#009988', '#BBBBBB'],
           'MedContrast_PT':  ['#FFFFFF', '#EECC66', '#EE99AA', '#6699CC', '#997700', '#994455', '#004488', '#000000'],
           'HighContrast_PT': ['#FFFFFF', '#DDAA33', '#BB5566', '#004488']

           }


    def hex_to_rgb(self, h):
        # Takes in Hex string and converts to RBG
        # Solution from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
        h = h.lstrip('#')
        rbg = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        return rbg


    def write_to_xml(self, cname, outdir='./XMLS/'):

        hex = self.hex[cname]
        nhex = len(hex)

        xpt = np.linspace(0, 1, nhex)

        # Open xml file:
        f = open(outdir + cname+'.xml', 'w')

        f.write("<ColorMaps>\n")
        f.write(f'   <ColorMap name="{cname}" space="RGB">\n')
        for i in range(nhex):
            rgb = np.array(self.hex_to_rgb(hex[i]))/255
            f.write(f'        <Point x="{xpt[i]}" o="1" r="{rgb[0]}" g="{rgb[1]}" b="{rgb[2]}"/>\n')

        f.write("    </ColorMap>\n")
        f.write("</ColorMaps>\n")

        f.close()

        print(f'Written to {outdir + cname}.xml')


