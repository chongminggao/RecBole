
import os
import unittest

from recbole.quick_start import objective_function, run_recbole


current_path = os.path.dirname(os.path.realpath(__file__))
config_file_list = [os.path.join(current_path, "tests", "model", "test_model.yaml")]


config_dict = {"model": "GRU4Rec", "train_neg_sample_args": None}

objective_function(
        config_dict=config_dict, config_file_list=config_file_list, saved=False
    )



