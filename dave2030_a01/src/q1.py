"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2019-10-19"
-------------------------------------------------------
"""

from asgn01 import keyword_table
from Connect import Connect

conn = Connect("dcris.txt")

rows = keyword_table(conn);

for row in rows:
        print(row)

conn.close()
