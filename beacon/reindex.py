from pymongo.mongo_client import MongoClient
import conf


client = MongoClient(
        "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
            conf.database_user,
            conf.database_password,
            conf.database_host,
            conf.database_port,
            conf.database_name,
            conf.database_auth_source,
        )
    ) if conf.database_host != "" else MongoClient(conf.database_uri)

beacon_db = conf.database_name

try:
    client[beacon_db].drop_collection("synonyms")
except Exception:
    client[beacon_db].create_collection(name="synonyms")
try:
    client[beacon_db].validate_collection("synonyms")
except Exception:
    db=client[beacon_db].create_collection(name="synonyms")
try:
    client[beacon_db].drop_collection("counts")
except Exception:
    client[beacon_db].create_collection(name="counts")
try:
    client[beacon_db].validate_collection("counts")
except Exception:
    db=client[beacon_db].create_collection(name="counts")
try:
    client[beacon_db].drop_collection("similarities")
except Exception:
    client[beacon_db].create_collection(name="similarities")
try:
    client[beacon_db].validate_collection("similarities")
except Exception:
    db=client[beacon_db].create_collection(name="similarities")
#client[beacon_db].analyses.create_index([("$**", "text")])
#client[beacon_db].biosamples.create_index([("$**", "text")])
#client[beacon_db].cohorts.create_index([("$**", "text")])
#client[beacon_db].datasets.create_index([("$**", "text")])
#client[beacon_db].genomicVariations.create_index([("$**", "text")])
#client[beacon_db].genomicVariations.create_index([("caseLevelData.biosampleId", 1)])
#client[beacon_db].genomicVariations.create_index([("variation.location.interval.end.value", -1), ("variation.location.interval.start.value", 1)])
client[beacon_db].genomicVariations.create_index([("variantInternalId", 1), ("caseLevelData.biosampleId", 1)])
#client[beacon_db].genomicVariations.create_index([("identifiers.genomicHGVSId", 1), ("variation.location.interval.start.value", 1), ("caseLevelData.biosampleId", 1), ("variation.referenceBases", 1), ("variation.alternateBases", 1)])
client[beacon_db].genomicVariations.create_index([("variation.location.interval.end.value", -1), ("variation.location.interval.start.value", 1), ("variation.referenceBases", 1), ("variation.alternateBases", 1)])
client[beacon_db].genomicVariations.create_index([("molecularAttributes.geneIds", 1), ("variantInternalId", 1), ("variation.variantType", 1)])
#client[beacon_db].individuals.create_index([("$**", "text")])
#client[beacon_db].runs.create_index([("$**", "text")])
#collection_name = client[beacon_db].analyses
#print(collection_name.index_information())

