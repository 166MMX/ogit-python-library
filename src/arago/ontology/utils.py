import re
from re import Pattern

TWO_CHAR: Pattern = re.compile(r'(?<=[a-z])[A-Z][a-z](?=[A-Z][a-z])')
ANY_CHAR: Pattern = re.compile(r'(?<=[a-z])(?=[A-Z][a-z])')
ACRONYM_BEGIN: Pattern = re.compile(r'(?<=/)[A-Z]+?(?=[A-Z][a-z])')
ACRONYM_END: Pattern = re.compile(r'(?<=[a-z])(?=[A-Z][A-Z]+$)')
DELIMITER: Pattern = re.compile(r'[/-]')
# noinspection SpellCheckingInspection
MAP = {
    'ogit/MRP/kzTCond': 'ogit/MRP/kz_temperature_Cond',
    'ogit/Network/IDSIPS': 'ogit/Network/IDS_IPS',
    'ogit/occurenceCount': 'ogit/occurrence-Count',  # typo: occurence
    'ogit/_graphtype': 'ogit/_graph-type',
    'ogit/Credit/CounterpartyMutable': 'ogit/Credit/Counter-party-Mutable',
    'ogit/Timeseries': 'ogit/Time-series',

    'ogit/OSLC-change/inprogress': 'ogit/OSLC-change/in-progress',
    'ogit/OSLC-crtv/vmid': 'ogit/OSLC-crtv/vm-id',
    'ogit/OSLC-crtv/hostid': 'ogit/OSLC-crtv/host-id',
    'ogit/OSLC-perfmon/SqlStatmentFailures': 'ogit/OSLC-perfmon/Sql-Statement-Failures',  # typo: Statment

    'ogit/OSLC-perfmon/TimeJCAThreadPoolExhausted': 'ogit/OSLC-perfmon/Time-JCA-Thread-Pool-Exhausted',  # JCA
    'ogit/OSLC-perfmon/NetworkIOErrors': 'ogit/OSLC-perfmon/Network-IO-Errors',  # IO
}


def to_constant(relative_uri: str) -> str:
    if '/' == relative_uri[-1:]:  # endswith
        relative_uri = relative_uri[:-1]  # strip
    key = relative_uri
    if key in MAP:
        ki_lang_name = MAP[key]
    else:
        two_char = TWO_CHAR.sub(r'_\g<0>_', key)  # eg _of_ _to_ _by_ _in_
        any_char = ANY_CHAR.sub('_', two_char)
        acronym_begin = ACRONYM_BEGIN.sub(r'\g<0>_', any_char)
        acronym_end = ACRONYM_END.sub('_', acronym_begin)
        snake_case = acronym_end
        ki_lang_name = snake_case
    return DELIMITER.sub('_', ki_lang_name).upper()
