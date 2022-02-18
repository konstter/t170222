import json


def read_file(file):
    '''Получаем структуру из json в список-дано'''
    with open(file, 'r') as f:
        json_input = f.read()
        p = json.loads(json_input)
        print(struct_to_list(p))
        return p


def struct_to_list(ps):
    '''Рекурсивно обходим список-дано, на каждой итерации
    запоминаем путь папок в новый список-путь. Если в папке
    текущей итерации есть файлы, записываем каждый файл и его 
    список-путь в кортеж и присоединяем кортеж к списку-результату.
    Если подпапок нет - удаляем текущую папку из списка-пути'''
    result = []

    def rec(paths, path_list, result):
        for path in paths:
            path_list.append(path['name'])

            if path['files']:
                for p_f in path['files']:
                    elem = (p_f, list(path_list[:]))
                    result.append(elem)

            if path['sub_folders']:
                rec(path['sub_folders'], path_list, result)

            path_list.pop()

    rec(ps, [], result)

    return result


if __name__ == "__main__":
    f_json = 'folders.json'
    read_file(f_json)
