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


def get_file_size(filename: str) -> bool:
    file_size: float = float(os.path.getsize(filename)) / 1000000
    print(f"[f] File Size: {file_size:.2f} MB\n")
    return True


def scraper(filename):
    while True:
        try:
            random_wiki: str = get_wiki_text()
            unique_list: list = word_list(random_wiki)
            add_to_main_file(filename, unique_list)
            clean: list = clean_list(filename)
            file_backup(filename)
            clean_write_to_file(filename, clean)
            get_file_size(filename)
            os.unlink(filename + ".bak")
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
    (options, args) = parser.parse_args()
    if options.output is not None:
        scraper(options.output)
    else:
        parser.print_help()
    return True


if __name__ == "__main__":
    main()
