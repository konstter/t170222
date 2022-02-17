import json


def read_file(file):
    with open(file, 'r') as f:
        json_input = f.read()
        p = json.loads(json_input)
        struct_to_list(p, [])


def struct_to_list(paths, path_list):
    for path in paths:
        path_list.append(path['name'])
        if path['sub_folders']:
            if path['files']:
                print(path['files'], '|', path_list)
            struct_to_list(path['sub_folders'], path_list)
        else:
            print(path['files'], '|', path_list)

       path_list = []


if __name__ == "__main__":
    f_json = 'folders.json'
    read_file(f_json)
