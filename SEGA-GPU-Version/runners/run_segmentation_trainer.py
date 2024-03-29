### Ecosystem Imports ###
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from typing import Union
import pathlib

### External Imports ###
import numpy as np
import torch as tc
from torch.utils.tensorboard import SummaryWriter

### Internal Imports ###
from paths import hpc_paths as p
from training import segmentation_trainer as st
from runners.hpc_experiments import sega_experiments as sega
########################


def initialize(training_params):
    experiment_name = training_params['experiment_name']
    num_iterations = training_params['num_iterations']
    save_step = training_params['save_step']
    checkpoints_path = os.path.join(p.checkpoints_path, experiment_name)
    checkpoints_iters = list(range(0, num_iterations, save_step))
    log_image_iters = list(range(0, num_iterations, save_step))
    if not os.path.isdir(checkpoints_path):
        os.makedirs(checkpoints_path)
    log_dir = os.path.join(p.logs_path, experiment_name)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    logger = SummaryWriter(log_dir=log_dir, comment=experiment_name)
    training_params['logger'] = logger
    training_params['checkpoints_path'] = checkpoints_path
    training_params['checkpoint_iters'] = checkpoints_iters
    training_params['log_image_iters'] = log_image_iters
    return training_params

def run_training(training_params):
    training_params = initialize(training_params)
    trainer = st.SegmentationTrainer(**training_params)
    trainer.run()

def run():
    params = sega.get_experiment_final_4()
    run_training(params)


if __name__ == "__main__":
    run()
















# ### Ecosystem Imports ###
# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), "."))
# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# from typing import Union
# import pathlib

# ### External Imports ###
# import numpy as np
# import torch as tc
# from torch.utils.tensorboard import SummaryWriter

# ### Internal Imports ###
# from paths import hpc_paths as p
# from training import segmentation_trainer as st
# from runners.hpc_experiments import sega_experiments as sega
# ########################


# def initialize(training_params):
#     experiment_name = training_params['experiment_name']
#     num_iterations = training_params['num_iterations']
#     save_step = training_params['save_step']
#     checkpoints_path = os.path.join(p.checkpoints_path, experiment_name)
#     # checkpoints_path = os.path.join(p.checkpoints_path)
#     # to_load_checkpoint_path = os.path.join(p.checkpoints_path)
#     checkpoints_iters = list(range(0, num_iterations, save_step))
#     log_image_iters = list(range(0, num_iterations, save_step))
#     if not os.path.isdir(checkpoints_path):
#         os.makedirs(checkpoints_path)
#     # log_dir = os.path.join(p.logs_path)
#     log_dir = os.path.join(p.logs_path, experiment_name)
#     if not os.path.isdir(log_dir):
#         os.makedirs(log_dir)
#     logger = SummaryWriter(log_dir=log_dir, comment=experiment_name)
#     training_params['logger'] = logger
#     training_params['checkpoints_path'] = checkpoints_path
#     training_params['checkpoint_iters'] = checkpoints_iters
#     training_params['log_image_iters'] = log_image_iters
#     return training_params

# def run_training(training_params):
#     training_params = initialize(training_params)
#     trainer = st.SegmentationTrainer(**training_params)
#     trainer.run()

# def run():
#     params = sega.get_experiment_final_4()
#     run_training(params)


# if __name__ == "__main__":
#     run()
    
    
# def initialize(training_params):
#         experiment_name = training_params['experiment_name']
#         num_iterations = training_params['num_iterations']
#         save_step = training_params['save_step']
#         # checkpoints_path = os.path.join(p.checkpoints_path, experiment_name)
#         checkpoints_path = os.path.join(p.checkpoints_path)
#         to_load_checkpoint_path = os.path.join(p.checkpoints_path)
#         checkpoints_iters = list(range(0, num_iterations, save_step))
#         log_image_iters = list(range(0, num_iterations, save_step))
#         # if not os.path.isdir(checkpoints_path):
#             # os.makedirs(checkpoints_path)
#         log_dir = os.path.join(p.logs_path)
#         # log_dir = os.path.join(p.logs_path, experiment_name)
#         # if not os.path.isdir(log_dir):
#             # os.makedirs(log_dir)
#         logger = SummaryWriter(log_dir=log_dir, comment=experiment_name)
#         training_params['logger'] = logger
#         training_params['checkpoints_path'] = checkpoints_path
#         training_params['to_load_checkpoint_path'] = to_load_checkpoint_path
#         training_params['checkpoint_iters'] = checkpoints_iters
#         training_params['log_image_iters'] = log_image_iters
#         return training_params

# def run_training(training_params):
#         training_params = initialize(training_params)
#         trainer = st.SegmentationTrainer(**training_params)
#         trainer.run()

# def run():
#         params = sega.get_experiment_final_4()
#         run_training(params)


# if __name__ == "__main__":
#         run()