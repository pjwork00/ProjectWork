Travel planer
=========



This package provides the possibility to extract entities from books (LOC, GEP, FAC) 
and by means of an API with Google maps we are able to extract coordinates of the mentioned locations


1. Epub to text

2. Text to Spacy - NER
NLP algorithm

3. Quote extraction - loop on each NER, identifying a paragraph from period to period

4. loop over Entities with the Google API (unique values)
Add coordinates to the dataset 

5. Clustering according to the coordinates distribution

Cluster analysis, or clustering, is an unsupervised machine learning task.

It involves automatically discovering natural grouping in data. Unlike supervised learning (like predictive modeling), 
clustering algorithms only interpret the input data and find natural groups or clusters in feature space.

Clustering techniques apply when there is no class to be predicted but rather when the instances are to be divided into natural groups.

— Page 141, Data Mining: Practical Machine Learning Tools and Techniques, 2016.

A cluster is often an area of density in the feature space where examples from the domain 
(observations or rows of data) are closer to the cluster than other clusters. 
The cluster may have a center (the centroid) that is a sample or a point feature space and may have a boundary or extent.


Dependencies
------------

This package depends on the following packages:

-  Spacy
-  ebooklib
-  bs4

They can be installed using ``pip``.

::

    sudo pip install -r requirements.txt

Installation
------------

To run the following command from the top-level package
directory.

