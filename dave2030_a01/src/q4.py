"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2019-10-19"
-------------------------------------------------------
"""

from asgn01 import expertise
from Connect import Connect

conn = Connect("dcris.txt")

rows = expertise(conn)

for row in rows:
        print(row)

conn.close()
