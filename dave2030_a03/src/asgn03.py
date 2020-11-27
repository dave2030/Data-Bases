"""
-------------------------------------------------------
Author:  Shyam Dave
ID:      180332030
Email:   dave2030@mylaurier.ca
__updated__ = "2020-03-05"
-------------------------------------------------------
"""

def pub_counts_all(conn, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(conn)
    Use: rows = pub_counts(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of each type. Name these
        three fields "articles", "papers", and "books". List the results
        as appropriate in order by member last name and first name.
        If member_id is None, list all members. (list of ?)
    -------------------------------------------------------
    """    
    if (member_id == None):
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "a") AS articles,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "p") AS papers,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "b") AS books
                FROM member AS m 
                ORDER BY last_name, first_name
             """
        params = []
        conn.cursor.execute(sql, params)

    else: 
        
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "a") AS articles,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "p") AS papers,
                (SELECT COUNT(pub_type_id) FROM pub WHERE member_id = m.member_id AND pub_type_id = "b") AS books
                FROM member AS m 
                WHERE m.member_id = %s
                ORDER BY last_name, first_name
             """
        params = [member_id]
        
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(conn)
    Use: rows = expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of keywords and supplementary keywords
        for the member. Name these fields "keywords" and "supp_keys".
        List the results as appropriate in order by member last
        name and first name. If member_id is None, list all members.
        (list of ?)
    -------------------------------------------------------
    """
    if (member_id == None):
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = m.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = m.member_id) AS supp_keys
                FROM member AS m 
                ORDER BY last_name, first_name
             """
        params = []
        conn.cursor.execute(sql, params)

    else: 
        
        sql = """
        SELECT last_name, first_name, 
                (SELECT COUNT(keyword_id) FROM member_keyword WHERE member_id = m.member_id) AS keywords,
                (SELECT COUNT(supp_key_id) FROM member_supp_key WHERE member_id = m.member_id) AS supp_keys
                FROM member AS m 
                WHERE m.member_id = %s
                ORDER BY last_name, first_name
             """
        params = [member_id]
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def keyword_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(conn)
    Use: rows = keyword_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        supplementary keywords that belong to it. Name the second field
        "supp_key_count".
        List the results as appropriate in order by keyword description.
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    
    if (keyword_id == None):
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = k.keyword_id) AS supp_key_count
                FROM keyword AS k 
                ORDER BY k_desc
             """
        params = []
        conn.cursor.execute(sql, params)

    else: 
        
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(supp_key_id) FROM supp_key WHERE keyword_id = k.keyword_id) AS supp_key_count
                FROM keyword AS k 
                WHERE keyword_id = %s
                ORDER BY k_desc
             """
        params = [keyword_id]
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows

    
def keyword_member_count(conn, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(conn)
    Use: rows = keyword_member_count(conn, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
        members that have it. Name the second field
        "member_count".
        List the results as appropriate in order by keyword description.
        If keyword_id is None, list all keywords. (list of ?)
    -------------------------------------------------------
    """
    if (keyword_id == None):
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = k.keyword_id) AS member_count
                FROM keyword AS k 
                ORDER BY k_desc
             """
        params = []
        conn.cursor.execute(sql, params)

    else: 
        
        sql = """SELECT
                (SELECT (k_desc) FROM keyword WHERE keyword_id = k.keyword_id) AS k_desc,
                (SELECT COUNT(member_id) FROM member_keyword WHERE keyword_id = k.keyword_id) AS member_count
                FROM keyword AS k 
                WHERE keyword_id = %s
                ORDER BY k_desc
             """
        params = [keyword_id]
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows

    
def supp_key_member_count(conn, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(conn)
    Use: rows = supp_key_member_count(conn, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
        keyword description, and the number of members that have it.
        Name the last field "member_count".
        List the results as appropriate in order by keyword description
        and then supplementary keyword description.
        If supp_key_id is None, list all keywords and supplementary
        keywords. (list of ?)
    -------------------------------------------------------
    """
    if (supp_key_id == None):
        sql = """
        SELECT k.k_desc , sk_desc,
            (SELECT COUNT(mk.member_id)
            FROM member_supp_key AS mk
            WHERE sk.supp_key_id = mk.supp_key_id) AS member_count
            FROM keyword AS k
            INNER JOIN supp_key AS sk
            ON sk.keyword_id = k.keyword_id
            ORDER BY k.k_desc, sk_desc
        """
        params = []
        conn.cursor.execute(sql, params)

    else: 
        sql = """
        SELECT k.k_desc , sk_desc,
            (SELECT COUNT(mk.member_id)
            FROM member_supp_key AS mk
            WHERE sk.supp_key_id = mk.supp_key_id) AS member_count
            FROM keyword AS k
            INNER JOIN supp_key AS sk
            ON sk.keyword_id = k.keyword_id
            WHERE sk.supp_key_id = %s
            ORDER BY k.k_desc, sk_desc
             """
        params = [supp_key_id]
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows

