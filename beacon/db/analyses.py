import logging
import yaml
from typing import Dict, List, Optional
from beacon.db.filters import apply_alphanumeric_filter, apply_filters
from beacon.db.utils import query_id, query_ids, get_count, get_documents, get_cross_query, join_query
from beacon.db import client, beacon_db
from beacon.request.model import AlphanumericFilter, Operator, RequestParams
from beacon.db.schemas import DefaultSchemas
from beacon.db.utils import get_documents, query_id, get_count, get_filtering_documents, get_docs_by_response_type
from beacon.db.g_variants import apply_request_parameters
from beacon.request.model import RequestParams

LOG = logging.getLogger(__name__)

LIMIT = 1000

def include_resultset_responses(query: Dict[str, List[dict]], qparams: RequestParams):
    LOG.debug("Include Resultset Responses = {}".format(qparams.query.include_resultset_responses))
    include = qparams.query.include_resultset_responses
    return query

def get_analyses(entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'analyses'
    mongo_collection = client[beacon_db].analyses
    parameters_as_filters=False
    query_parameters, parameters_as_filters = apply_request_parameters({}, qparams)
    LOG.debug(query_parameters)
    LOG.debug(parameters_as_filters)
    if parameters_as_filters == True and query_parameters != {'$and': []}:
        query, parameters_as_filters = apply_request_parameters({}, qparams)
        query_parameters={}
    elif query_parameters != {'$and': []}:
        query=query_parameters
    elif query_parameters == {'$and': []}:
        query_parameters = {}
        query={}
    query = apply_filters(query, qparams.query.filters, collection, query_parameters)
    query = include_resultset_responses(query, qparams)
    schema = DefaultSchemas.ANALYSES
    #with open("beacon/request/datasets.yml", 'r') as datasets_file:
    with open("/beacon/beacon/request/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > LIMIT or limit == 0:
        limit = LIMIT
    idq="biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

def get_analysis_with_id(entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'analyses'
    idq="biosampleId"
    mongo_collection = client[beacon_db].analyses
    query = apply_filters({}, qparams.query.filters, collection, {})
    query = query_id(query, entry_id)
    query = include_resultset_responses(query, qparams)
    schema = DefaultSchemas.ANALYSES
    with open("/beacon/beacon/request/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > LIMIT or limit == 0:
        limit = LIMIT
    count, dataset_count, docs = get_docs_by_response_type(include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

def get_variants_of_analysis(entry_id: Optional[str], qparams: RequestParams, dataset: str):
    collection = 'analyses'
    mongo_collection = client[beacon_db].genomicVariations
    query = {"$and": [{"id": entry_id}]}
    query = apply_filters(query, qparams.query.filters, collection, {})
    analysis_ids = client[beacon_db].analyses \
        .find_one(query, {"biosampleId": 1, "_id": 0})
    LOG.debug(analysis_ids)
    query = {"caseLevelData.biosampleId": analysis_ids["biosampleId"]}
    query = apply_filters(query, qparams.query.filters, collection, {})
    query = include_resultset_responses(query, qparams)
    schema = DefaultSchemas.GENOMICVARIATIONS
    with open("/beacon/beacon/request/datasets.yml", 'r') as datasets_file:
        datasets_dict = yaml.safe_load(datasets_file)
    include = qparams.query.include_resultset_responses
    limit = qparams.query.pagination.limit
    skip = qparams.query.pagination.skip
    if limit > LIMIT or limit == 0:
        limit = LIMIT
    idq="caseLevelData.biosampleId"
    count, dataset_count, docs = get_docs_by_response_type(include, query, datasets_dict, dataset, limit, skip, mongo_collection, idq)
    return schema, count, dataset_count, docs, dataset

def get_filtering_terms_of_analyse(entry_id: Optional[str], qparams: RequestParams):
    query = {'scopes': 'analysis'}
    schema = DefaultSchemas.FILTERINGTERMS
    count = get_count(client[beacon_db].filtering_terms, query)
    remove_id={'_id':0}
    docs = get_filtering_documents(
        client[beacon_db].filtering_terms,
        query,
        remove_id,
        qparams.query.pagination.skip*qparams.query.pagination.limit,
        0
    )
    return schema, count, docs

