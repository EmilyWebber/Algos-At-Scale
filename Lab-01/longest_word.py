from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRMaxLenWord(MRJob):

  def mapper(self, _, line):
    for word in WORD_RE.findall(line):
      yield word, None
  
  def combiner(self, word, _):
    yield word, None

  def reducer_init(self):
    self.max_len = 0
    self.max_at = None
  
  def reducer(self, word, _):
    if len(word) > self.max_len:
      self.max_len = len(word)
      self.max_at = word
    # no yield!

  def reducer_final(self):
    yield self.max_at, self.max_len

if __name__ == '__main__':
  MRMaxLenWord.run()