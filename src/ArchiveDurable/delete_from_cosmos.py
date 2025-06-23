def delete_records(records):
    for record in records:
        cosmos.delete(record.id)
