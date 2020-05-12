#!/usr/bin/env python
import json
import pytest
from pathlib import Path
from textfsm_iij_seil.parse import parse_output


@pytest.mark.parametrize(
    "command, dataname",
    [
        ["show status arp", "iij_seil_show_status_arp"],
        ["show status dhcp6", "iij_seil_show_status_dhcp6"],
        ["show status filter", "iij_seil_show_status_filter"],
        ["show status filter6", "iij_seil_show_status_filter6"],
        ["show status function", "iij_seil_show_status_function"],
        ["show status nat", "iij_seil_show_status_nat"],
        ["show status ndp", "iij_seil_show_status_ndp"],
        ["show status ppp", "iij_seil_show_status_ppp"],
        ["show status resolver", "iij_seil_show_status_resolver"],
        ["show status route", "iij_seil_show_status_route"],
        ["show status route6", "iij_seil_show_status_route6"],
        ["show status vrrp", "iij_seil_show_status_vrrp"],
        ["show status vrrp3", "iij_seil_show_status_vrrp3"],
        ["show certificate", "iij_seil_show_certificate"],
        ["show key", "iij_seil_show_key"],
        ["show users", "iij_seil_show_users"],
        ["show system", "iij_seil_show_system"],
    ]
)
def test_parse(command, dataname):
    stdout_file = Path(__file__).parent / dataname / '{}.raw'.format(dataname)
    parsed_file = Path(__file__).parent / dataname / '{}.json'.format(dataname)

    with open(stdout_file) as f:
        stdout = f.read()
    with open(parsed_file) as f:
        correct_dict = json.load(f)

    parsed_dict = parse_output(command, stdout)
    assert parsed_dict == correct_dict
