import os

from kepler import Kepler
from kepler.wrappers import ESLoggingWrapper, SentryWrapper

logging_wrapper = ESLoggingWrapper(
    service_name="eric-test-workshop",
    log_level='INFO',
    formatter='logstash_formatter.LogstashFormatterV1',
    es_log_index_name="eric-test-workshop-logs"
)

sentry_wrapper = SentryWrapper(os.environ['SENTRY_DSN'])

kepler_app = Kepler(
    root_directory=__name__,  # where to search for tasks (decorated functions)
    is_production='yes',  # do we execute on production now?
    logging_wrapper=logging_wrapper,  # required wrapper for you logs to appear in ES
    sentry_wrapper=sentry_wrapper  # required wrapper for you exception appear in Sentry
)
