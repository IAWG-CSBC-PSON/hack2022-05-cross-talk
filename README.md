# hack2022-05-cross-talk
Challenge 5: Detect and correct spatial cross-talk

## Motivation
Novel multiplexed imaging tools hold great promise for characterizing interactions within dense tissues, at the single cell level and in situ. The number of multiplexed images currently being produced via platforms such as PerkinElmer Vectra, CODEX, MERFISH, smFISH, Ionpath MIBI, NanoString Technologies is growing rapidly. Many of these technologies boast of capturing multiple protein markers within a single image bringing in a wealth of information in terms of the cells as well as their spatial contexts. 
To take full advantage of the basic science and clinical potential of such spatial technologies, various challenges - some unique to certain platforms and some shared across platforms - such as cell segmentation, cellular feature extraction must first be addressed. In a typical multiplexed image with 7 or more markers, more than half of the pixels go unsegmented. This is mainly due to the uncertainty in cell boundaries and is further compounded by the technical noise across protein markers in the image.  Inaccurate cell segmentation in dense tissue creates conditions in which signals from adjacent cells spatially “bleed” into each other, which leads to the creation of nonsensical cell states as determined by unsupervised clustering methods. 

## Goal of the Challenge
Recent efforts have led to the development of a novel spatial cross-talk correction method called REinforcement Dynamic Spillover EliminAtion (REDSEA, PMID: 34295327). This challenge proposes the evaluation of this method’s performance on datasets exhibiting lateral spillover and its benchmarking against alternative methods that seek to improve performance.

## Prerequisites
* REDSEA
  * Paper: Bai Yunhao, Zhu Bokai, Rovira-Clave Xavier, Chen Han, Markovic Maxim, Chan Chi Ngai, Su Tung-Hung, McIlwain David R., Estes Jacob D., Keren Leeat, Nolan Garry P., Jiang Sizun, “Adjacent Cell Marker Lateral Spillover Compensation and Reinforcement for Multiplexed Images” , Frontiers in Immunology, vol 12, 2021. Link: URL=https://www.frontiersin.org/article/10.3389/fimmu.2021.652631. DOI=10.3389/fimmu.2021.652631    
  * Tweetorial: https://twitter.com/sizunj/status/1412189614668861441
  * Matlab Code and data : https://github.com/nolanlab/REDSEA. Check if you have a running implementation of REDSEA on either the MIBI or t-CyCIF tonsil data provided in the repo.
 
* Deepcell/Mesmer
  * To generate cell segmentations for the images: check the segmentation code using Deepcell/MESMER as provided in the REDSEA code repository: https://github.com/nolanlab/REDSEA/tree/master/code or 
  * Check the MESMER implementation according to the Deepcell guide for CyCIF: https://github.com/vanvalenlab/intro-to-deepcell/blob/master/README.md and https://github.com/vanvalenlab/deepcell-tf/blob/master/notebooks/applications/Mesmer-Application.ipynb

* Software 
  * Matlab : since REDSEA is implemented in Matlab
  * Any software of choice (e.g. Matlab, Python, R, Julia) for benchmarking and subsequent data analysis

* Datasets 
  * Whole slide Tonsil images processed using different imaging technologies: https://mcmicro.org/datasets.html
	
## Check in times 
* Zoom hours:
  * 1.00pm-2.00pm (Feb 16th, 17th)
  * 10.00pm-11.00pm (Feb 15th-17th)
  * Link: https://us02web.zoom.us/j/85687379145?pwd=bW0vbFRJYTFEZUJmTXgvS1VMMnNZUT09
* Team Slack: 05-cross-talk

## Final team presentations
February 18th 12-3pm ET (9am-12pm PT)
 * Team 5 tentative slot: 1:00pm-1:15pm
