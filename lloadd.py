import os,sys,time
from time import sleep


load = '-'
time = 0

for u in range(101):
    print(f'\rLoading {u}% [{load}]',end='',flush=True)
    sleep (0.6)
    time += 1
    if time == 3:
        time = 0
        load += '-'
print('\nBerjaya!')
