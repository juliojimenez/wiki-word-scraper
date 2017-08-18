# Wiki Word Scraper

This python script scrapes words from random w1k1p3d1a pages and saves them to a wordlist file.  That's it! ;-)

Wordlist file is one entry per line, all lowercase. No numbers, no special characters, no spaces. This mangling is left to others, like John.

# Usage

`./wiki-word-scraper -o file.name`

or 

`python wiki-word-scraper -o filename.whatever`

`CTRL-C` to quit

## Dependencies

[**requests**](http://docs.python-requests.org/en/master/)

If you don't have it just **`pip install requests`** it.

# Tests

**20170817** - Been running wws for about 3 hours, it created a file called wordlist.lst. So far it has close to 500000 entries. It was stopped and started a few times and kept on going just fine.

# Release Notes

- 0.0.2 - Put it all in a loop
- 0.0.1 - Initial
