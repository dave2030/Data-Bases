"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""

from Connect import Connect
from asgn04 import constraint_info

conn = Connect("dcris.txt")

rows = constraint_info(conn, 'dcris')

for row in rows:
    print(row)

conn.close()

