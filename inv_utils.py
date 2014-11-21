# -*- coding: utf-8 -*
import re

__author__ = 'b9om'



class Inv:
    PID = 'PID:[\s]*\w*[-]*\w*'
    SN = 'SN:[\s]*\w*'

    def __init__(self,text):
        self.text = text

    def get_inventory(self):
      ALL_PID = []
      ALL_SN = []
      # PID
      rg = re.compile(self.PID,re.IGNORECASE|re.DOTALL)
      m = re.findall(rg,self.text.decode())
      if m:
          ALL_PID = m
      # SN
      rg = re.compile(self.SN,re.IGNORECASE|re.DOTALL)
      m = re.findall(rg,self.text.decode())
      if m:
          ALL_SN = m

      return list(zip(ALL_PID,ALL_SN))