# Entity linking batch CLI

This utility is made to launch batch requests against the entity linker, based on the contents of a CSV.

Usage

    usage: main.py [-h] [--mode {annotate,metrics}] [--csv CSV] [--url URL]

    Entity Linker

    optional arguments:
        -h, --help            show this help message and exit
        --mode {annotate,metrics}
                              Choose between the operating modes
        --csv CSV             Filepath for the CSV to annotate
        --url URL             URL of the linker endpoint


