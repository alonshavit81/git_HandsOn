#!/usr/bin/env python
"""
seqClass.py
Classify an input nucleotide sequence as DNA, RNA, or ambiguous (could be either).
Optionally, search for a motif inside the sequence.
"""

import sys
import re
from argparse import ArgumentParser

# CLI (command-line interface)
# We use argparse so the script can be run like:
#   python seqClass.py -s actg
#   python seqClass.py -s actg -m tg
parser = ArgumentParser(description="Classify a sequence as DNA or RNA")

# Required input: the nucleotide sequence to classify
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

# Optional input: a motif pattern to search for in the sequence
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search for")

# If the user runs the script with no arguments, show help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse CLI arguments into the args object (args.seq, args.motif, ...)
args = parser.parse_args()

# Normalization / cleaning step
# Convert input to uppercase so the regex checks work even if the user provided
# lowercase letters (e.g., "actg" -> "ACTG").
args.seq = args.seq.upper()

# Validate and classify sequence
# First check that the sequence contains only A/C/G/T/U.
# if it contains other characters (e.g., N, X, numbers), it is invalid.
if re.search(r"^[ACGTU]+$", args.seq):
    has_t = "T" in args.seq
    has_u = "U" in args.seq

 # A sequence containing both T and U is inconsistent.
    if has_t and has_u:
        print("The sequence is not DNA or RNA")

    # DNA contains T and no U
    elif has_t:
        print("The sequence is DNA")

     # RNA contains U and no T       
    elif has_u:
        print("The sequence is RNA")

    # Only A/C/G: could be DNA or RNA
    else:
        print("The sequence can be DNA or RNA")
        
else:
    print("The sequence is not DNA nor RNA")


# motif search feature
# If the user provided a motif (args.motif is not None/empty),
# search for it inside the normalized sequence.
if args.motif:
    # Normalize motif to uppercase to match args.seq
    args.motif = args.motif.upper()

    # Inform the user what we are searching for
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end="")

    # Search for the motif anywhere in the sequence
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
