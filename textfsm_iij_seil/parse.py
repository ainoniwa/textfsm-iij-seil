#!/usr/bin/env python
import re
from pathlib import Path
from textfsm import clitable


def _strip_prefix(text):
    """Strip first 10 characters like `7ffeffff: ` prefix"""
    return "\n".join([re.sub(r'[0-9a-fA-F]{8}: ', '', l) for l in text.splitlines()])


def parse_output(command, data, platform=None):
    template_dir = Path(__file__).parent / 'templates'
    cli_table = clitable.CliTable("index", template_dir)

    attrs = {"Command": command}
    if platform:
        attrs.update({"Platform": platform})
    cli_table.ParseCmd(_strip_prefix(data), attrs)
    header = [h.lower() for h in cli_table.header]
    parsed_dict = [dict(zip(header, line)) for line in cli_table]

    return parsed_dict