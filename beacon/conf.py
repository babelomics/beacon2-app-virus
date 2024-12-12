import yaml

with open("beacon/api_version.yml") as api_version_file:
    api_version_yaml = yaml.safe_load(api_version_file)

"""Beacon Configuration."""


#
# Beacon general info
#
#
beacon_id = 'SARS-CoV-2-beacon.clinbioinfosspa.es'  # ID of the Beacon
beacon_name = 'Beacon SARS-CoV-2'  # Name of the Beacon service
api_version = 'v2.0.0' # Version of the Beacon implementation
uri = 'https://SARS-CoV-2.clinbioinfosspa.es/api/'

#
# Beacon granularity
#
default_beacon_granularity = "record"
max_beacon_granularity = "record"

#
#  Organization info
#
org_id = 'es.clinbioinfosspa'  # Id of the organization
org_name = 'Andalusian Platform for Computational Medicine, Fundacion Progreso y Salud'  # Full name
org_description = ('Andalusian Platform for Computational Medicine (APCM) '
                   'is one of the research platforms of the Fundación Progreso y Salud (FPS). '
                   'APCM has  the mission of facilitating and providing the tools for the inclusion of the genomic data '
                   'of the patient in the electronic health record.')
org_adress = ('Edificio C.D.C.A.. Hospital Universitario  Virgen del Rocio'
              'Avenida Manuel Siurot s/n, '
              '41013 Sevilla, Spain')
org_welcome_url = 'http://www.clinbioinfosspa.es/'
org_contact_url = 'mailto:csvs@clinbioinfosspa.es'
org_logo_url = 'http://www.clinbioinfosspa.es/sites/default/files/logo-fundacion_3.png'
org_info = ('Genomic approach for the identification of SARS-CoV-2 is based on the GA4GH Beacon '
            '<a href="https://github.com/ga4gh-beacon/specification-v2/blob/master/beacon.yaml">v2.0</a>')

#
# Project info
#
#description = (r"This <a href='https://beacon-project.io/'>Beacon</a> "
#               r"is based on the GA4GH Beacon "
#               r"<a href='https://github.com/ga4gh-beacon/specification-v2/blob/master/beacon.yaml'>v2.0</a>")
description = r"This Beacon is based on SARS-Cov-2 project."
version = api_version_yaml['api_version']
welcome_url = 'https://SARS-CoV-2.clinbioinfosspa.es/'
alternative_url = 'https://SARS-CoV-2.clinbioinfosspa.es/api'
create_datetime = '2024-07-30T12:00:00.000000'
update_datetime = ''
# update_datetime will be created when initializing the beacon, using the ISO 8601 format

#
# Service
#
service_type = 'org.ga4gh:beacon:1.0.0'  # service type
service_url = 'https://beacon.ega-archive.org/api/services'
entry_point = False
is_open = True
documentation_url = 'https://github.com/EGA-archive/beacon-2.x/'  # Documentation of the service
environment = 'test'  # Environment (production, development or testing/staging deployments)

# GA4GH
ga4gh_service_type_group = 'org.ga4gh'
ga4gh_service_type_artifact = 'beacon'
ga4gh_service_type_version = '1.0'

# Beacon handovers
beacon_handovers ={
        'handoverType': {
            'id': 'CUSTOM:000001',
            'label': 'Genome sequencing of the SARS-CoV-2 virus'
        },
        'note': ('Genome sequencing of the SARS-CoV-2 virus'
                 'for the monitoring and management of the Covid-19 epidemic in Andalusia and rapid generation'
                 'of prognostic biomarkers and response to treatment'),
        'url': 'https://www.clinbioinfosspa.es/projects/covseq/'
    }

#
# Database connection
#
#database_host = 'mongo'#'host.docker.internal'
#PRO
database_uri = "xxx"
database_host = ''
database_port = 27020
database_user = ''
database_password = ''
database_name = 'xxx'
database_auth_source = 'xxx'

# Web server configuration
# Note: a Unix Socket path is used when behind a server, not host:port
#
beacon_host = '0.0.0.0'
beacon_port = 5050
beacon_tls_enabled = False
beacon_tls_client = False
beacon_cert = '/etc/ega/server.cert'
beacon_key = '/etc/ega/server.key'
CA_cert = '/etc/ega/CA.cert'

#
# Permissions server configuration
#
permissions_url = 'http://beacon-permissions:5051/'

#
# IdP endpoints (OpenID Connect/Oauth2)
#
# or use Elixir AAI (see https://elixir-europe.org/services/compute/aai)
#

idp_url = 'http://idp:8080/'
#idp_url = 'http://localhost:8080/'

#
# UI
#
autocomplete_limit = 16
autocomplete_ellipsis = '...'

#
# Ontologies
#
ontologies_folder = "ontologies"

alphanumeric_terms = ['libraryStrategy', 'molecularAttributes.geneIds', 'diseases.ageOfOnset.iso8601duration', 'molecularAttributes.aminoacidChanges']

ontology_files={"NCIT": "http://purl.obolibrary.org/obo/NCIT.obo"}
