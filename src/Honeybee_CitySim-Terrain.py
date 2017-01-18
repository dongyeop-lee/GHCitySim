# Interface to CitySim Solver
# http://citysim.epfl.ch/
#
# GH-Python component initiated by
# Giuseppe Peronato <giuseppe.peronato@epfl.ch> 
# 

"""
This component imports the geometry and produces the XML chuck for terrain.

-
This component will hopefully be part of
Ladybug: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari

@license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

-

    
    Args:
        T: List of terrain meshes
        R: List (or single value) for SW reflectance; Default = 0.1 
        path: path of project
        name: title of project
        Write: Boolean to start
"""

ghenv.Component.Name = "Honeybee_CitySim-Terrain"
ghenv.Component.NickName = 'CitySim-Terrain'
ghenv.Component.Message = 'VER 0.0.3\nJAN_17_2017'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "14 | CitySim"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

import rhinoscriptsyntax as rs
if len(R) == 0:
    R.append(0.1) #Default
while len(R) < len(T):
    R.append(R[0])

XML = "<GroundSurface>\n"
for m in range(len(T)):
    facevertices = rs.MeshFaceVertices(T[m])
    meshvertices = rs.MeshVertices(T[m])
    for f in range(len(facevertices)):
        XML += '<Ground id="{0}" ShortWaveReflectance="{1}">\n'.format(str(m)+'-'+str(f),R[m])
        for v in range(len(facevertices[f])):
            XML += '<V{0} x ="{1}" y="{2}" z ="{3}"/>\n'.format(v,meshvertices[facevertices[f][v]][0],meshvertices[facevertices[f][v]][1],meshvertices[facevertices[f][v]][2])
        XML += '</Ground>\n'
XML += '</GroundSurface>'


def writeXML(xml, path, name):
    xmlpath = path+name+"_terrain.xml"
    out_file = open(xmlpath,"w")
    out_file.write(xml)
    out_file.close()

if Write:
    writeXML(XML,path,name)
    print "XML file created"
else:
    print "Set Write to true"