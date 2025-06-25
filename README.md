# SBDH-Reader
## Introduction
Social and behavioral determinants of health (SBDH) are increasingly recognized as essential for prognostication and informing targeted interventions. Clinical notes often contain details about SBDH in unstructured format. Conventional extraction methods for these data tend to be labor intensive, inaccurate, and/or unscalable. In this study, we aim to develop and validate an LLM-powered method to extract structured SBDH data from clinical notes through prompt engineering. We developed SBDH-Reader to extract six categories of granular SBDH data by prompting GPT-4o, including employment, housing, marital status, and substance use including alcohol, tobacco, and drug use. SBDH-Reader was developed using 7,225 notes from 6,382 patients in the MIMIC-III database (2001–2012) and externally validated using 971 notes from 437 patients at The University of Texas Southwestern Medical Center (UTSW; 2022–2023). We evaluated SBDH-Reader’s performance against human-annotated ground truths based on precision, recall, F1, and confusion matrix. To conclude, we found that a general-purpose LLM can accurately extract structured SBDH data through effective prompt engineering. The SBDH-Reader has the potential to serve as a scalable and effective method for collecting real-time, patient-level SBDH data to support clinical research and care.

## Getting started
- `conda create -n sbdh_reader python=3.9` creating a new conda env
- `conda activate sbdh_reader`
- `pip install -r requirements.txt` installs specific packages for the wrapper function
- Note: Compatibility test done on the following Linux systems: `Red Hat Enterprise Linux 7.9`; 

## Usage
TL;DR: `python example_call.py` runs SBDH-Reader end-to-end, from free text to LLM's structured json output.

`cats.py` contains the granular attribute definition of the six SBDH categories: employment, housing, marital status, and substance use including alcohol, tobacco, and drug use.

`caller.py` composes the SBDH categories of interest with a global starter, output specifications, and global finisher.

# Citation
If you find this work useful, please cite us: Gu Z, He L, Naeem A, Chan PM, Mohamed A, Khalil H, Guo Y, Shi W, Dupre ME, Xiao G, Peterson ED, Xie Y, Navar AM, Yang DM. SBDH-Reader: an LLM-powered method for extracting social and behavioral determinants of health from medical notes. medRxiv [Preprint] (2025). DOI: 10.1101/2025.02.19.25322576