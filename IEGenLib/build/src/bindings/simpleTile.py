import iegenlib

parflowio = iegenlib.Computation() 
dataReads3 =  iegenlib.PairVector([])
dataWrites3 = iegenlib.PairVector([])

s3 = iegenlib.Stmt("m_data;",
                    "{[i,j,k]: 0<=i<nx &&  0<=j<ny &&  0<=k<nz}",
                    "{[i,j,k]->[0,i,0,j,0,k,0]}",
                    dataReads3,
                    dataWrites3)
parflowio.addStmt(s3)

dataReads4  =  iegenlib.PairVector([])
dataWrites4 = iegenlib.PairVector([])
s4 = iegenlib.Stmt("mean[x+y*m_nx]+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x];",
                    "{[x,y,z]: 0<=x<m_nx &&  0<=y<m_ny &&  0<=z<m_nz}",
                    "{[x,y,z]->[1,x,0,y,0,z,0]}",
                    dataReads4,
                    dataWrites4)
parflowio.addStmt(s4)

#{[i,j,k]->[ik,ir,i, jk,jr,j, kk,kr,k]: 0<=ir<99999999 and i=99999999 ik+ir and 0<=jr<99999999 and j=99999999 jk+jr  and   0<=kr<99999999 and k=99999999 kk+kr}

rel2 = iegenlib.Relation("{[1, x, 0, y, 0, z, 0]-> [0, x, 0, y, 0, z, 1]}")
parflowio.addTransformation(1,rel2)

rel = iegenlib.Relation("{[0, x, 0, y, 0, z, 1]->[ik,ir,x, jk,jr,y, kk,kr,z]: 0<=ir<888888 and x=888888 ik+ir and 0<=jr<777777 and y=777777 jk+jr  and   0<=kr<999999 and z=999999 kk+kr}")
parflowio.addTransformation(stmtIndex=1,rel=rel)

#parflowio.fuse(0,1,8)
#rel2 = iegenlib.Relation("{[1, x, 0, y, 0, z, 0]-> [1, z, 0, y, 0, x, 0]}")

codeGenStr = parflowio.codeGen()

codeGenStr = codeGenStr.replace('888888','nx')
codeGenStr = codeGenStr.replace('888887','nx-1')
codeGenStr = codeGenStr.replace('777777','ny')
codeGenStr = codeGenStr.replace('777776','ny-1')
codeGenStr = codeGenStr.replace('999999','nz')
codeGenStr = codeGenStr.replace('999998','nz-1')
print(codeGenStr)
