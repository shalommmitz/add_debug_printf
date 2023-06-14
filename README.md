# A Python script to add debug messages to a C module

This repository contains a simple Python-3 script that adds many printf statements to a C-language module.
The "printf" statements print the executed line number and a condensed version of the code in this line.

The parsing done by the script is primitive, so likely it will break the C module and you will need to remove a few of the added lines.
Yet, I found it useful, as it produces a detailed execution log.

### Installation and Environment

Only dependency is Python 3.x

### Usage

Run: `python3 add_line_number_prints.py <filename of a C module>  > debug.c`

This will create a "debug.c" file, with the original statements and debug messages.

## Author

**Shalom Mitz** - [shalommmitz](https://github.com/shalommmitz)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE ) file

