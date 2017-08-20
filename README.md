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

**20170817** - Been running wws for about 3 hours, it created a file called wordlist.lst. So far it has close to 500000 unique entries. It was stopped and started a few times and kept on going just fine.

**20170819** - Kept running it on the same file, got it up to 763661 entries. Played a little game of grepping the file for whatever word I could think of, there was very little I couldn't find in that file, lol.

Don't be discouraged if after 500,000 words you're not seeing aggressive increases in your wordlist. According to [Oxford](https://en.oxforddictionaries.com/explore/how-many-words-are-there-in-the-english-language), the Second Edition of the 20-volume Oxford English Dictionary contains full entries for 171,476 words in current use, and 47,156 obsolete words. So really, after 250,000 it's pretty much all nouns and extraneous stuff.

# Release Notes

- 0.0.3 - Save temporary backup of wordlist file in the dupe cleanup and sorting process
- 0.0.2 - Put it all in a loop
- 0.0.1 - Initial
