from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class HysteresisParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from hysteresis.parsers.parser import HysteresisParser

        return HysteresisParser(**self.model_dump())


parser_entry_point = HysteresisParserEntryPoint(
    name='HysteresisParser',
    description='New hysteresis parser.',
    mainfile_name_re=r'.*\.mh',
)
