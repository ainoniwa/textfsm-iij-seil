#!/usr/bin/env python
from pathlib import Path
from textfsm import clitable


def parse_output(command, data, platform=None):
    template_dir = Path(__file__).parent / 'templates'
    cli_table = clitable.CliTable("index", template_dir)

    attrs = {"Command": command}
    if platform:
        attrs.update({"Platform": platform})
    cli_table.ParseCmd(data, attrs)
    header = [h.lower() for h in cli_table.header]
    parsed_dict = [dict(zip(header, line)) for line in cli_table]

    return parsed_dict