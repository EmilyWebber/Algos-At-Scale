from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRMaxWordLen(MRJob):

  def mapper(self, _, line):
    for word in WORD_RE.findall(line):
      yield None, len(word)
  
  def combiner_find_words(self, _, lens):
    yield None, max(lens)
  
  def reducer(self, _, lens):
    yield None, max(lens)

if __name__ == '__main__':
  MRMaxWordLen.run()
