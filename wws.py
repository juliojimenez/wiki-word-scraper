#!/usr/bin/python3
from optparse import OptionParser
import requests
import re
import os
import shutil as copy


def get_wiki_text() -> str:
    url: str = "https://www.wikipedia.org/wiki/Special:Random"
    random_wiki: requests.Response = requests.get(url)
    print(f"[w] Scraping {random_wiki.url}")
    return random_wiki.text


def word_list(wiki_text: str) -> list:
    regex: list = re.findall(r"[a-zA-Z]+", wiki_text)
    lower_list: list = [x.lower() for x in regex]
    print(f"[w] Total Words: {len(lower_list)}")
    unique_list: list = list(set(lower_list))
    print(f"[w] Unique Words: {len(unique_list)}")
    return unique_list


def add_to_main_file(filename: str, unique_list: list) -> bool:
    with open(filename, "a") as f:
        for x in unique_list:
            f.write(f"{x}\n")
    return True


def clean_list(filename: str) -> list:
    clean: list
    with open(filename, "r") as f:
        dirty: list = []
        for x in f:
            dirty.append(x[:-1])
        clean = list(set(dirty))
        clean.sort()
        print(f"\n[f] Total words in file: {len(clean)}")
    return clean


def file_backup(filename: str) -> bool:
    copy.copyfile(filename, f"{filename}.bak")
    os.unlink(filename)
    return True


def clean_write_to_file(filename: str, clean_list: list) -> bool:
    with open(filename, "a") as f:
        for x in clean_list:
            f.write(f"{x}\n")
    return True


def get_file_size(filename: str) -> float:
    file_size: float = float(os.path.getsize(filename)) / 1000000
    print(f"[f] File Size: {file_size:.2f} MB\n")
    return file_size


def check_word_count(words: int, word_list: list) -> bool:
    if words > 0 and len(word_list) > words:
        return True
    else:
        return False


def validate_size(size_string: str) -> float:
    validator = re.search(
        r"^([0-9]*)(TB|GB|MB|KB|B|Tb|Gb|Mb|Kb|tB|gB|mB|kB|tb|gb|mb|kb|b)$",
        size_string,
    )
    if validator is not None:
        if (
            validator.group(2) == "TB"
            or validator.group(2) == "Tb"
            or validator.group(2) == "tB"
            or validator.group(2) == "tb"
        ):
            return float(validator.group(1)) * 1000000
        if (
            validator.group(2) == "GB"
            or validator.group(2) == "Gb"
            or validator.group(2) == "gB"
            or validator.group(2) == "gb"
        ):
            return float(validator.group(1)) * 1000
        if (
            validator.group(2) == "MB"
            or validator.group(2) == "Mb"
            or validator.group(2) == "mB"
            or validator.group(2) == "mb"
        ):
            return float(validator.group(1))
        if (
            validator.group(2) == "KB"
            or validator.group(2) == "Kb"
            or validator.group(2) == "kB"
            or validator.group(2) == "kb"
        ):
            return float(validator.group(1)) * 0.001
        if validator.group(2) == "B" or validator.group(2) == "b":
            return float(validator.group(1)) * 0.000001
    else:
        return -1


def min_length(word_list: list, length: int) -> list:
    min_length_words: list = []
    for word in word_list:
        if len(word) >= length:
            min_length_words.append(word)
    return min_length_words


def max_length(word_list: list, length: int) -> list:
    max_length_words: list = []
    for word in word_list:
        if len(word) <= length:
            max_length_words.append(word)
    return max_length_words


def scraper(filename: str, words: int, size: float, min: int, max: int):
    while True:
        try:
            random_wiki: str = get_wiki_text()
            unique_list: list = word_list(random_wiki)
            if min > 0:
                unique_list = min_length(unique_list, min)
            if max > 0:
                unique_list = max_length(unique_list, max)
            add_to_main_file(filename, unique_list)
            clean: list = clean_list(filename)
            file_backup(filename)
            clean_write_to_file(filename, clean)
            os.unlink(f"{filename}.bak")
            file_size: float = get_file_size(filename)
            if check_word_count(words, clean):
                return True
            if size > 0 and file_size >= size:
                return True
        except KeyboardInterrupt:
            print(" Thanks for playing!")
            break
    return True


def main():
    print("")
    print(" Wiki Word Scraper")
    print(" Julio Jimenez")
    print("")
    usage = "Usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option(
        "-o",
        "--output",
        action="store",
        type="string",
        dest="output",
        help="Output wordlist file.",
    )
    parser.add_option(
        "-w",
        "--words",
        type="int",
        dest="words",
        default=0,
        help=(
            "Minimum number of words the list shall "
            "contain before execution stops."
        ),
    )
    parser.add_option(
        "-s",
        "--size",
        type="string",
        dest="size",
        help="Size of wordlist file. TB, GB, MB, KB, B, case insensitive.",
    )
    parser.add_option(
        "-n",
        "--min-length",
        type="int",
        dest="min_word_length",
        default=0,
        help="Minimum word length (characters).",
    )
    parser.add_option(
        "-x",
        "--max-length",
        type="int",
        dest="max_word_length",
        default=0,
        help="Maximum word length (characters).",
    )
    (options, args) = parser.parse_args()
    if options.output is not None:
        size: float = 0
        if options.size is not None:
            size = validate_size(options.size)
            if size < 0:
                print("[x] Invalid --size -s option.")
                parser.print_help()
                return True
        scraper(
            options.output,
            options.words,
            size,
            options.min_word_length,
            options.max_word_length,
        )
    else:
        parser.print_help()
    return True


if __name__ == "__main__":
    main()
