#!/usr/bin/env python
# -*- coding: utf-8 -*-

characteristics_dict = {
    "black": "CCAGCAATCGC", "Brown": "GCCAGTGCCG", "Blonde": "TTAGCTATCGC",
    "Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA",
    "Blue": "TTGTGGTGGC", "Green": "GGGAGGTGGC", "Dark": "AAGTAGTGAC",
    "Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC",
    "White": "AAAACCTCA", "Black": "CGACTACAG", "Asian": "CGCGGGCCG"}

sample_file = open ("sample.txt", "r")
dna = sample_file.read()

guilty = []
for key, value in characteristics_dict.iteritems():
    if dna.find(value) != -1:
        guilty.append(key)

sample_file.close()

print "Guilty characteristics are: "
for item in guilty:
    print "- " + item

suspect_dict = {
    "Eva": "[Female, White, Blonde, Blue, Oval]",
    "Larisa": "[Female, White, Brown, Dark, Oval]",
    "Matej": "[Male, White, Black, Blue, Oval]",
    "Miha": "[Male, White, Brown, Green, Square]"
}

for key, value in suspect_dict.iteritems():
    if all(elem in value for elem in guilty):
        print "The person who ate the chocolate ice-cream is " + key

print "Thank you to use our services."








