# Wiki Word Scraper

This tool scrapes words from random Wikipedia pages and saves them to a file.

Wordlist file is one entry per line, all lowercase. No numbers, no special characters, no spaces.

## Installation

```shell
$ git clone https://github.com/juliojimenez/wiki-word-scraper
$ cd wiki-word-scraper
$ pip install -r requirements.txt
```

## Basic Usage

```shell
$ python3 wws.py -o|--output out.txt
```

or 

```shell
$ ./wws.py -o out.txt
```

`CTRL-C` to quit

## Options

### Output

Sets the output file. Required.

```shell
$ python3 wws.py -o|--output out.txt
```

### Words

Minimum number of words the list should contain before execution stops. If the number set by this option is less than the result of scraping one wiki, after other size and word length constraints, then the latter will be the final list result.

```shell
$ python3 wws.py --words|-w 1000 -o out.txt
```

### Size

Size of wordlist file. Unit can be expressed in TB, GB, MB, KB, or B. Units are case insensitive.

```shell
$ python3 wws.py --size|-s 1mb -o out.txt
```

### Minimum Word Length

Minimum word length in characters.

```shell
$ python3 wws.py --min-length|-n 3 -o out.txt
```

### Maximum Word Length

Maximum word length in characters.

```shell
$ python3 wws.py --max-length|-x 6 -o out.txt
```
