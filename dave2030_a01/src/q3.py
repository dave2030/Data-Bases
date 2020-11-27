"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2019-10-19"
-------------------------------------------------------
"""

from asgn01 import member_expertise
from Connect import Connect

conn = Connect("dcris.txt")

rows = member_expertise(conn,"53",None)

for row in rows:
        print(row)
conn.close()
