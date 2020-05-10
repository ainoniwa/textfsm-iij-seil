# textfsm-iij-seil

[![CircleCI](https://circleci.com/gh/ainoniwa/textfsm-iij-seil.svg?style=shield)](https://circleci.com/gh/ainoniwa/textfsm-iij-seil)

TextFSM template for IIJ SEIL series

## Install

```bash
$ pip install git+ssh://git@github.com/ainoniwa/textfsm-iij-seil.git
```

## Support commands

See the [template index](./textfsm_iij_seil/templates/index)

## Example

* Useful table viewing tool: `pip install prettytable`

```
from textfsm_iij_seil.parse import parse_output
from prettytable import PrettyTable

with open('tests/{s}/{s}.raw'.format(s="iij_seil_show_status_vrrp")) as f:
    text = f.read()

parsed_text = parse_output("show status vrrp", text)
table = PrettyTable(parsed_text[0].keys())
for l in parsed_text:
    table.add_row(l.values())

print(table)
```

Result

```
+-----------+------+----------+--------+----------------+--------+----------+---------+
| interface | vrid | priority | state  |    address     | watch  | interval | preempt |
+-----------+------+----------+--------+----------------+--------+----------+---------+
|    lan1   |  1   |   245    | master | 192.168.1.1/24 | pppoe0 |    1     |    on   |
+-----------+------+----------+--------+----------------+--------+----------+---------+
```

## Test

```
$ pip install tox
$ tox
```
