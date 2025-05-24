#!/bin/bash
# Install dependencies required to build slides offline
set -e

sudo apt-get update
sudo apt-get install -y pandoc texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended

