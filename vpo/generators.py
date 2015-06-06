'''
Created on 5/6/2015

@author: xgid
'''

def usefull_lines(line):
    '''
    Yield only usefull lines (i.e. non-empty and non-commented)
    '''
    line = line.strip()
    if not line:
        return
    
    if line.startswith(u'#'):
        return
    
    yield line

