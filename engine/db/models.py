from datetime import datetime

from config import DB


class MongoDBModel:
    def encode_object_id_to_string(self, rec):
        rec["_id"] = str(rec["_id"])
        return rec

    def add(self, rec):
        """
        avoid adding duplicates while adding
        """
        rec['ts'] = datetime.now()
        self.collection.insert_one(rec)

    def find(self, filter_criteria):
        return list(self.collection.find(filter_criteria))

    def list_all(self):
        return map(self.encode_object_id_to_string, list(self.collection.find()))


class Scrip(MongoDBModel):
    def __init__(self):
        self.collection = DB['udun']

    def add(self, rec):
        """
        avoid adding duplicates while adding
        """
        rec['ts'] = datetime.now()
        # scrip_id = rec['Scrip ID']
        # company = rec['Firm Name']

        # Insert the case if not already inserted
        # if not len(self.find({"Scrip ID": scrip_id, "Firm Name": company})) > 0:
        self.collection.insert_one(rec)

    def find(self, filter_criteria):
        return list(self.collection.find(filter_criteria))


def update(collection_name, results):
    """
    this method is used to update records in MongoDB
    """
    scrip = Scrip()

    if collection_name == "udun":
        print("inserting ====>", results)
        for current in results:
            scrip.add(current)
