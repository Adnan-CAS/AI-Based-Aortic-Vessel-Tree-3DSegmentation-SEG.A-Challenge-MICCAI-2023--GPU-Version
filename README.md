# SEG.A-Challenge-MICCAI-2023--GPU-Version

This project has modified the repository by Marek Wodzinski [Link](https://github.com/MWod/SEGA_MW_2023.git)

The original network was trained using HPC infrastructure (PLGRID). To reproduce the network on personal GPUs the following modifications are required:

# Main Contributions for Reproducibility

•	To Download the SEG.A dataset [Link](https://multicenteraorta.grand-challenge.org/data/)


•	Update the paths in both hpc_paths.py and paths.py files.

•	Run the parse_sega.py

•	Put all the newly generated files in the folder 'PRASEDSHAPE_400_400_400'

•	Rename the path in both parsed training and validation CSV e.g: PARSEDShape_400_400_400Dongyang_13.seg.nrrd, Note change both the input path and   GT path

•	Rename the newly generated folder as PARSEDElasticShape_400_400_400_V2

•	Rename the path in newly generated CSV ’elasticaug400_v2_training_dataset’, note: change the \ to /

•	For Augmentation: Run the run_aug_sega.py

•	For Training: Run the training using run_segmentation_trainer.py

•	For visualization: the images are logged in the logs folder
