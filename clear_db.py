from db import collection

# cursor = collection.find()
# for obj in cursor:
#     empty_db(obj['_id'])

# Delete all documents from the collection
result = collection.delete_many({})

# Print the number of deleted documents
print("Number of documents deleted:", result.deleted_count)




