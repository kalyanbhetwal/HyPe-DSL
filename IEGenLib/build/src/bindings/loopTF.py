import iegenlib

parflowio = iegenlib.Computation() 
dataReads3 =  iegenlib.PairVector([])
dataWrites3 = iegenlib.PairVector([])

#{[a,b,c] -> [nsg,k,i,j,a,b,c] : 0 <= nsg < m_numSubgrids & 0 <= k < nz & 0 <= i < ny & 0 <= j < nx & c = j + x & b = y+ i & c =... }

s3 = iegenlib.Stmt("m_data;",
                    "{[i,j,k]: 0<=i<nx &&  0<=j<ny &&  0<=k<nz}",
                    "{[i,j,k]->[0,i,0,j,0,k,0]}",
                    dataReads3,
                    dataWrites3)
#parflowio.addStmt(s3)

dataReads4  =  iegenlib.PairVector([])
dataWrites4 = iegenlib.PairVector([])
s4 = iegenlib.Stmt("mean[x+y*m_nx]+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x];",
                    "{[z,y,x]: 0<=x<m_nx &&  0<=y<m_ny &&  0<=z<m_nz}",
                    "{[z,y,x]->[0,z,0,y,0,x,0]}",
                    dataReads4,
                    dataWrites4)
parflowio.addStmt(s4)

rel = iegenlib.Relation("{[0,z,0,y,0,x,0]->[0,nsg,0,k,0,i,0,j,0] : 0 <= nsg < m_numSubgrids and 0 <= k < nz and 0 <= i < ny and 0 <= j < nx}")

parflowio.islSetAffineApply(rel, "{[0,nsg,0,k,0,i,0,j,0]}")

print(parflowio.codeGen())