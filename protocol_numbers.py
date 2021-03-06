# Array of protocol numbers and names according to IANA http:{"Name": ""},//www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

"""IANA-defined protocol numbers"""
protocol_type = {
    0:{"Name":"HOPOPT"},
    1:{"Name": "ICMP", "Category":"ICMP"},
    2:{"Name": "IGMP", "Category":"Multicast"},
    3:{"Name": "GGP"},
    4:{"Name": "IP-in-IP", "Category":"Tunnel"},
    5:{"Name": "ST"},
    6:{"Name": "TCP", "Category":"Transport"},
    7:{"Name": "CBT"},
    8:{"Name": "EGP", "Category":"Routing"},
    9:{"Name": "IGP", "Category":"Routing"},
    10:{"Name": "BBN-RCC-MON"},
    11:{"Name": "NVP-II"},
    12:{"Name": "PUP"},
    13:{"Name": "ARGUS"},
    14:{"Name": "EMCON"},
    15:{"Name": "XNET"},
    16:{"Name": "CHAOS"},
    17:{"Name": "UDP", "Category":"Transport"},
    18:{"Name": "MUX"},
    19:{"Name": "DCN-MEAS"},
    20:{"Name": "HMP"},
    21:{"Name": "PRM"},
    22:{"Name": "XNS-IDP"},
    23:{"Name": "TRUNK-1"},
    24:{"Name": "TRUNK-2"},
    25:{"Name": "LEAF-1"},
    26:{"Name": "LEAF-2"},
    27:{"Name": "RDP"},
    28:{"Name": "IRTP"},
    29:{"Name": "ISO-TP4"},
    30:{"Name": "NETBLT"},
    31:{"Name": "MFE-NSP"},
    32:{"Name": "MERIT-INP"},
    33:{"Name": "DCCP"},
    34:{"Name": "3PC"},
    35:{"Name": "IDPR"},
    36:{"Name": "XTP"},
    37:{"Name": "DDP"},
    38:{"Name": "IDPR-CMTP"},
    39:{"Name": "TP++"},
    40:{"Name": "IL"},
    41:{"Name": "IPv6 6in4", "Category":"Tunnel"},
    42:{"Name": "SDRP", "Category":"Routing"},
    43:{"Name": "IPv6 Routing", "Category":"IPv6"},
    44:{"Name": "IPv6 Fragment", "Category":"IPv6"},
    45:{"Name": "IDRP"},
    46:{"Name": "RSVP"},
    47:{"Name": "GRE", "Category":"Tunnel"},
    48:{"Name": "DSR"},
    49:{"Name": "BNA"},
    50:{"Name": "ESP", "Category":"Tunnel"},
    51:{"Name": "AH", "Category":"Tunnel"},
    52:{"Name": "I-NLSP"},
    53:{"Name": "SWIPE"},
    54:{"Name": "NARP"},
    55:{"Name": "IP Mobility"},
    56:{"Name": "TLSP"},
    57:{"Name": "SKIP"},
    58:{"Name": "IPv6 ICMP", "Category":"ICMP"},
    59:{"Name": "IPv6 NoNxt", "Category":"IPv6"},
    60:{"Name": "IPv6 Options", "Category":"IPv6"},
    61:{"Name": "Host Internal Protocol"},
    62:{"Name": "CFTP"},
    63:{"Name": "Local Network"},
    64:{"Name": "SAT-EXPAK"},
    65:{"Name": "KRYPTOLAN"},
    66:{"Name": "RVD"},
    67:{"Name": "IPPC"},
    68:{"Name": "Distributed File System"},
    69:{"Name": "SAT-MON"},
    70:{"Name": "VISA"},
    71:{"Name": "IPCV"},
    72:{"Name": "CPNX"},
    73:{"Name": "CPHB"},
    74:{"Name": "WSN"},
    75:{"Name": "PVP"},
    76:{"Name": "BR-SAT-MON"},
    77:{"Name": "SUN-ND"},
    78:{"Name": "WB-MON"},
    79:{"Name": "WB-EXPAK"},
    80:{"Name": "ISO-IP"},
    81:{"Name": "VMTP"},
    82:{"Name": "SECURE-VMTP"},
    83:{"Name": "VINES"},
    84:{"Name": "TTP / IPTM"},
    85:{"Name": "NSFNET-IGP"},
    86:{"Name": "DGP"},
    87:{"Name": "TCF"},
    88:{"Name": "EIGRP", "Category":"Routing"},
    89:{"Name": "OSPF", "Category":"Routing"},
    90:{"Name": "Sprite-RPC"},
    91:{"Name": "LARP"},
    92:{"Name": "MTP"},
    93:{"Name": "AX.25"},
    94:{"Name": "IPIP", "Category":"Tunnel"},
    95:{"Name": "MICP"},
    96:{"Name": "SCC-SP"},
    97:{"Name": "ETHERIP", "Category":"Tunnel"},
    98:{"Name": "ENCAP", "Category":"Tunnel"},
    99:{"Name": "Private Encryption Scheme"},
    100:{"Name": "GMTP"},
    101:{"Name": "IFMP"},
    102:{"Name": "PNNI"},
    103:{"Name": "PIM", "Category":"Multicast"},
    104:{"Name": "ARIS"},
    105:{"Name": "SCPS"},
    106:{"Name": "QNX"},
    107:{"Name": "A/N"},
    108:{"Name": "IPComp"},
    109:{"Name": "SNP"},
    110:{"Name": "Compaq-Peer"},
    111:{"Name": "IPX-in-IP", "Category":"Tunnel"},
    112:{"Name": "VRRP", "Category":"Failover"},
    113:{"Name": "PGM"},
    114:{"Name": "0-Hop Protocol"},
    115:{"Name": "L2TP", "Category":"Tunnel"},
    116:{"Name": "DDX"},
    117:{"Name": "IATP"},
    118:{"Name": "STP"},
    119:{"Name": "SRP"},
    120:{"Name": "UTI"},
    121:{"Name": "SMP"},
    122:{"Name": "SM"},
    123:{"Name": "PTP"},
    124:{"Name": "ISIS", "Category":"Routing"},
    125:{"Name": "FIRE"},
    126:{"Name": "CRTP"},
    127:{"Name": "CRUDP"},
    128:{"Name": "SSCOPMCE"},
    129:{"Name": "IPLT"},
    130:{"Name": "SPS"},
    131:{"Name": "PIPE"},
    132:{"Name": "SCTP"},
    133:{"Name": "Fibre Channel"},
    134:{"Name": "RSVP-E2E-IGNORE"},
    135:{"Name": "Mobility Header"},
    136:{"Name": "UDPLite"},
    137:{"Name": "MPLS-in-IP"},
    138:{"Name": "MANET"},
    139:{"Name": "HIP"},
    140:{"Name": "Shim6", "Category":"IPv6"},
    141:{"Name": "WESP"},
    142:{"Name": "ROHC"},
    253:{"Name": "Experimentation and Testing"},
    254:{"Name": "Experimentation and Testing"},
    255:{"Name": "Reserved"}
}
