import os
import sys
from datetime import datetime

from docko import *
from docko.chai import run_chai_df

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# set all cudo devices to cuda:1

if __name__ == "__main__":

    log_folder = checkNgen_folder("logs/chai/test")

    # log outputs
    f = open(os.path.join(log_folder, f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.out"), 'w')
    sys.stdout = f


    run_chai_df(
        "tests/fzl/test",
        "tests/fzl/input/test.csv",
        entry_column="Entry",
        seq_column="Sequence",
        ligand_column="Substrate",
        cofactor_column="Cofactor",
    )
    
    f.close()