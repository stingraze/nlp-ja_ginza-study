#When faced with error, I had to update pip and install python-devel via yum (CentOS 7)
import spacy
import ginza
nlp = spacy.load("ja_ginza")
doc = nlp("東京オリンピックは２０２１年に開催されています。")
print(ginza.bunsetu_spans(doc))
print ("===============")
for np in doc.noun_chunks:
    print(np)
