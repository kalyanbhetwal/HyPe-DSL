import iegenlib
import gc  
import inspect 
from pprint import pprint
#gc.disable()


parflowio = iegenlib.Computation()
parflowio.addDataSpace("nsg", "int")
parflowio.addDataSpace("x", "int")
parflowio.addDataSpace("y", "int")
parflowio.addDataSpace("z", "int")
parflowio.addDataSpace("nx", "int")
parflowio.addDataSpace("ny", "int")
parflowio.addDataSpace("nz", "int")
parflowio.addDataSpace("rx", "int")
parflowio.addDataSpace("ry", "int")
parflowio.addDataSpace("rz", "int")
parflowio.addDataSpace("errcheck", "int")
parflowio.addDataSpace("x_overlap", "int")
parflowio.addDataSpace("clip_x", "int")
parflowio.addDataSpace("extent_x", "int")
parflowio.addDataSpace("qq", "int")
parflowio.addDataSpace("tmp", "uint64_t")
parflowio.addDataSpace("buf", "uint64_t*")

parflowio.addDataSpace("m_p", "int")
parflowio.addDataSpace("m_q", "int")
parflowio.addDataSpace("m_r", "int")
parflowio.addDataSpace("fp", "FILE*")
parflowio.addDataSpace("m_X", "double")
parflowio.addDataSpace("m_Y", "double")
parflowio.addDataSpace("m_Z", "double")
parflowio.addDataSpace("m_nx","uint64_t")
parflowio.addDataSpace("m_ny", "uint64_t")
parflowio.addDataSpace("m_nz", "int")
parflowio.addDataSpace("m_dX", "double")
parflowio.addDataSpace("m_dY", "double")
parflowio.addDataSpace("m_dZ", "double")
parflowio.addDataSpace("m_numSubgrids", "double")
parflowio.addDataSpace("max_x_extent", "int")
parflowio.addDataSpace("byte_offsets", "long*")
parflowio.addDataSpace("sg_count", "long long")
parflowio.addDataSpace("x_extent", "int")
parflowio.addDataSpace("m_fp", "FILE*")
parflowio.addDataSpace("m_data", "double*")

parflowio.addDataSpace("mean", "double*")
parflowio.addDataSpace("sum", "double")

parflowio.addDataSpace("_offsets", "long*")

#parflowio.addDataSpace("writeBuf", "double*")
parflowio.addDataSpace("read_count", "double")
parflowio.addDataSpace("index", "long long")

parflowio.addDataSpace("iz_min", "long long")
parflowio.addDataSpace("iz_max", "long long")
parflowio.addDataSpace("iy_min ", "long long")
parflowio.addDataSpace("iy_max", "long long")

