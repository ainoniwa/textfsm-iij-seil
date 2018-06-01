# textfsm-iij-seil

TextFSM template for IIJ SEIL series

## Requirements

* textfsm

## Support commands

* `show key`
* `show status arp`
* `show status function`
* `show status nat`
* `show status route`
* `show status route6`
* `show status vrrp`
* `show status vrrp3`
* `show system`
* `show users`

## Example

```
import json
import textfsm

target = "iij_seil_show_status_vrrp"

with open('tests/{s}/{s}.raw'.format(s=target)) as f:
    text = f.read()

with open('templates/{s}.template'.format(s=target)) as f:
    t = textfsm.TextFSM(f)
    pt = t.ParseText(text)
    parsed_dict = [dict(zip(t.header, l)) for l in pt]

print(json.dumps(parsed_dict, indent=2))
```

## Test

```
$ pip install tox
$ tox
```
