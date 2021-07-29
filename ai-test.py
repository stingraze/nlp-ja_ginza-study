#When faced with error, I had to update pip and install python-devel via yum (CentOS 7)
#Most of code from sample at: https://www.megagon.ai/jp/blog/ginza-version-4-0/
import spacy
import ginza
nlp = spacy.load("ja_ginza")
doc = nlp("東京オリンピックは２０２１年に開催されています。")
print(ginza.bunsetu_spans(doc))
print ("===============")
for np in doc.noun_chunks:
    print(np)
