import json
import re
from collections import OrderedDict
import sys

input_file = sys.argv[1]
keyword = OrderedDict()
from collections import defaultdict
questions=[]
dict= defaultdict(list)
pattern = r'(^{0}(?=(\s)+)|^{0}\?$|^{0}(?=,))'
keywords = ["how","how many","how much","what","when","where","which","whom","who"]
for x in keywords:
    keyword[x] = 0
with open(input_file, 'r') as f:
    d = json.load(f)


for i in range(0,len(d['data'])):
  for j in range (0,len(d['data'][i]['paragraphs'])):
      for k in range(0,len(d['data'][i]['paragraphs'][j]['qas'])):
          questions.append(d['data'][i]['paragraphs'][j]['qas'][k]['question'])

for i in range(0, len(questions)):
        for word in keywords:
                if re.match(pattern.format(word),questions[i].lower().strip()):
                    keyword[word]+=1
                    dict[word].append(questions[i])

with open('1a.json', 'w') as fp:
    json.dump(keyword, fp)
