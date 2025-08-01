#!/bin/bash

echo "Recreating test-cities-cif environment"
conda activate base
conda remove -n test-cities-cif --all --yes
conda env create --file environment.yml --yes

echo "Switching back to test-cities-cif env"
conda activate test-cities-cif
