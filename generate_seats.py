'''
Usage: 
ipython generate_seats.py 50000 1000000 > out.txt
'''

from __future__ import division
import numpy as np
import random 
import sys

def generate_seat_arragements(N):

#Initialize:
    allowed = range(1,N+1, 1)
    occupied = []
    
    while len(allowed) != 0:  
          seat = seat=random.sample(allowed,  1)[0] 
          #if seat not in forbidden:        
          if seat == 1:
             eliminated_seats = [1,2]
          elif seat == N:
             eliminated_seats = [N-1,N]
          elif (seat > 1) and (seat < N):
             eliminated_seats = [seat-1,seat, seat+1]
          occupied.append(seat) 
          allowed = set(allowed) - set(eliminated_seats) 
             
    empty_seats = list(set(range(1, N+1, 1)) - set(occupied))   
    return (N - len(empty_seats))/N
    
    
    
def main():
    frac = []
    #Now make a distribution:
    for i in range(int(sys.argv[2])):
         frac.append(generate_seat_arragements(int(sys.argv[1])))
    print "Mean = ", np.mean(frac)
    print "Std dev = ", np.std(frac)
if __name__ == '__main__':
    main()


'''
ANS:
N=25
Mean 0.4442397200
Std 0.02865380907
N=50000
Mean 0.4325220000
Std  0.0006034865367

N = 25
iters = 1000
Mean =  0.442
Std dev =  0.0287193314685
Mean =  0.44468
Std dev =  0.0294295361839

iters=10,000
Mean =  0.44402
Std dev =  0.0286663496107
Mean =  0.444108
Std dev =  0.0291026517005
Mean =  0.443856
Std dev =  0.0286693436269
iters=100,000
Mean =  0.4442136
Std dev =  0.0286200904094
Mean =  0.4441452
Std dev =  0.0286286799723

iters = 1,000,000
Mean =  0.444170240001
0.4442397200#01
0.02865380907#15
Std dev =  0.0286555456822
Mean =  0.444239720001
Std dev =  0.0286538090715
Mean =  0.444232640001
Std dev =  0.0286328754868

N=50000
python generate_seats.py 50000 10
Mean =  0.432522
Std dev =  0.000603486536718

python generate_seats.py 50000 100
Mean =  0.4322266
Std dev =  0.000672494193283


'''