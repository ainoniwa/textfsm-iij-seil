#!/usr/bin/env python
# coding=utf-8

import os
import json
import textfsm
import pytest


@pytest.mark.parametrize(
    "target",
    [
        "iij_seil_show_status_arp",
        "iij_seil_show_status_dhcp6",
        "iij_seil_show_status_filter",
        "iij_seil_show_status_function",
        "iij_seil_show_status_nat",
        "iij_seil_show_status_ndp",
        "iij_seil_show_status_ppp",
        "iij_seil_show_status_resolver",
        "iij_seil_show_status_route",
        "iij_seil_show_status_route6",
        "iij_seil_show_status_vrrp",
        "iij_seil_show_status_vrrp3",
        "iij_seil_show_key",
        "iij_seil_show_users",
        "iij_seil_show_system",
    ]
)
def test_parse(target):
    base = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.normpath(os.path.join(base, '{s}/{s}.raw'.format(s=target)))
    correct_path = os.path.normpath(os.path.join(base, '{s}/{s}.json'.format(s=target)))
    template_path = os.path.normpath(os.path.join(base, '../templates/{s}.template'.format(s=target)))
    with open(text_path) as f:
        text = f.read()

    with open(template_path) as f:
        t = textfsm.TextFSM(f)
        pt = t.ParseText(text)
        parsed_dict = [dict(zip(t.header, l)) for l in pt]
        correct_dict = json.load(open(correct_path))
        assert parsed_dict == correct_dict
