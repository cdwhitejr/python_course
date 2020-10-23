#file_analyzer.py


import pefile

path = '/root/Desktop/Malware/Lab01-02.ext'

pe = pefile.PE(path)

print(f'Magic number is: {hex(pe.DOS_HEADER.e_magic)')
print(f'')