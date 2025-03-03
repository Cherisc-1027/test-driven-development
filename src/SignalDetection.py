import numpy as np
import scipy.stats
# created with the help of chatgpt, group project members
class SignalDetection:
   def __init__(self, hits, misses, falseAlarms, correctRejections):
       self.hits = hits
       self.misses = misses
       self.falseAlarms = falseAlarms
       self.correctRejections = correctRejections

   def hit_rate(self):
        if self.hits + self.misses == 0:
            return 0.5  # Prevents undefined case
        return self.hits / (self.hits + self.misses)
  
   def false_alarm_rate(self):
        if self.falseAlarms + self.correctRejections == 0:
            return 0.5  # Prevents undefined case
        return self.falseAlarms / (self.falseAlarms + self.correctRejections)
  
   def d_prime(self):
       return scipy.stats.norm.ppf(self.hit_rate()) - scipy.stats.norm.ppf(self.false_alarm_rate())
  
   def criterion(self):
       return -0.5 * (scipy.stats.norm.ppf(self.hit_rate()) + scipy.stats.norm.ppf(self.false_alarm_rate()))
