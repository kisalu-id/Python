import ipaddress

def expand_ipv6(ipv6_address: str) -> str:
    """Convert compressed IPv6 address to full (expanded) form."""
    try:
        return ipaddress.IPv6Address(ipv6_address).exploded
    except ipaddress.AddressValueError as e:
        raise ValueError(f"Invalid IPv6 address: {ipv6_address}") from e


def compress_ipv6(ipv6_address: str) -> str:
    """Convert full IPv6 address to compressed form."""
    try:
        return ipaddress.IPv6Address(ipv6_address).compressed
    except ipaddress.AddressValueError as e:
        raise ValueError(f"Invalid IPv6 address: {ipv6_address}") from e


def main():
    test_addresses = [
        "2001:0db8:0000:08d3:0000:8a2e:0070:7344",
        "2001:db8:0:8d3:0:8a2e:70:7344",
        "2001:db8::1428:57ab",
        "2001:0db8:1234:0000:0000:0000:0000:0000",
        "2001:DB8::"
    ]

    for address in test_addresses:
        try:
            expanded = expand_ipv6(address)
            compressed = compress_ipv6(address)
            print(f"Original:   {address}")
            print(f"Expanded:   {expanded}")
            print(f"Compressed: {compressed}")
            print("-" * 40)
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    main()
