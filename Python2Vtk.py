import numpy as np
# This .py is a package to handle .vtk files in python without the need of ITK package
# So far the following functions are implemented:
# WritePython2Vtk: write .vtk files in python

def WritePython2Vtk(filename, vertices, faces, normal, scalar, name_of_scalar=None):
    #save the mesh into vtk ascii file
    #Syntax:
    
    #[]=WritePython2Vtk(FILENAME, VERTICES, FACES, NORMAL,SCALAR,NAME_OF_SCALAR)
    
    # Vertices (nbr of vertices * nbr of dimention)
    # Faces    (nbr of faces * 3)
    # Normals  (nbr of vertices * 3)
    # scalar   (nbr of vertices*1)
    # name_of_scalar (string) 
    
    #Created by Brahim Belaoucha on 2014/02/01
    #Copyright (c) Brahim Belaoucha. All right reserved


    if not name_of_scalar:
        name_of_scalar = 'Scalar'
    npoints, nbr_dimension=np.shape(vertices)
    nbr_faces=np.shape(faces)[0]
    f = open(filename,'w')
    f.write('# vtk DataFile Version 2.0\n')
    L='File '+filename
    f.write(L+'\n')
    f.write('ASCII\n')
    f.write('DATASET POLYDATA\n')
    L='POINTS '+str(npoints)+" float"
    f.write(L+'\n')
    for i in range(npoints): # write point coordinates
        point=vertices[i,:]
        L=' '.join(str('%.7f' %x) for x in point)
        f.write(L+'\n')
    f.write(' POLYGONS '+str(nbr_faces)+' '+str(nbr_faces*4)+'\n')
    for i in range(nbr_faces): # write faces
        face=faces[i,:]
        f.write(str(3)+" "+str(face[0]-1)+' '+str(face[1]-1)+' '+str(face[2]-1)+'\n')
    f.write(' CELL_DATA '+str(nbr_faces)+'\n')
    f.write('POINT_DATA '+str(npoints)+'\n')
    f.write('SCALARS '+name_of_scalar+' float 1\n')
    f.write('LOOKUP_TABLE default\n')
    for i in range(npoints):
        f.write(str(scalar[i])+'\n')
    f.write(' NORMALS normals float\n')
    for i in range(npoints):
        f.write(" "+str('%.4f' %normal[i,0])+' '+str('%.4f' %normal[i,1])+' '+str('%.4f' %normal[i,2]))
    f.close()