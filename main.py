#!/usr/bin/python

__author__ = 'Khadim GUEYE - Colman'

import yaml 
import sys , os
from package.download_data import DownData
from package.nextstrain import nextstrain
import logging
import pandas as pd


def dropduplicates (dir_metadata):
    metadata = dir_metadata+'/data/metadata.tsv'
    df = pd.read_csv(metadata, sep="\t")
    df_unique = df.drop_duplicates(subset="strain")
    df_unique.to_csv(metadata, sep="\t", index=False)


def pathogens ():
    try:
        with open('pathogens.yaml', 'r') as file:
            pathogens = yaml.safe_load(file)
            West_Nile_virus = str(pathogens['West Nile virus'])
            Zika = str(pathogens['Zika'])
            monkeypox = str(pathogens['Monkeypox'])
            return West_Nile_virus , Zika , monkeypox
    except FileNotFoundError:
        sys.exit()


def process_virus(virus, data_dir, package_dir, virus_name):
    try:
        DownData.downdata(virus, data_dir)
        DownData.metadata_prep(data_dir, package_dir + 'data/', virus_name)
        DownData.fataprep(data_dir, package_dir + 'data/')
        dropduplicates(package_dir)
        nextstrain.precess(package_dir,virus_name)
    except Exception as ex:
        logging.error(f'Exception for {virus_name}: {ex}')

def main():
    West_Nile_virus, Zika, monkeypox = pathogens()

    # output log configuration
    logging.basicConfig(filename='output.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    viruses = {        
        'monkeypox': (monkeypox, 'data/Monkeypox', 'package/monkeypox/'),
        'west nile': (West_Nile_virus, 'data/West_Nile_virus', 'package/West_Nile/'),
        'zika': (Zika, 'data/Zika', 'package/zika/')
    }

    for virus_name, (virus, data_dir, package_dir) in viruses.items():
        process_virus(virus, data_dir, package_dir, virus_name)


    #----------------------------- view 


if __name__ == '__main__':
    main()







