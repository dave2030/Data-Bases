"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""
from Connect import Connect
from asgn04 import column_info

conn = Connect("dcris.txt")

rows = column_info(conn, 'dcris', None)

for row in rows:
    print(row)

conn.close()

