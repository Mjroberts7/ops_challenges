# Import libraries
import os
import psutil
import time
# Script Name:                  ops-301d14_Challenge10.py
# Author:                       Michael Roberts 
# Date of latest revision:      12/11/2023
# Purpose:                      utilize psutil to output some computer info
# Execution:			        python3 ops-301d14_Challenge10.py 
# Documentation                 https://psutil.readthedocs.io/en/latest/

# putting the cpu_times outpute into a variable
cputimes = psutil.cpu_times()
print('Time spent')

# Time spent by normal processes executing in user mode
print(f'User mode: {cputimes.user}')

# Time spent by processes executing in kernel mode
print(f'Kernel mode: {cputimes.system}')

# Time when system was idle
print(f'Idle mode: {cputimes.idle}')

# Time spent by priority processes executing in user mode
print(f'Nice mode: {cputimes.nice}')

# Time spent waiting for I/O to complete.
print(f'Waiting for I/O to complete: {cputimes.iowait}')

# Time spent for servicing hardware interrupts
print(f'Servicing hardware interrupts: {cputimes.irq}')

# Time spent for servicing software interrupts
print(f'Servicing software interrupts: {cputimes.softirq}')

# Time spent by other operating systems running in a virtualized environment
print(f'Other operating systems in virtual env: {cputimes.steal}')

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print(f'Running virtual CPU for guest os under linux kernel: {cputimes.guest}')

time.sleep(2)
print('')
# stretch goals this just created a new text file, put the variable info into the text file,
# printed to the screen all the informatioin in the text file then delete the file when done.
new_file = 'cpu_info.txt'

with open(new_file, 'w') as cpu:
    cpu.write(f'This is the cpu information saved: {cputimes}')
    
with open(new_file, 'r') as cpu:
    for line in cpu:
        print(line)

cpu.close()

os.remove('cpu_info.txt')