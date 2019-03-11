# textfsm-iij-seil

[![CircleCI](https://circleci.com/gh/ainoniwa/textfsm-iij-seil.svg?style=shield)](https://circleci.com/gh/ainoniwa/textfsm-iij-seil)

TextFSM template for IIJ SEIL series

## Requirements

* textfsm

## Support commands

* `show key`
* `show status arp`
* `show status filter`
* `show status function`
* `show status nat`
* `show status ppp`
* `show status resolver`
* `show status route`
* `show status route6`
* `show status vrrp`
* `show status vrrp3`
* `show system`
* `show users`

## Example

* Useful table viewing tool: `pip install prettytable`

```
from textfsm import TextFSM
from prettytable import PrettyTable

target = "iij_seil_show_status_vrrp"

with open('tests/{s}/{s}.raw'.format(s=target)) as f:
    text = f.read()

with open('templates/{s}.template'.format(s=target)) as f:
    t = TextFSM(f)
    pt = t.ParseText(text)
    table = PrettyTable(t.header)
    [table.add_row(l) for l in pt]

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
