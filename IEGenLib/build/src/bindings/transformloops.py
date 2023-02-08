import iegenlib

parflowio_mean = iegenlib.Computation()
dataReads4 =  iegenlib.PairVector([("m_data","{[x,y,z]->[z,y,x]}")])
dataWrites4 = iegenlib.PairVector([("mean","{[x,y,z]->[x,y]}")])

s4 = iegenlib.Stmt("mean[x+y*m_nx]+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x];",
                    "{[x,y,z]:0<=y<m_ny && 0<=x<m_nx && 0<=z<m_nz}",
                    "{[x,y,z]->[0,x,0,y,1,z,0]}",
                    dataReads4,
                    dataWrites4)
parflowio_mean.addStmt(s4)

dataReads5 =  iegenlib.PairVector([("mean","{[y,x]->[y,x]}")])
dataWrites5 = iegenlib.PairVector([("mean","{[y,x]->[y,x]}")])

s5 = iegenlib.Stmt("mean[x+y*m_nx] = mean[x+y*m_nx]/m_nz;",
                    "{[x,y]:0<=y<m_ny && 0<=x<m_nx}",
                    "{[x,y]->[0,x,0,y,2]}",
                    dataReads5,
                    dataWrites5)
parflowio_mean.addStmt(s5)

rel7 = iegenlib.Relation("{[0,x,0,y,1,z,0]-> [0,z,0,y,0,x,0]}")
parflowio_mean.addTransformation(0, rel7)

# shift statement to the second from the top
rel8 = iegenlib.Relation("{[0,x,0,y,2]-> [1,y,0,x,0]}")
parflowio_mean.addTransformation(1, rel8)


print(parflowio_mean.codeGen())