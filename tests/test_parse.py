#!/usr/bin/env python
# coding=utf-8

import os
import json
import textfsm


def parse_and_diff_correct_dict(target):
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


def test_iij_seil_show_status_arp():
    parse_and_diff_correct_dict("iij_seil_show_status_arp")


def test_iij_seil_show_status_function():
    parse_and_diff_correct_dict("iij_seil_show_status_function")


def test_iij_seil_show_status_nat():
    parse_and_diff_correct_dict("iij_seil_show_status_nat")


def test_iij_seil_show_status_route():
    parse_and_diff_correct_dict("iij_seil_show_status_route")


def test_iij_seil_show_status_route6():
    parse_and_diff_correct_dict("iij_seil_show_status_route6")


def test_iij_seil_show_status_vrrp():
    parse_and_diff_correct_dict("iij_seil_show_status_vrrp")


def test_iij_seil_show_status_vrrp3():
    parse_and_diff_correct_dict("iij_seil_show_status_vrrp3")


def test_iij_seil_show_key():
    parse_and_diff_correct_dict("iij_seil_show_key")


def test_iij_seil_show_users():
    parse_and_diff_correct_dict("iij_seil_show_users")