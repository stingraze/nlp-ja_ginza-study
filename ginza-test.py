#(C)Inspire Search 2020 Coded by Tsubasa Kato on April 22nd, 2020.
import spacy
nlp = spacy.load('ja_ginza')

doc = nlp("イギリス、ドイツ、フランス、イタリアの各国、ウィンストン・チャーチル、加藤清正")
for ent in doc.ents:
	if ent.label_ == "LOC":
		print("location found")
		print(ent.text)
	if ent.label_ == "PERSON":
		print("person found")
		print (ent.text)
