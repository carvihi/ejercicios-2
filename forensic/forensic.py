#!/usr/bin/env python
# -*- coding: utf-8 -*-

characteristics_dict = {
    "hair_black": "CCAGCAATCGC", "hair_Brown": "GCCAGTGCCG", "hair_Blonde": "TTAGCTATCGC",
    "face_Square": "GCCACGG", "face_Round": "ACCACAA", "face_Oval": "AGGCCTCA",
    "eye_Blue": "TTGTGGTGGC", "eye_Green": "GGGAGGTGGC", "eye_Dark": "AAGTAGTGAC",
    "gender_Female": "TGAAGGACCTTC", "gender_Male": "TGCAGGAACTTC",
    "race_White": "AAAACCTCA", "race_Black": "CGACTACAG", "race_Asian": "CGCGGGCCG"}

sample_file = open ("sample.txt", "r")
dna = sample_file.read()
sample_file.close()

guilty = []
for key, value in characteristics_dict.iteritems():
    if dna.find(value) != -1:
        guilty.append(key)


print "Guilty characteristics are: "
for item in guilty:
    print "- " + item

suspect_dict = {
    "Eva": "[gender_Female, race_White, hair_Blonde, eye_Blue, face_Oval]",
    "Larisa": "[gender_Female, race_White, hair_Brown, eye_Dark, face_Oval]",
    "Matej": "[gender_Male, race_White, hair_Black, eye_Blue, face_Oval]",
    "Miha": "[gender_Male, race_White, hair_Brown, eye_Green, face_Square]"
}

for key, value in suspect_dict.iteritems():
    if all(elem in value for elem in guilty):
        print "The person who ate the chocolate ice-cream is " + key

print ("_" * 51)

print "Thank you to use our services."








