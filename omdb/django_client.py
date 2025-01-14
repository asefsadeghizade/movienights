from django.conf import settings

from omdb.client import OmdbClient


def get_client_from_settings():
    """Create an instance of an OmdbClient using the OM         DB_KEY from the django settings."""
    return OmdbClient(settings.OMDB_KEY)