def readFile(fileName):
    dataReads0 = iegenlib.PairVector([])
    dataWrites0 =  iegenlib.PairVector([("m_fp","{[0]->[0]}")])


    s0 = iegenlib.Stmt("m_fp = fopen( m_filename.c_str(), \"rb\");",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads0,
                        dataWrites0)
    parflowio.addStmt(s0);  

    dataReads1 = iegenlib.PairVector([])
    dataWrites1 =  iegenlib.PairVector([("m_X","{[0]->[0]}"),\
                                        ("m_Y","{[0]->[0]}"),\
                                        ("m_Z","{[0]->[0]}"),\
                                        ("m_nx","{[0]->[0]}"),\
                                        ("m_ny","{[0]->[0]}"),\
                                        ("m_nz","{[0]->[0]}"),\
                                        ("m_dX","{[0]->[0]}"),\
                                        ("m_dY","{[0]->[0]}"),\
                                        ("m_dZ","{[0]->[0]}"),\
                                       ("m_numSubgrids","{[0]->[0]}")])

    s1 = iegenlib.Stmt("READDOUBLE(m_X,m_fp,errcheck);    READDOUBLE(m_Y,m_fp,errcheck);    READDOUBLE(m_Z,m_fp,errcheck);    READINT(m_nx,m_fp,errcheck);    READINT(m_ny,m_fp,errcheck);    READINT(m_nz,m_fp,errcheck);    READDOUBLE(m_dX,m_fp,errcheck);    READDOUBLE(m_dY,m_fp,errcheck);    READDOUBLE(m_dZ,m_fp,errcheck);    READINT(m_numSubgrids,m_fp,errcheck);",
                        "{[0]}",
                        "{[0]->[1]}",
                        dataReads1,
                        dataWrites1      
                            )

    parflowio.addStmt(s1)


    dataReads2 =  iegenlib.PairVector([ ("m_nx","{[0]->[0]}"),\
                                        ("m_ny","{[0]->[0]}"),\
                                        ("m_nz","{[0]->[0]}")])
    dataWrites2 = iegenlib.PairVector([("m_data","{[0]->[0]}")])



    s2 = iegenlib.Stmt("m_data = (double*)malloc(sizeof(double)*m_nx*m_ny*m_nz);",
                        "{[0]}",
                        "{[0]->[2]}",
                        dataReads2,
                        dataWrites2)
    parflowio.addStmt(s2)


    dataReads3 = iegenlib.PairVector([("m_numSubgrids","{[nsg]->[0]}")])
    dataWrites3 =  iegenlib.PairVector([("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                        ("z" ,"{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                        ("nz","{[nsg]->[0]}"),\
                                        ("rx","{[nsg]->[0]}"),\
                                        ("ry","{[nsg]->[0]}"),\
                                         ("rz","{[nsg]->[0]}")])

    s3 = iegenlib.Stmt("READINT(x,m_fp,errcheck);READINT(y,m_fp,errcheck);READINT(z,m_fp,errcheck);READINT(nx,m_fp,errcheck);READINT(ny,m_fp,errcheck);READINT(nz,m_fp,errcheck);READINT(rx,m_fp,errcheck);READINT(ry,m_fp,errcheck);READINT(rz,m_fp,errcheck);",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[nsg]->[3,nsg,0]}",
                        dataReads3,
                        dataWrites3)
    parflowio.addStmt(s3)  


    dataReads4 = iegenlib.PairVector([("qq" ,"{[nsg]->[0]}")])
    dataWrites4 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                         ("z","{[nsg]->[0]}")])


    s4 = iegenlib.Stmt("qq = z*m_nx*m_ny + y*m_nx + x;",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[nsg]->[3,nsg,1]}",
                        dataReads4,
                        dataWrites4)
    parflowio.addStmt(s4)  

    dataReads5 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                         ("nz","{[nsg]->[0]}"),\
                                        ("m_data","{[nsg,k,i]->[0]}"),\
                                        ("qq","{[nsg,k,i]->[0]}")])

    dataWrites5 = iegenlib.PairVector([("m_fp", "{[nsg] -> [0]}"),\
                ("buf", "{[nsg,k,i] -> [0]}"),\
                ("index", "{[nsg,k,i] -> [0]}")])
                
    s5 = iegenlib.Stmt("index = qq+k*m_nx*m_ny+i*m_nx; buf = (uint64_t*)&(m_data[index]);read_count = fread(buf,8,nx,m_fp);",
                        "{[nsg,k,i] : 0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids}",
                        "{[nsg,k,i]->[3, nsg,2, k, 0,i,0]}",
                        dataReads5,
                        dataWrites5)
    parflowio.addStmt(s5) 
    
    dataReads6 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("buf","{[nsg,k,i]->[0]}"),\
                                        ("nx","{[nsg,k,i,j]->[0]}"),\
                                        ("ny","{[nsg,k,i,j]->[0]}"),\
                                         ("nz","{[nsg,k,i,j]->[0]}"),\
                                        ("index","{[nsg,k,i,j]->[0]}")])

    dataWrites6 = iegenlib.PairVector([ ("tmp", "{[nsg,k,i,j] -> [0]}"),\
                                        ("m_data", "{[nsg,k,i,j] -> [0]}")])


    s6 = iegenlib.Stmt("tmp = buf[j];  tmp = bswap64(tmp);  m_data[index+j] = *(double*)(&tmp);",
                        "{[nsg,k,i,j] :0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids && 0<=j<nx }",
                        "{[nsg,k,i,j]->[3, nsg,2, k, 0,i,1,j,0]}",
                        dataReads6,
                        dataWrites6)
    parflowio.addStmt(s6)  
    return parflowio
    #print(parflowio.codeGenMemoryManagementString())
    #print(parflowio.codeGen())


