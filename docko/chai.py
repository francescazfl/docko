###############################################################################
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from __future__ import annotations

from pathlib import Path
import os
import torch
from ast import literal_eval
import pandas as pd
from chai_lab.chai1 import run_inference
from docko.helpers import *


def run_chai(label: str, seq: str, smiles: str, output_dir: str, cofactor_smiles:list|str = "", joinsubcofactor:bool=True) -> None:
    """
    Run CHAI on a single protein-ligand pair.

    Args:
    - label (str): label for the protein-ligand pair
    - seq (str): sequence of the protein
    - smiles (str): SMILES string of the ligand
    - output_dir (str): output directory
    - cofactor_smiles (list or str): list of SMILES strings of cofactors, default is ""
    - joinsubcofactor (bool): whether to join the substrate and cofactor in the same fasta file, default is True
    """

    # make sure output dir is dir
    output_subdir = os.path.join(output_dir, label)

    # Need to clean up the sequence
    seq = seq.strip().replace("*", "").replace(" ", "").upper()

    example_fasta = f">protein|{label}\n{seq}\n"

    if cofactor_smiles != "":
        # convert if cofactor_smiles to a list if it is a string
        if isinstance(cofactor_smiles, str):
            # use ast.literal_eval to convert string to list
            try:
                cofactor_smiles = literal_eval(cofactor_smiles)
            except:
                cofactor_smiles = [cofactor_smiles]

        # add cofactor SMILES to the fasta
        for cofactor_smile in cofactor_smiles:
            example_fasta += f">ligand|{label}-cofactor\n{cofactor_smile}\n"

    # now add substrate
    example_fasta += f">ligand|{label}-substrate\n{smiles}\n"

    if not os.path.exists(output_subdir):
        os.system(f"mkdir {output_subdir}")
        output_subdir = Path(checkNgen_folder(output_subdir))
        smiles = canonicalize_smiles(smiles)
        # CHeck this is OK
        if smiles:
            fasta_path = Path(f"{output_subdir}/{label}.fasta")
            fasta_path.write_text(example_fasta)

            output_paths = run_inference(
                fasta_file=fasta_path,
                output_dir=output_subdir,
                # 'default' setup
                num_trunk_recycles=3,
                num_diffn_timesteps=200,
                seed=42,
                device=torch.device("cuda:0"),
                use_esm_embeddings=True,
            )
    else:
        print(f"Output directory exists: {output_subdir}")


def run_chai_df(
    output_dir: str,
    filename: str,
    entry_column: str ="Entry",
    seq_column: str="Sequence",
    ligand_column: str="Substrate",
    cofactor_column: str="Cofactor",
):
    """
    Run on a dataframe!

    Args:
    - output_dir (str): output directory
    - filename (str): filename of the dataframe
    - entry_column (str): column name for the entry
    - seq_column (str): column name for the sequence
    - ligand_column (str): column name for the ligand
    - cofactor_column (str): column name for the cofactor that has A LIST of SMILES strings
    """

    df = pd.read_csv(filename)

    if cofactor_column not in df.columns:
        df[cofactor_column] = ""

    for label, seq, smiles, cofactor_smiles in df[
        [entry_column, seq_column, ligand_column, cofactor_column]
    ].values:
        run_chai(
            label=label,
            seq=seq,
            smiles=smiles,
            output_dir=checkNgen_folder(output_dir),
            cofactor_smiles=cofactor_smiles,
        )