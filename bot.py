import re

def read_proxies(file_path):
    """Read proxies from a file and return them as a list."""
    with open(file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]

def validate_proxy(proxy):
    """Validate the proxy format."""
    # Regex pattern for IP:PORT format
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$')
    if pattern.match(proxy):
        return True
    return False

def add_prefix(proxy, prefix):
    """Add the specified prefix to the proxy if not present."""
    if not proxy.startswith((prefix, 'https://', 'socks5://')):
        return prefix + proxy
    return proxy

def format_proxies(proxies, prefix):
    """Format and validate a list of proxies with the specified prefix."""
    valid_proxies = []
    for proxy in proxies:
        if validate_proxy(proxy):
            valid_proxies.append(add_prefix(proxy, prefix))
        else:
            print(f"Invalid proxy format: {proxy}")
    return valid_proxies

def write_proxies(file_path, proxies):
    """Write proxies to a file."""
    with open(file_path, 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")

def main():
    input_file = 'input_proxies.txt'
    output_file = 'formatted_proxies.txt'
    
    # Display options to the user
    print("Choose the proxy format:")
    print("1. HTTP")
    print("2. HTTPS")
    print("3. SOCKS")
    
    choice = input("Enter the number corresponding to your choice: ")
    
    # Determine the prefix based on user choice
    if choice == '1':
        prefix = 'http://'
    elif choice == '2':
        prefix = 'https://'
    elif choice == '3':
        prefix = 'socks5://'
    else:
        print("Invalid choice. Defaulting to HTTP.")
        prefix = 'http://'
    
    proxies = read_proxies(input_file)
    formatted_proxies = format_proxies(proxies, prefix)
    write_proxies(output_file, formatted_proxies)
    print(f"Formatted proxies have been written to {output_file}")

if __name__ == "__main__":
    main()