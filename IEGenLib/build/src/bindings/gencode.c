#undef s0
#undef s_0
#undef s1
#undef s_1
#define s_0(i, j, k)   m_data; 
#define s0(__x0, i, __x2, j, __x4, k, __x6)   s_0(i, j, k);
#define s_1(x, y, z)   mean[x+y*m_nx]+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x]; 
#define s1(ik, ir, x1, jk, jr, y1, kk, kr, z1)   s_1(x1, y1, z1);


int t1 = 0; 
int t2 = 0; 
int t3 = 0; 
int t4 = 0; 
int t5 = 0; 
int t6 = 0; 
int t7 = 0; 
int t8 = 0; 
int t9 = 0; 

for(t1 = 0; t1 <= intFloor(m_nx-1,nx); t1++) {
  for(t2 = 0; t2 <= nx-1; t2++) {
    for(t3 = 0; t3 <= nx*t1+t2; t3++) {
      for(t4 = 0; t4 <= ny-1; t4++) {
        for(t5 = 0; t5 <= ny-1; t5++) {
          if (nz >= t5+1) {
            for(t6 = 0; t6 <= nz-1; t6++) {
              if (m_nz >= 1) {
                for(t7 = -1; t7 <= intFloor(m_nz-1,ny); t7++) {
                  if (t5 <= 0 && t3 <= 0 && t1 <= 0 && t7 == 0) {
                    s0(t1,t2,t3,t4,t5,t6,t7);
                  }
                  if (m_nx >= t3+1 && nx*t1 >= t3-nx-1 && m_ny >= ny*t4+t5+1 && t3 >= nx*t1+t2 && t6 == ny*t4+t5) {
                    for(t8 = max(0,-ny*t7); t8 <= min(m_nz-ny*t7-1,nz-1); t8++) {
                      s1(t1,t2,t3,t4,t5,t6,t7,t8,ny*t7+t8);
                    }
                  }
                }
              }
              else {
                if (t5 <= 0 && t3 <= 0 && t1 <= 0) {
                  s0(t1,t2,t3,t4,t5,t6,0);
                }
              }
            }
          }
          if (m_nz >= 1 && m_nx >= t3+1 && m_ny >= ny*t4+t5+1 && nx*t1 >= t3-nx-1 && t3 >= nx*t1+t2 && ny*t4+t5 >= nz) {
            for(t7 = -1; t7 <= intFloor(m_nz-1,ny); t7++) {
              for(t8 = max(0,-ny*t7); t8 <= min(-ny*t7+m_nz-1,nz-1); t8++) {
                s1(t1,t2,t3,t4,t5,ny*t4+t5,t7,t8,ny*t7+t8);
              }
            }
          }
        }
      }
      if (nx*t1 >= t3-nx-1 && m_nz >= 1 && t3 >= nx*t1+t2 && m_nx >= t3+1) {
        for(t4 = max(0,ny); t4 <= intFloor(m_ny-1,ny); t4++) {
          for(t5 = 0; t5 <= min(-ny*t4+m_ny-1,ny-1); t5++) {
            for(t7 = -1; t7 <= intFloor(m_nz-1,ny); t7++) {
              for(t8 = max(-ny*t7,0); t8 <= min(-ny*t7+m_nz-1,nz-1); t8++) {
                s1(t1,t2,t3,t4,t5,ny*t4+t5,t7,t8,ny*t7+t8);
              }
            }
          }
        }
      }
    }
  }
  if (m_ny >= 1 && m_nz >= 1) {
    for(t2 = max(nx,0); t2 <= min(nx-1,-nx*t1+m_nx-1); t2++) {
      for(t4 = 0; t4 <= intFloor(m_ny-1,ny); t4++) {
        for(t5 = 0; t5 <= min(-ny*t4+m_ny-1,ny-1); t5++) {
          for(t7 = -1; t7 <= intFloor(m_nz-1,ny); t7++) {
            for(t8 = max(0,-ny*t7); t8 <= min(nz-1,m_nz-ny*t7-1); t8++) {
              s1(t1,t2,nx*t1+t2,t4,t5,ny*t4+t5,t7,t8,ny*t7+t8);
            }
          }
        }
      }
    }
  }
}
if (ny >= 1 && m_nx <= 0 && nz >= 1) {
  for(t2 = 0; t2 <= nx-1; t2++) {
    for(t4 = 0; t4 <= ny-1; t4++) {
      for(t6 = 0; t6 <= nz-1; t6++) {
        s0(0,t2,0,t4,0,t6,0);
      }
    }
  }
}

#undef s0
#undef s_0
#undef s1
#undef s_1