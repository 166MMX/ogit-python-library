import re
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Pattern, Tuple, Optional


class DCTermsValidLabel(Enum):
    START = auto()
    END = auto()
    SCHEME = auto()
    NAME = auto()

    def __repr__(self):
        # https://docs.python.org/3/library/enum.html#omitting-values
        return '<%s.%s>' % (self.__class__.__name__, self.name)


@dataclass(frozen=True)
class LabeledValue:
    label: DCTermsValidLabel
    value: str


UNESCAPE_PATTERN: Pattern = re.compile(r'(?<=\\)[.:=\\]')
PAIR_PATTERN: Pattern = re.compile(r'\s*(?<!\\)[:=]\s*')
RECORD_PATTERN: Pattern = re.compile(r'\s*(?<!\\);\s*')


@dataclass(frozen=True)
class DCTermsValid:
    start: datetime
    end: datetime
    scheme: str
    name: str

    @staticmethod
    def parse_dc_structured_values(structured_values: str) -> Tuple[LabeledValue]:
        # https://www.dublincore.org/specifications/dublin-core/labelled-values-syntax/
        # https://www.dublincore.org/specifications/dublin-core/dcmi-period/
        records = RECORD_PATTERN.split(structured_values)
        records = (r for r in records if len(r.strip()) > 0)

        def transform(record: str) -> LabeledValue:
            pair = PAIR_PATTERN.split(record)
            if len(pair) != 2:
                raise RuntimeError(f"IllegalArgument: '{record}'")
            label = UNESCAPE_PATTERN.sub(r'\0', pair[0])
            value = UNESCAPE_PATTERN.sub(r'\0', pair[1])
            label = DCTermsValidLabel[label.upper()]
            return LabeledValue(label=label, value=value)

        return tuple(map(transform, records))

    @classmethod
    def parse(cls, string: str) -> 'DCTermsValid':
        if string is None:
            raise RuntimeError()
        # http://web.resource.org/rss/1.0/modules/dcterms/#valid
        structured_values = DCTermsValid.parse_dc_structured_values(string)
        start: Optional[LabeledValue] = \
            next(filter(lambda value: value.label is DCTermsValidLabel.START, structured_values), None)
        end: Optional[LabeledValue] = \
            next(filter(lambda value: value.label is DCTermsValidLabel.END, structured_values), None)
        scheme: Optional[LabeledValue] = \
            next(filter(lambda value: value.label is DCTermsValidLabel.SCHEME, structured_values), None)
        name: Optional[LabeledValue] = \
            next(filter(lambda value: value.label is DCTermsValidLabel.NAME, structured_values), None)
        if scheme and scheme.value.upper() != 'W3C-DTF':
            raise RuntimeError(f"IllegalArgument scheme='{scheme.value}'")
        start_date = DCTermsValid.parse_w3c_date_time_format(start.value) if start else None
        end_date = DCTermsValid.parse_w3c_date_time_format(end.value) if end else None
        return cls(
            start_date if start_date else None,
            end_date if end_date else None,
            scheme.value if scheme else None,
            name.value if name else None)

    @staticmethod
    def parse_w3c_date_time_format(string: Optional[str]) -> Optional[datetime]:
        # https://www.w3.org/TR/NOTE-datetime
        if string is not None:
            return datetime.fromisoformat(string)
