from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w]+")

class MRAvgUniqWordLen(MRJob):

  def mapper_find_words(self, _, line):
    for word in WORD_RE.findall(line):
      yield word, None
  
  def combiner_find_words(self, word, _):
    yield word, None
  
  def reducer_find_words(self, word, _):
    #print ("this is the reducer that's finding words")
    yield None, len(word)

  def reducer_average_len(self, _, lens):
    print ("I'm hoping this only gets executed once")
    lens_list = list(lens)
    yield None, sum(lens_list)/len(lens_list)

  def steps(self):
    return [
      MRStep(mapper=self.mapper_find_words,
             combiner=self.combiner_find_words,
             reducer=self.reducer_find_words),
      MRStep(reducer=self.reducer_average_len)
    ]

if __name__ == '__main__':
  MRAvgUniqWordLen.run()