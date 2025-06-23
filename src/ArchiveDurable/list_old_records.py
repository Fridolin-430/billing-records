def list_old_records():
    query = "SELECT * FROM c WHERE c.timestamp < (NOW - 90 days)"
    return cosmos.query(query)