def compute_mean():
    parflowio_mean = iegenlib.Computation()

    dataReads1 =  iegenlib.PairVector([])
    dataWrites1 = iegenlib.PairVector([("mean","{[0]->[0]}")])

    s1 = iegenlib.Stmt("mean = (double*)malloc(sizeof(double)*m_ny*m_nx);",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads1,
                        dataWrites1)
    parflowio_mean.addStmt(s1)

    dataReads3 =  iegenlib.PairVector([])
    dataWrites3 = iegenlib.PairVector([("mean","{[x,y]->[x,y]}")])

    # s3 = iegenlib.Stmt("mean=0;",
    #                     "{[y,x]:0<=y<m_ny && 0<=x<m_nx}",
    #                     "{[y,x]->[0,y,0,x,0]}",
    #                     dataReads3,
    #                     dataWrites3)
    # parflowio_mean.addStmt(s3)

    s3 = iegenlib.Stmt("mean[x+m_nx*y] = 0;",
                        "{[x,y]:0<=y<m_ny && 0<=x<m_nx}",
                        "{[x,y]->[0,x,0,y,1]}",
                        dataReads3,
                        dataWrites3)
    parflowio_mean.addStmt(s3)


    dataReads4 =  iegenlib.PairVector([("m_data","{[x,y,z]->[z,y,x]}")])
    dataWrites4 = iegenlib.PairVector([("mean","{[x,y,z]->[x,y]}")])

    s4 = iegenlib.Stmt("mean[x+m_nx*(y)]+=m_data[(long long)(z)*m_ny*m_nx+(y)*m_nx+x];",
                        "{[x,y,z]:0<=y<m_ny && 0<=x<m_nx && 0<=z<m_nz}",
                        "{[x,y,z]->[0,x,0,y,1,z,0]}",
                        dataReads4,
                        dataWrites4)
    parflowio_mean.addStmt(s4)

    dataReads5 =  iegenlib.PairVector([("mean","{[y,x]->[y,x]}")])
    dataWrites5 = iegenlib.PairVector([("mean","{[y,x]->[y,x]}")])

    s5 = iegenlib.Stmt("mean[x+m_nx*(y)] = mean[x+m_nx*(y)]/m_nz;",
                        "{[x,y]:0<=y<m_ny && 0<=x<m_nx}",
                        "{[x,y]->[0,x,0,y,2]}",
                        dataReads5,
                        dataWrites5)
    parflowio_mean.addStmt(s5)

    return parflowio_mean


def writeFile(filename):
    parflowio_write = iegenlib.Computation()

    dataReads1 =  iegenlib.PairVector([("mean","{[0]->[0]}")])
    dataWrites1 = iegenlib.PairVector([("byte_offsets","{[0]->[0]}"),
                                        ("m_data","{[0]->[0]}")])

    s1 = iegenlib.Stmt("m_data = mean;m_p=1;m_q=1;m_r=1;byte_offsets =(long*)malloc(sizeof(long)* ((m_p*m_q*m_r) + 1));m_nz=1;",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads1,
                        dataWrites1)
    parflowio_write.addStmt(s1)

    dataReads2 = iegenlib.PairVector([])
    dataWrites2 =  iegenlib.PairVector([("fp","{[0]->[0]}")])

    s2 = iegenlib.Stmt("fp = std::fopen(filename.c_str(), \"wb\");",
                        "{[0]}",
                        "{[0]->[1]}",
                        dataReads2,
                        dataWrites2)
    parflowio_write.addStmt(s2) 

    dataReads3 =  iegenlib.PairVector([("fp","{[0]->[0]}"),\
                                    ("m_p", "{[0]->[0]}"),\
                                    ("m_q", "{[0]->[0]}"),\
                                    ("m_r", "{[0]->[0]}"),\
                                    ("m_X", "{[0]->[0]}"),\
                                    ("m_Y", "{[0]->[0]}"),\
                                    ("m_Z", "{[0]->[0]}"),\
                                    ("m_nx", "{[0]->[0]}"),\
                                    ("m_ny", "{[0]->[0]}"),\
                                    ("m_nz", "{[0]->[0]}"),\
                                    ("m_dX", "{[0]->[0]}"),\
                                    ("m_dY", "{[0]->[0]}"),\
                                    ("m_dZ", "{[0]->[0]}"),\
                                    ("m_numSubgrids", "{[0]->[0]}")\
                                     ])
    dataWrites3 = iegenlib.PairVector([("m_numSubgrids", "{[0]->[0]}"),\
                    ("max_x_extent", "{[0]->[0]}"),\
                    ("fp", "{[0]->[0]}")])

    s3 = iegenlib.Stmt("m_numSubgrids = m_p * m_q * m_r;    WRITEDOUBLE(m_X,fp);    WRITEDOUBLE(m_Y,fp);    WRITEDOUBLE(m_Z,fp);    WRITEINT(m_nx,fp);    WRITEINT(m_ny,fp);    WRITEINT(m_nz,fp);    WRITEDOUBLE(m_dX,fp);    WRITEDOUBLE(m_dY,fp);    WRITEDOUBLE(m_dZ,fp);    WRITEINT(m_numSubgrids,fp);max_x_extent =calcExtent(m_nx,m_p,0);",
                        "{[0]}",
                        "{[0]->[2]}",
                        dataReads3,
                        dataWrites3)
    parflowio_write.addStmt(s3)
 
    dataReads4 = iegenlib.PairVector([("max_x_extent","{[0]->[0]}")]) 
    dataWrites4 =  iegenlib.PairVector([("writeBuf","{[0]->[0]}")])

    s4 = iegenlib.Stmt(" std::vector<double> writeBuf(max_x_extent);",
                        "{[0]}",
                        "{[0]->[3]}",
                        dataReads4,
                        dataWrites4)
    parflowio_write.addStmt(s4)

    # nsg=0; byte_offsets[0] = 0;sg_count = 1;
 
    dataReads5 = iegenlib.PairVector([("nsg","{[0]->[0]}"),\
                                    ("byte_offsets","{[0]->[0]}"),\
                                     ("sg_count","{[0]->[0]}")]) 
    dataWrites5 =  iegenlib.PairVector([("writeBuf","{[0]->[0]}")])

    s5 = iegenlib.Stmt("nsg=0; byte_offsets[0] = 0;sg_count = 1;",
                        "{[0]}",
                        "{[0]->[4]}",
                        dataReads5,
                        dataWrites5)
    parflowio_write.addStmt(s5)

 
    dataReads6 = iegenlib.PairVector([("m_X", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_Y", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_Z", "{[nsg_z, nsg_y, nsg_x]->[0]}"),
                                   ("m_nx", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_p", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_x", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_ny", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_q", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_y", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_nz", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_r", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_z", "{[nsg_z, nsg_y, nsg_x]->[0]}")
                                   ]) 
    dataWrites6 =  iegenlib.PairVector([("fp", "{[nsg_z, nsg_y, nsg_x]->[0]}")])

    s6 = iegenlib.Stmt("x = m_X + calcOffset(m_nx,m_p,nsg_x);y = m_Y + calcOffset(m_ny,m_q,nsg_y);z = m_Z + calcOffset(m_nz,m_r,nsg_z);WRITEINT(x, fp);WRITEINT(y, fp);WRITEINT(z, fp);x_extent =calcExtent(m_nx,m_p,nsg_x);WRITEINT(x_extent, fp);WRITEINT(calcExtent(m_ny,m_q,nsg_y), fp);WRITEINT(calcExtent(m_nz,m_r,nsg_z), fp);WRITEINT(1, fp);WRITEINT(1, fp);WRITEINT(1, fp);",
                        "{[nsg_z, nsg_y, nsg_x]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  }",
                        "{[nsg_z, nsg_y, nsg_x]->[5,nsg_z,0,nsg_y,0,nsg_x,0]}",
                        dataReads6,
                        dataWrites6)
    parflowio_write.addStmt(s6)

     
    dataReads6a = iegenlib.PairVector([("m_data","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")
                                    ]) 
    dataWrites6a =  iegenlib.PairVector([("buf","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")])

    s6a = iegenlib.Stmt("iz_min=calcOffset(m_nz,m_r,nsg_z);iz_max=calcOffset(m_nz,m_r,nsg_z+1);iy_min=calcOffset(m_ny,m_q,nsg_y); iy_max= calcOffset(m_ny,m_q,nsg_y+1);",
                        "{[nsg_z, nsg_y, nsg_x]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  }",
                        "{[nsg_z, nsg_y, nsg_x]->[5,nsg_z,0,nsg_y,0,nsg_x,1]}",
                        dataReads6a,
                        dataWrites6a)
    parflowio_write.addStmt(s6a)

 
    dataReads7 = iegenlib.PairVector([("m_data","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")
                                    ]) 
    dataWrites7 =  iegenlib.PairVector([("buf","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")])

    s7 = iegenlib.Stmt("buf = (uint64_t*)&(m_data[iz*m_nx*m_ny+iy*m_nx+calcOffset(m_nx,m_p,nsg_x)]);",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  && iz_min  <=iz< iz_max && iy_min <=iy< iy_max}",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]->[5,nsg_z,0,nsg_y,0,nsg_x,2,iz,0,iy,0]}",
                        dataReads7,
                        dataWrites7)
    parflowio_write.addStmt(s7)

    dataReads8 = iegenlib.PairVector([("tmp","{[nsg_z, nsg_y, nsg_x, iz, iy,j]->[0]}"),\
                                      ("buf","{[nsg_z, nsg_y, nsg_x, iz, iy,j]->[j]}")\
                                    ]) 
    dataWrites8 =  iegenlib.PairVector([("tmp","{[nsg_z, nsg_y, nsg_x, iz, iy,j]->[0]}"),\
                                       ("writeBuf","{[nsg_z, nsg_y, nsg_x, iz, iy,j]->[j]}")])

    s8 = iegenlib.Stmt("tmp = buf[j]; tmp = bswap64(tmp); writeBuf[j] = *(double*)(&tmp);",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy,j]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  && iz_min  <=iz< iz_max && iy_min <=iy< iy_max && 0<=j<x_extent}",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy,j]->[5,nsg_z,0,nsg_y,0,nsg_x,2,iz,0,iy,1,j,0]}",
                        dataReads8,
                        dataWrites8)
    parflowio_write.addStmt(s8)
    
    dataReads9 = iegenlib.PairVector([("x_extent","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}"),\
                                    ("writeBuf","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")
                                    ]) 
    dataWrites9 =  iegenlib.PairVector([("fp","{[nsg_z, nsg_y, nsg_x, iz, iy]->[0]}")])

    s9 = iegenlib.Stmt("fwrite(writeBuf.data(),sizeof(double),x_extent,fp);",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  && iz_min  <=iz< iz_max && iy_min <=iy< iy_max}",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]->[5,nsg_z,0,nsg_y,0,nsg_x,2,iz,0,iy,2]}",
                        dataReads9,
                        dataWrites9)
    parflowio_write.addStmt(s9)


    dataReads10 = iegenlib.PairVector([("fp","{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                    ("sg_count","{[nsg_z, nsg_y, nsg_x]->[0]}")
                                    ]) 
    dataWrites10 =  iegenlib.PairVector([("byte_offsets","{[nsg_z, nsg_y, nsg_x]->[sg_count]}"),\
                                       ("sg_count","{[nsg_z, nsg_y, nsg_x]->[0]}")])

    s10 = iegenlib.Stmt("byte_offsets[sg_count] = ftell(fp); sg_count++;",
                        "{[nsg_z, nsg_y, nsg_x]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p }",
                        "{[nsg_z, nsg_y, nsg_x]->[5,nsg_z,0,nsg_y,0,nsg_x,3]}",
                        dataReads10,
                        dataWrites10)
    parflowio_write.addStmt(s10)

    dataReads11 = iegenlib.PairVector([("nsg", "{[0]->[0]}")])

    dataWrites11 =  iegenlib.PairVector([("nsg", "{[0]->[0]}")])
                                   

    s11 = iegenlib.Stmt("nsg= nsg+1;",
                        "{[nsg_z]: 0<= nsg_z< m_r}",
                        "{[nsg_z]->[5,nsg_z,1]}",
                        dataReads11,
                        dataWrites11)
    parflowio_write.addStmt(s11)


    dataReads12 = iegenlib.PairVector([("fp","{[0]->[0]}")])
    dataWrites12 =  iegenlib.PairVector([("fp","{[0]->[0]}")])

    s12 = iegenlib.Stmt("fclose(fp);",
                        "{[0]}",
                        "{[0]->[6]}",
                        dataReads12,
                        dataWrites12)
    parflowio_write.addStmt(s12) 

    return parflowio_write
    

parflowiox_readFile = iegenlib.Computation()
parflowiox_readFile = readFile("test.pfb")

print(parflowiox_readFile.codeGenMemoryManagementString())
#print(parflowiox_readFile.codeGen())

parflowiox_mean = iegenlib.Computation()
parflowiox_mean = compute_mean()

result = parflowiox_readFile.appendComputation(parflowiox_mean, "{[0]}","{[0]->[4]}")
#print(result.tuplePosition,  result.returnValues)

parflowiox_writeFile = iegenlib.Computation()
parflowiox_writeFile = writeFile("hello.pfb")

update_ES = "{[0]->[" +str((result.tuplePosition+1))+"]}"
result2 = parflowiox_readFile.appendComputation(parflowiox_writeFile, "{[0]}",update_ES)
# parflowiox_readFile.finalize()
knownConstraints = iegenlib.Set("{[nsg_z, nsg_y, nsg_x, iz, iy]:calcOffset(m_nz,m_r,nsg_z)  <= calcOffset(m_nz,m_r,nsg_z+1) && calcOffset(m_ny,m_q,nsg_y) <= calcOffset(m_ny,m_q,nsg_y+1)}")

## shift statement to the top
rel7 = iegenlib.Relation("{[4]->[2]}")
parflowiox_readFile.addTransformation(7, rel7)

# shift statement to the second from the top
rel8 = iegenlib.Relation("{[4, x, 0, y, 1]-> [2, x, 0, y, 1]}")
parflowiox_readFile.addTransformation(8, rel8)


# transform x, y, z -> z, y, x
rel9 = iegenlib.Relation("{[4, x, 0, y, 1, z, 0]-> [3, z, 0, y, 1, x, 1]}")
parflowiox_readFile.addTransformation(9, rel9)

# add nsg loop to prepare for tiling
rel2 = iegenlib.Relation("{[3, z, 0, y, 1, x, 1]-> [3,nsg,2, z, 0, y, 1, x, 1]:nsg=0}")
parflowio.addTransformation(9,rel2)

#tile the loop
rel = iegenlib.Relation("{[3,0,2, z, 0, y, 1, x, 1]->[3,0,2,ik,ir,z,0, jk,jr,y,1,kk,x,2]: 0<=ir<888888 and z=888888 ik+ir and 0<=jr<777777 and y=777777 jk+jr  and   0<=kr<999999 and x=999999 kk+kr}")
parflowio.addTransformation(stmtIndex=9,rel=rel)

rel10 = iegenlib.Relation("{[4, x, 0, y, 2]-> [4, y, 0, x, 0]}")
parflowiox_readFile.addTransformation(10, rel10)


# parflowiox_mean.fuse(6,8,3)
#print(parflowiox_readFile.codeGen(knownConstraints=knownConstraints))


codeGenStr = parflowiox_readFile.codeGen()

codeGenStr = codeGenStr.replace('888888','nz')
codeGenStr = codeGenStr.replace('888887','nz-1')
codeGenStr = codeGenStr.replace('777777','ny')
codeGenStr = codeGenStr.replace('777776','ny-1')
codeGenStr = codeGenStr.replace('999999','nx')
codeGenStr = codeGenStr.replace('999998','nx-1')
print(codeGenStr)

parflowiox_readFile.clear()