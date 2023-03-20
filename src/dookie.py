#!/usr/bin/env python3

LOGO = '''
   _ _ _         
  /     \      
 |  @ d o o k i e 
  \_ _\ 

'''

class dookie:
    """ The dookie class """
    def __init__(self,logo=LOGO):
        self.logo = logo
    def __iter__(self):
        return self
    def screen(self):
        print(self.logo)
 
if __name__ == '__main__':

    d = dookie()
    d.screen()
