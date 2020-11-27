"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""

def publications(conn, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = publications(conn)
    Use: rows = publications(conn, title=v1)
    Use: rows = publications(conn, pub_type_id=v2)
    Use: rows = publications(conn, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a'; the entire table if
            title and pub_type_id are None,
            else
            rows matching the partial title and pub_type_id
            if given
            sorted by last name, first name, title (list of ?)
    -------------------------------------------------------
    """ 
    if (title == None and pub_type_id == None):
        sql = "SELECT * FROM pub"
        parameter = []
    elif (title == None):
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc FROM pub AS p
                 JOIN member AS m ON m.member_id = p.member_id
                 JOIN pub_type AS pt ON pt.pub_type_id = p.pub_type_id
                 WHERE p.pub_type_id = %s 
                 ORDER BY m.last_name, m.first_name, p.p_title
              """
        parameter = [pub_type_id]
    elif (pub_type_id == None):
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc 
                 FROM pub AS p JOIN member AS m 
                 ON m.member_id = p.member_id
                 JOIN pub_type AS pt 
                 ON pt.pub_type_id = p.pub_type_id
                 WHERE p.p_title LIKE %s
                 ORDER BY m.last_name, m.first_name, p.p_title
              """  
        parameter = ["%" + title + "%"]
    else: 
        sql = """SELECT m.last_name, m.first_name, p.p_title, pt.pt_desc 
                 FROM pub AS p JOIN  member AS m ON m.member_id = p.member_id
                 JOIN pub_type AS pt ON pt.pub_type_id = p.pub_type_id
                 WHERE p.p_title LIKE %s AND pt.pub_type_id = %s
                 ORDER BY m.last_name, m.first_name, p.p_title
             """
        parameter = ["%" + title + "%", pub_type_id]
    conn.cursor.execute(sql, parameter)
    rows = conn.cursor.fetchall()
    return rows


def pub_counts(conn, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_counts(conn, member_id=v1)
    Use: rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect) 
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of type pub_type
        if given, if not, the number of all their publications (list of ?)
    -------------------------------------------------------
    """
    if (pub_type_id == None):
        sql = """SELECT p.member_id, last_name, first_name, COUNT(pub_type_id)
                 FROM pub p INNER JOIN member pc ON p.member_id = pc.member_id 
                 WHERE p.member_id = %s 
                 ORDER BY last_name, first_name, pub_type_id
              """
        parameter = [member_id]
    else:
        sql = """SELECT p.member_id, last_name, first_name, COUNT(pub_type_id) 
                 FROM pub p INNER JOIN member pc ON p.member_id = pc.member_id 
                 WHERE p.member_id = %s AND p.pub_type_id = %s
                ORDER BY last_name, first_name, pub_type_id
              """
        parameter = [member_id, pub_type_id]
    conn.cursor.execute(sql, parameter)
    rows = conn.cursor.fetchall()
    return rows


def member_expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = member_expertise_count(conn)
    Use: rows = member_expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the count of the number of expertises they
            hold (i.e. keywords)
        all records member_id is None, sorted by last name, first name
            (list of ?)
    -------------------------------------------------------
    """
    if (member_id == None):
        sql = """SELECT * FROM member m 
                 INNER JOIN member_keyword mkw 
                 ON m.member_id = mkw.member_id  
                 INNER JOIN keyword k 
                 ON mkw.keyword_id = k.keyword_id
                 ORDER BY m.last_name, m.first_name
              """
        parameter = []
    else:     
        sql = """SELECT m.last_name, m.first_name, count(k_desc) 
                 FROM member m INNER JOIN member_keyword mkw 
                    ON m.member_id = mkw.member_id  
                    INNER JOIN keyword k 
                    ON mkw.keyword_id = k.keyword_id
                    WHERE m.member_id = %s
                    ORDER BY m.last_name, m.first_name
              """
        parameter = [member_id]
    conn.cursor.execute(sql, parameter)
    rows = conn.cursor.fetchall()
    return rows


def all_expertise(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = all_expertise(conn)
    Use: rows = all_expertise(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, a keyword description, and a supplementary keyword description
        all records if member_id is None,
        sorted by last_name, first_name, keyword description, supplementary
                keyword description
    -------------------------------------------------------
    """
    if (member_id == None):
        sql = """SELECT * FROM member m INNER JOIN member_keyword mkw 
                 ON m.member_id = mkw.member_id INNER JOIN keyword k 
                 ON mkw.keyword_id = k.keyword_id INNER JOIN supp_key sk 
                 ON k.keyword_id = sk.keyword_id
                 ORDER BY m.last_name, m.first_name, k.k_desc,sk.sk_desc
              """
        parameter = []
    else:
        sql = """SELECT m.last_name, m.first_name, k_desc, sk_desc 
                 FROM member m INNER JOIN member_keyword mkw 
                 ON m.member_id = mkw.member_id INNER JOIN keyword k 
                 ON mkw.keyword_id = k.keyword_id INNER JOIN supp_key sk 
                 ON k.keyword_id = sk.keyword_id
                 WHERE m.member_id = %s
                 ORDER BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
              """
        parameter = [member_id]
    conn.cursor.execute(sql, parameter)
    rows = conn.cursor.fetchall()
    return rows
    
