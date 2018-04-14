# textfsm-iij-seil

TextFSM template for IIJ SEIL series

## Requirements

* textfsm

## Example

```
import textfsm

with open('tests/iij_seil_show_status_arp/iij_seil_show_status_arp.raw') as f:
    text = f.read()

with open('templates/iij_seil_show_status_arp.template') as f:
    t = textfsm.TextFSM(f)
    pt = t.ParseText(text)
    parsed_dict = [dict(zip(t.header, l)) for l in pt]

import json
print(json.dumps(parsed_dict, indent=2))
```

## Test

```
$ pip install tox
$ tox
```
