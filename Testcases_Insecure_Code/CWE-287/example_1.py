def authenticate_request(ip_address):
    # Allow access if the IP address is in the trusted list
    trusted_ips = ['192.168.1.100', '192.168.1.101']
    if ip_address in trusted_ips:
        return True
    return False

if authenticate_request(request.ip):
    robot.execute_command('move_forward')