import iegenlib

parflowio = iegenlib.Computation() 
dataReads3 =  iegenlib.PairVector([])
dataWrites3 = iegenlib.PairVector([])


s3 = iegenlib.Stmt("m_data;",
                    "{[nsg,i,j,k]: 0<=nsg<m_sub && 0<=i<nx &&  0<=j<ny &&  0<=k<nz}",
                    "{[nsg,i,j,k]->[0,nsg,0,i,0,j,0,k,0]}",
                    dataReads3,
                    dataWrites3)
parflowio.addStmt(s3)


s4 = iegenlib.Stmt("m_data;",
                    "{[i,j,k]: 0<=i<nx &&  0<=j<ny &&  0<=k<nz}",
                    "{[i,j,k]->[1,i,0,j,0,k,0]}",
                    dataReads3,
                    dataWrites3)
parflowio.addStmt(s4)

print(parflowio.codeGenMemoryManagementString())
rel2 = iegenlib.Relation("{[1,i,0,j,0,k,0]-> [0,nsg,0,i,0,j,0,k,1]:nsg=0}")
parflowio.addTransformation(1,rel2)
print(parflowio.codeGen())