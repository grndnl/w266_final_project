"""
Extract the ABC strings into a form which could be used to train
a language model
"""
import json
from pathlib import Path
from nltk.tokenize import word_tokenize
import re
import pandas as pd
import numpy as np
from tqdm import tqdm


def find_file(line):
    return line.split(".step:")[0]


def tokenize_string(text_string):
    return word_tokenize(text_string)


def find_text_strings(line):
    return re.findall(r"'(.*?)'", line, re.DOTALL)


def filter_useful_strings(text_strings):
    token_bad_list = [
        "part",
        "body",
        "desc",
        "top",
        "base",
        "bottom",
        "left",
        "right",
        "front",
        "back",
        "curve",
        "surface",
        "surf"
    ]
    filtered_strings = []
    for s in text_strings:
        tokens = tokenize_string(s)
        ltokens = set([t.lower() for t in tokens])
        bad = ltokens.intersection(token_bad_list)
        if len(bad) == 0 or len(ltokens) > 2:
            filtered_strings.append(s)

    return set(filtered_strings)


def is_brep(line):
    return line.find("MANIFOLD_SOLID_BREP") > 0


def build_string_table(file, output):
    """
    Build the string table from the file
    """
    string_table = {}
    with open(file, "r") as fp:
        lines = fp.readlines()
        for line in tqdm(lines, desc="processing lines"):
            if not is_brep(line):
                continue
            text_strings = find_text_strings(line)
            useful_strings = filter_useful_strings(text_strings)
            if len(useful_strings) > 0:
                file_name = find_file(line)
                if not file_name in string_table:
                    string_table[file_name] = set()
                string_table[file_name] = string_table[file_name].union(set(useful_strings))

    keys = [k for k in string_table]
    for key in tqdm(keys, desc="processing keys"):
        string_table[key] = list(string_table[key])

    with open(output, 'w', encoding='utf8') as fp:
        json.dump(string_table, fp, indent=4, ensure_ascii=False, sort_keys=False)


def process_assembly_text(metadata_path):
    """
    Read the metadata file, and map it to the JSON with the part names. Export one data file with `assembly_id`,
    `assembly_name`, `and assembly_part_names`.
    """
    metadata = pd.read_csv(metadata_path)

    metadata.drop_duplicates(subset='assembly_id', inplace=True)
    metadata.drop(['file_number', 'part_num'], axis=1, inplace=True)
    metadata = metadata.set_index('assembly_id')

    # Read JSON of part names
    # with open("abc_text_data.json") as f:
    with open("abc_text_data_2.json") as f:
        part_names = json.load(f)

    # Map assembly names and copy of list of part names
    metadata['part_names'] = np.empty((len(metadata), 0)).tolist()
    for k, v in part_names.items():
        assembly_name = k.split("_")[1]
        try:
            if len(metadata.at[assembly_name, 'part_names']) == 0:
                metadata.at[assembly_name, 'part_names'] = v
            else:
                metadata.at[assembly_name, 'part_names'].extend(v)
        except Exception as e:
            print(e, k)
    metadata.part_names = metadata.part_names.apply(lambda y: np.nan if len(y) == 0 else y)
    # metadata.part_names = metadata.part_names.apply(lambda y: np.nan if len(y) <= 1 else y)
    print(metadata.info())

    return metadata


def save_data(data, name):
    data.to_csv(f"{name}.csv")
    data.reset_index().to_feather(f"{name}.feather")


if __name__ == "__main__":
    all_name_lines = Path("all_name_lines.txt")
    output_raw = Path("abc_text_data_2.json")
    metadata_path = "meta.csv"
    output_processed = "data"

    build_string_table(all_name_lines, output_raw)

    metadata = process_assembly_text(metadata_path)
    save_data(metadata, output_processed)
