# nxpy: Network XML Python Proxy

`nxpy` maps exported XML configuration (from Juniper network devices) to python
classes. It is compatible only with Junipers' xml configuration and is developed
to work alongside [ncclient](https://github.com/ncclient/ncclient).

nxpy allows for retrieving the device configuration in xml format (using either
netconf or "show configuration | display xml" via an expect script), transform
the configuration to python classes in order to manipulate them (view, edit,
delete).  After editing, the configuration can be applied back to the device via
netconf or cli expect.

Furthermore, it allows for building configuration via python classes, and apply
it to the device(s) via netconf or cli expect.  For the time, it supports
limited configuration changes.

## Installing

Requirements:

* Python 2.6 <= version < 3.0
* lxml (tested with 2.2.6)

To install:

```
python setup.py install
```

## Examples

* Grab the configuration in xml format

Let's say that you have grabbed your Juniper device configuration in xml format
(This is STRICT!!!). You can use either "show configuration | display xml" (and
copy paste the output to a file), or use an automated cli excpect script or
invoke netconf.  nxpy is developed as a companion to
[ncclient](https://github.com/ncclient/ncclient).

* Feed the configuration to nxpy

```
import nxpy as np
conf = np.Parser(<configuration_file_OR_configuration_text>)
conf = conf.export()
```

To check if it worked:

```
conf.interfaces
```

(...you should get the list of device interfaces)

## Changelog

* v0.4.3:
  * Python packaging changes (README,setup.py)
  * Change license to GPLv3
* v0.4.2:
  * Preliminary support for L2VPNS
  * Ethernet OAM support
* v0.4.1:
  * Fix version in setup.py
* v0.4:
  * Added full support for bgp flowspec (routing-options flow) configuration
* v0.3:
  * Support for basic interface configuration (name, description, vlan)
  * Support for basic vlan configuration

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file
for details.
