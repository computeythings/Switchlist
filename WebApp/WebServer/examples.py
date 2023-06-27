tableData =  [
    {
        "scan_ip": "192.168.1.1",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH1-B123-RM9",
        "ip_addresses": {
            "192.168.10.1/24": {
                "interface": "Vlan10",
                "vrf": ""
            },
            "192.168.20.1/24": {
                "interface": "Vlan20",
                "vrf": ""
            },
            "192.168.30.1/24": {
                "interface": "Vlan30",
                "vrf": ""
            },
            "192.168.40.1/24": {
                "interface": "Vlan40",
                "vrf": ""
            },
            "192.168.50.1/24": {
                "interface": "Vlan50",
                "vrf": ""
            },
            "192.168.60.1/24": {
                "interface": "Vlan60",
                "vrf": ""
            },
            "192.168.70.1/24": {
                "interface": "Vlan70",
                "vrf": ""
            },
            "192.168.80.1/24": {
                "interface": "Vlan80",
                "vrf": ""
            },
            "10.0.0.1/24": {
                "interface": "Vlan100",
                "vrf": "CUSTOMER_B"
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC09823481"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Twe1/0/23": {
                "distant_host": "DOWNSTREAM-SWITCH1",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe1/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2-RM123-TESTINGasdfasdfasdfasdfasdf",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe2/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe1/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe2/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe2/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe1/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe1/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe2/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe1/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe3/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe3/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe3/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe3/0/13": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe3/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe3/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Twe3/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Twe3/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Twe3/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe1/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe2/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe1/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe2/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe2/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe1/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe1/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe2/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe1/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe3/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe3/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe3/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe3/0/13": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe3/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe3/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Dwe3/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Dwe3/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Dwe3/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Te1/0/23": {
                "distant_host": "DOWNSTREAM-SWITCH1",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Te1/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2-RM123-TESTING",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Te2/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Te1/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Te2/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Te2/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Te1/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Te1/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "Te2/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "Te1/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "Te3/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Te3/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Te3/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Te3/0/13": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Te3/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Te3/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "Te3/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "Te3/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "Te3/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "De1/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "De2/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "De1/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "De2/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "De2/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "De1/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "De1/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.143"
            },
            "De2/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.155"
            },
            "De1/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.123"
            },
            "De3/0/12": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "De3/0/1": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "De3/0/4": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "De3/0/13": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "De3/0/15": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "De3/0/41": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            },
            "De3/0/22": {
                "distant_host": "DOWNSTREAM-SWITCH2",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.143"
            },
            "De3/0/16": {
                "distant_host": "DOWNSTREAM-SWITCH3",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.155"
            },
            "De3/0/45": {
                "distant_host": "DOWNSTREAM-SWITCH4",
                "distant_port": "Gi3/3/1",
                "distant_ip": "192.168.2.123"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.2",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH2-B123-RM12",
        "ip_addresses": {
            "192.168.1.2/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC09823482"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH2",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.2"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.3",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH3-B123-RM3",
        "ip_addresses": {
            "192.168.1.3/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U",
            "C3850-48U",
            "C3850-48U",
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC09823483",
            "FJC09823469",
            "FJC09823420",
            "FJC09828008"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH3",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.3"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.4",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH4-B123-RM18",
        "ip_addresses": {
            "192.168.1.4/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC09823484"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH4",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.4"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.5",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH5-B123-RM15",
        "ip_addresses": {
            "192.168.1.5/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC09823485"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH5",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.5"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.6",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH6-B123-RM10",
        "ip_addresses": {
            "192.168.1.6/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC09823486"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH6",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.6"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.7",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH7-B123-RM3",
        "ip_addresses": {
            "192.168.1.7/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC09823487"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH7",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.7"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.8",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH8-B123-RM11",
        "ip_addresses": {
            "192.168.1.8/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC09823488"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH8",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.8"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.9",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH9-B123-RM14",
        "ip_addresses": {
            "192.168.1.9/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC09823489"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH9",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.9"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.10",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH10-B123-RM19",
        "ip_addresses": {
            "192.168.1.10/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234810"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH10",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.10"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.11",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH11-B123-RM10",
        "ip_addresses": {
            "192.168.1.11/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234811"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH11",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.11"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.12",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH12-B123-RM8",
        "ip_addresses": {
            "192.168.1.12/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC098234812"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH12",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.12"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.13",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH13-B123-RM4",
        "ip_addresses": {
            "192.168.1.13/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234813"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH13",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.13"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.14",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH14-B123-RM12",
        "ip_addresses": {
            "192.168.1.14/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234814"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH14",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.14"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.15",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH15-B123-RM4",
        "ip_addresses": {
            "192.168.1.15/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234815"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH15",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.15"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.16",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH16-B123-RM9",
        "ip_addresses": {
            "192.168.1.16/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC098234816"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH16",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.16"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.17",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH17-B123-RM2",
        "ip_addresses": {
            "192.168.1.17/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234817"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH17",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.17"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.18",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH18-B123-RM3",
        "ip_addresses": {
            "192.168.1.18/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234818"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH18",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.18"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.19",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH19-B123-RM18",
        "ip_addresses": {
            "192.168.1.19/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234819"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH19",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.19"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.20",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH20-B123-RM9",
        "ip_addresses": {
            "192.168.1.20/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC098234820"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH20",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.20"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.21",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH21-B123-RM7",
        "ip_addresses": {
            "192.168.1.21/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234821"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH21",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.21"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.22",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH22-B123-RM16",
        "ip_addresses": {
            "192.168.1.22/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234822"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH22",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.22"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.23",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH23-B123-RM4",
        "ip_addresses": {
            "192.168.1.23/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234823"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH23",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.23"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.24",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH24-B123-RM3",
        "ip_addresses": {
            "192.168.1.24/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234824"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH24",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.24"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.25",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH25-B123-RM6",
        "ip_addresses": {
            "192.168.1.25/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234825"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH25",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.25"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.26",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH26-B123-RM19",
        "ip_addresses": {
            "192.168.1.26/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234826"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH26",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.26"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.27",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH27-B123-RM15",
        "ip_addresses": {
            "192.168.1.27/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234827"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH27",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.27"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.28",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH28-B123-RM8",
        "ip_addresses": {
            "192.168.1.28/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC098234828"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH28",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.28"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.29",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH29-B123-RM14",
        "ip_addresses": {
            "192.168.1.29/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234829"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH29",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.29"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.30",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH30-B123-RM9",
        "ip_addresses": {
            "192.168.1.30/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234830"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH30",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.30"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.31",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH31-B123-RM2",
        "ip_addresses": {
            "192.168.1.31/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-24U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234831"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH31",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.31"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.32",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH32-B123-RM3",
        "ip_addresses": {
            "192.168.1.32/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234832"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH32",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.32"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.33",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH33-B123-RM6",
        "ip_addresses": {
            "192.168.1.33/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234833"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH33",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.33"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.34",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH34-B123-RM20",
        "ip_addresses": {
            "192.168.1.34/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-24U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.8.1",
        "serial": [
            "FJC098234834"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH34",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.34"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.35",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH35-B123-RM5",
        "ip_addresses": {
            "192.168.1.35/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "3560CX-12P"
        ],
        "base_model": "3560CX",
        "firmware": "IOS 15.2",
        "serial": [
            "FJC098234835"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH35",
                "distant_port": "Gi1/1/4",
                "distant_ip": "192.168.2.35"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.36",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH36-B123-RM13",
        "ip_addresses": {
            "192.168.1.36/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234836"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH36",
                "distant_port": "Gi1/1/1",
                "distant_ip": "192.168.2.36"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.37",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH37-B123-RM12",
        "ip_addresses": {
            "192.168.1.37/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C9300-48U"
        ],
        "base_model": "C9300",
        "firmware": "IOS-XE 17.3.5",
        "serial": [
            "FJC098234837"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH37",
                "distant_port": "Gi1/1/2",
                "distant_ip": "192.168.2.37"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.38",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH38-B123-RM9",
        "ip_addresses": {
            "192.168.1.38/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
            "FJC098234838"
        ],
        "upstream": "Gi1/1/1 CORE",
        "fips": True,
        "neighbors": {
            "Gi1/1/1": {
                "distant_host": "UPSTREAM-SWITCH38",
                "distant_port": "Gi1/1/3",
                "distant_ip": "192.168.2.38"
            }
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "managed"
    },
    {
        "scan_ip": "192.168.1.39",
        "base_subnet": "255.255.255.0",
        "hostname": "SWITCH39-B123-RM9",
        "ip_addresses": {
            "192.168.1.39/24": {
                "interface": "Vlan1",
                "vrf": ""
            }
        },
        "make": "Cisco",
        "model": [
            "C3850-48U"
        ],
        "base_model": "C3850",
        "firmware": "IOS-XE 16.12.2",
        "serial": [
                "FJC098234839"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH39",
                    "distant_port": "Gi1/1/4",
                    "distant_ip": "192.168.2.39"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.40",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH40-B123-RM4",
            "ip_addresses": {
                "192.168.1.40/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C9300-24U"
            ],
            "base_model": "C9300",
            "firmware": "IOS-XE 17.3.5",
            "serial": [
                "FJC098234840"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH40",
                    "distant_port": "Gi1/1/1",
                    "distant_ip": "192.168.2.40"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.41",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH41-B123-RM5",
            "ip_addresses": {
                "192.168.1.41/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C3850-48U"
            ],
            "base_model": "C3850",
            "firmware": "IOS-XE 16.12.2",
            "serial": [
                "FJC098234841"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH41",
                    "distant_port": "Gi1/1/2",
                    "distant_ip": "192.168.2.41"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.42",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH42-B123-RM2",
            "ip_addresses": {
                "192.168.1.42/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C9300-48U"
            ],
            "base_model": "C9300",
            "firmware": "IOS-XE 17.3.5",
            "serial": [
                "FJC098234842"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH42",
                    "distant_port": "Gi1/1/3",
                    "distant_ip": "192.168.2.42"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.43",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH43-B123-RM16",
            "ip_addresses": {
                "192.168.1.43/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "3560CX-12P"
            ],
            "base_model": "3560CX",
            "firmware": "IOS 15.2",
            "serial": [
                "FJC098234843"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH43",
                    "distant_port": "Gi1/1/4",
                    "distant_ip": "192.168.2.43"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.44",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH44-B123-RM15",
            "ip_addresses": {
                "192.168.1.44/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C9300-24U"
            ],
            "base_model": "C9300",
            "firmware": "IOS-XE 17.3.5",
            "serial": [
                "FJC098234844"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH44",
                    "distant_port": "Gi1/1/1",
                    "distant_ip": "192.168.2.44"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.45",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH45-B123-RM11",
            "ip_addresses": {
                "192.168.1.45/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C3850-24U"
            ],
            "base_model": "C3850",
            "firmware": "IOS-XE 16.8.1",
            "serial": [
                "FJC098234845"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH45",
                    "distant_port": "Gi1/1/2",
                    "distant_ip": "192.168.2.45"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.46",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH46-B123-RM3",
            "ip_addresses": {
                "192.168.1.46/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C3850-24U"
            ],
            "base_model": "C3850",
            "firmware": "IOS-XE 16.8.1",
            "serial": [
                "FJC098234846"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH46",
                    "distant_port": "Gi1/1/3",
                    "distant_ip": "192.168.2.46"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.47",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH47-B123-RM8",
            "ip_addresses": {
                "192.168.1.47/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C3850-24U"
            ],
            "base_model": "C3850",
            "firmware": "IOS-XE 16.8.1",
            "serial": [
                "FJC098234847"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH47",
                    "distant_port": "Gi1/1/4",
                    "distant_ip": "192.168.2.47"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.48",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH48-B123-RM15",
            "ip_addresses": {
                "192.168.1.48/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C3850-48U"
            ],
            "base_model": "C3850",
            "firmware": "IOS-XE 16.12.2",
            "serial": [
                "FJC098234848"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH48",
                    "distant_port": "Gi1/1/1",
                    "distant_ip": "192.168.2.48"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "managed"
        },
        {
            "scan_ip": "192.168.1.49",
            "base_subnet": "255.255.255.0",
            "hostname": "SWITCH49-B123-RM11",
            "ip_addresses": {
                "192.168.1.49/24": {
                    "interface": "Vlan1",
                    "vrf": ""
                }
            },
            "make": "Cisco",
            "model": [
                "C9300-48U"
            ],
            "base_model": "C9300",
            "firmware": "IOS-XE 17.3.5",
            "serial": [
                "FJC098234849"
            ],
            "upstream": "Gi1/1/1 CORE",
            "fips": True,
            "neighbors": {
                "Gi1/1/1": {
                    "distant_host": "UPSTREAM-SWITCH49",
                    "distant_port": "Gi1/1/2",
                    "distant_ip": "192.168.2.49"
                }
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "offline"
        },
        {
            "scan_ip": "192.168.2.2",
            "base_subnet": "255.255.255.0",
            "hostname": "???",
            "ip_addresses": {
            },
            "make": "???",
            "model": [
                "???"
            ],
            "base_model": "???",
            "firmware": "???",
            "serial": [
            ],
            "upstream": "",
            "fips": False,
            "neighbors": {
            },
            "updated": "16:59 GMT 21 December, 2022",
            "uptime": "12d 2hr 42min",
            "users": 42,
            "baseMAC": "ac4a.566c.7c00",
            "status": "nologin"
        }
    ]
discover_data = [
    {
        "scan_ip": "192.168.0.1",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.2",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.3",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.4",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.5",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.6",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.7",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.8",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.9",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.10",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.11",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.12",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.13",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.14",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    },
    {
        "scan_ip": "192.168.0.15",
        "base_subnet": "255.255.255.0",
        "hostname": "???",
        "ip_addresses": {
        },
        "make": "???",
        "model": [
            "???"
        ],
        "base_model": "???",
        "firmware": "???",
        "serial": [
        ],
        "upstream": "",
        "fips": False,
        "neighbors": {
        },
        "updated": "16:59 GMT 21 December, 2022",
        "uptime": "12d 2hr 42min",
        "users": 42,
        "baseMAC": "ac4a.566c.7c00",
        "status": "nologin"
    }
]

site_info = [
    { 'name': 'CORPORATE', 'subnets': ['192.168.0.0/24','192.168.1.0/24'] },
    { 'name': 'BRANCH 1', 'subnets': ['192.168.10.0/25','192.168.10.128/25'] },
    { 'name': 'BRANCH 2', 'subnets': ['192.168.20.0/28']}
  ]