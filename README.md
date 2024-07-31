# ENA_nextstrain_phylogeny

This repository enables the generation of phylogenetic analyses for Mpox, Zika and West Nile viruses using Nextstrain.

## Prerequisites

- [Nextstrain CLI](https://docs.nextstrain.org/en/latest/install.html)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/KhadimGueyeKgy1/ENA_nextstrain.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd ENA_nextstrain
   ```

3. **Install required Python packages:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main Python script:**
   ```sh
   python main.py
   ```

   This script will process the data and generate the necessary files for visualisation.

2. **View the results in Nextstrain's Auspice visualisation tool localy:**

   If you installed Nextstrain CLI using Conda:
   ```sh
   nextstrain view auspice_res
   ```

3. **Open your web browser and navigate to:**
   ```
   http://localhost:4000
   ```

   You should see the Auspice visualisation of your phylogenetic analysis.

The visualisation part is deployed on [GitLab](https://gitlab.ebi.ac.uk/ena-dcap/pathogen-phylogeny-monkeypox/-/tree/main/aupice_res/aupice) and the result can be viewed at this [link](https://dev.pathogensportal.org/priority-pathogens) (Nextstrain section).
