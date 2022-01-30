# hack2022-05-cross-talk
Challenge 5: Detect and correct spatial cross-talk

## Motivation
Novel multiplexed imaging tools hold great promise for characterizing interactions within dense tissues, at the single cell level and in situ. The number of multiplexed images currently being produced via platforms such as PerkinElmer Vectra, CODEX, MERFISH, smFISH, Ionpath MIBI, NanoString Technologies is growing rapidly. Many of these technologies boast of capturing multiple protein markers within a single image bringing in a wealth of information in terms of the cells as well as their spatial contexts. 
To take full advantage of the basic science and clinical potential of such spatial technologies, various challenges - some unique to certain platforms and some shared across platforms - such as cell segmentation, cellular feature extraction must first be addressed. In a typical multiplexed image with 7 or more markers, more than half of the pixels go unsegmented. This is mainly due to the uncertainty in cell boundaries and is further compounded by the technical noise across protein markers in the image.  Inaccurate cell segmentation in dense tissue creates conditions in which signals from adjacent cells spatially “bleed” into each other, which leads to the creation of nonsensical cell states as determined by unsupervised clustering methods. 

## Goal of the Challenge
Recent efforts have led to the development of a novel spatial cross-talk correction method called REinforcement Dynamic Spillover EliminAtion (REDSEA, PMID: 34295327). This challenge proposes the evaluation of this method’s performance on datasets exhibiting lateral spillover and its benchmarking against alternative methods that seek to improve performance.
## Check in times 
* Zoom hours:
  * 11.30am-12.30pm 
  * 10.00pm-11.00pm 
  * Link: https://us02web.zoom.us/j/85687379145?pwd=bW0vbFRJYTFEZUJmTXgvS1VMMnNZUT09
* Team Slack: 05-cross-talk
