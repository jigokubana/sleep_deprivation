import os
import csv


def append_csv_row(filepath: str, headers: list[str], row: list) -> None:
    folder = os.path.dirname(filepath)
    if folder:
        os.makedirs(folder, exist_ok=True)
    need_headers = (
        not os.path.exists(filepath)
        or os.path.getsize(filepath) == 0
    )
    with open(filepath, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if need_headers:
            writer.writerow(headers)
        writer.writerow(row)
