import iegenlib
import gc  
import inspect 
from pprint import pprint
#gc.disable()

parflowio = iegenlib.Computation() 
dataReads4 =  iegenlib.PairVector([("m_data","{[x,y,z]->[z,y,x]}")])
dataWrites4 = iegenlib.PairVector([("mean","{[x,y,z]->[x,y]}")])

s4 = iegenlib.Stmt("mean[x+y*m_nx]+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x];",
                    "{[x,y,z]:0<=y<m_ny && 0<=x<m_nx && 0<=z<m_nz}",
                    "{[x,y,z]->[0,x,0,y,0,z,0]}",
                    dataReads4,
                    dataWrites4)
parflowio.addStmt(s4)

rel = iegenlib.Relation("{[0,x,0,y,0,z,0]-> [0,z,0,y,0,x,0]}")
parflowio.addTransformation(stmtIndex=0,rel=rel)

print(parflowio.codeGen())