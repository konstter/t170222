"""Необходимо написать программу (класс/функция) на языке python, цель которой - собрать пути ко всем файлам
в иерархии папок. Для простоты представим иерархию папок в виде обычного списка (list).

Например, для иерархии вида:

folders = [
    {
        name: folder_1,
        sub_folders: [
            {
                name: inner_folder,
                sub_folders: [],
                files: [
                    file1,
                    file2
                ]
            }
        ],
        files: [
            another_file
        ]
    }
]

должна получиться структура (любая из или их комбинация: список, словарь, кортеж и т.д.), содержащая 3 элемента:

- Название: another_file, путь: [folder_1],
- Название: file1, путь: [folder_1, inner_folder],
- Название: file2, путь: [folder_1, inner_folder],

Например:

{
    another_file: [folder_1],
    file1: [folder_1, inner_folder],
    file2: [folder_1, inner_folder]
}

Иерархию папок необходимо взять из приложенного файла folders.json.

"""
