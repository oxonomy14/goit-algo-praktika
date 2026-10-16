import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(
        description="Копіює файли з однієї директорії в іншу"
    )
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Шлях до директорії-джерела"
    )
    parser.add_argument("-o", "--output", type=Path, default=Path("output"))
    return parser.parse_args()


def recursive_copy(source_dir: Path, output_dir: Path):
    for item in source_dir.iterdir():
        if item.is_file():
            shutil.copy(item, output_dir)
            print(f"Скопійовано: {item.name} -> {output_dir}")
        elif item.is_dir():
            new_output_dir = output_dir / item.name
            new_output_dir.mkdir(parents=True, exist_ok=True)
            recursive_copy(item, new_output_dir)


def main():
    args = parse_argv()
    source_dir = args.source
    output_dir = args.output

    if not source_dir.is_dir():
        print(f"Помилка: {source_dir} не є директорією")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in source_dir.iterdir():
        if file_path.is_file():
            shutil.copy(file_path, output_dir)
            print(f"Скопійовано: {file_path.name} -> {output_dir}")


if __name__ == "__main__":
    main()
