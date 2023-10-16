import json

def get_ip_port(json_path):
    # Load the JSON data from the file
    with open(json_path, 'r') as file:
        data = json.load(file)

    if not 'ip' in data:
        data['ip'] = "127.0.0.1"
    if not 'port' in data:
        data['port'] =  12009
    return data['ip'], data['port']

def get_upload_dir_path(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    if not 'upload_dir' in data:
        data['upload_dir'] = './'
    return data['upload_dir']