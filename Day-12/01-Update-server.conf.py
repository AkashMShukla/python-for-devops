def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines() #It reads all lines from the file & store them in a list called lines

    with open(file_path, "w") as file:
        for line in lines:
            #if key in line:   #It may match unintended lines like: MAX_CONNECTIONS_BACKUP=100
            if line.startswith(key + "="):
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

server_config_file = 'server.conf'
key_to_update = 'MAX_CONNECTIONS'
new_value = '200'

update_server_config(server_config_file, key_to_update, new_value)