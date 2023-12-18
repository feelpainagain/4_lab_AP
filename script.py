import os

import pandas as pd


def scan_dataset(folder_paths: list[str]) -> list[list[str]]:
    """This function scans given datasets and returns them in a form that can be saved as csv.

    Args:
        folder_paths (list[str]): Paths to datasets to be scanned.

    Returns:
        list[list[str]]: Data in a form of table of strings.
    """
    result = []
    for folder in folder_paths:
        item_class = folder.split('\\')[-1]
        for name in os.listdir(folder):
            result.append([os.path.abspath(folder + '\\' + name), f'{folder}\\{name}', item_class])
    return result


def save_as_csv(to_save: list[list[str]], columns: list[str], relpath: str) -> None:
    """Saves given data table as csv

    Args:
        to_save (list[list[str]]): Table (matrix) of strings to be saved, formatted as in scan_dataset.

        columns (list[str]): Name of data's columns.

        relpath (str): Relative path where data is to be saved.
    """
    df = pd.DataFrame(to_save, columns=columns)
    df.to_csv(relpath, sep=";")
    print(f'Successfully saved in {relpath}')


if __name__ == "__main__":
    data = scan_dataset(["dataset\\tiger", "dataset\\leopard"])
    columns = data.pop(0)
    save_as_csv(data, columns, "annotation.csv")