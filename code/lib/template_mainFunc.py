# -*- coding: utf-8 -*-
"""
template_mainFuc.py
normal script with direct main function
Copyright (C) 2020 Yuichi Takeuchi
"""

# import libraries
import pandas as pd
import matplotlib.pyplot as plt


# define functions and classes
def myfunc_a(x, y):
    '''
    Docstring for this function
    '''
    return x + y


def myfunc_b(x, y):
    '''
    Docstring for this function
    '''
    return x - y


def main():
    '''
    Docstring for this function
    '''
    # meta info
    #dataFldr = '../data'
    resultFldr = '../results'
    #dataFile = 'blahblah.csv'
    
    # data import
    #df = pd.read_csv(dataFldr + '/' + dataFile)
    
    # figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([0, 1])

    fname = 'figure'
    fig.savefig(resultFldr + '/' + fname+'.png', dpi=300, format='png')
    fig.savefig(resultFldr + '/' + fname+'.pdf', dpi=300, format='pdf')
    #fig.savefig(resultFldr + '/' + fname+'.ps', dpi=300, format='ps')
    #fig.savefig(resultFldr + '/' + fname+'.eps', dpi=300, format='eps')
    #fig.savefig(resultFldr + '/' + fname+'.svg', dpi=300, format='svg')
    
    x, y = 3, 5
    mainFunc_out1 = myfunc_a(x, y)
    mainFunc_out2 = myfunc_b(x, y)
    print(mainFunc_out1, mainFunc_out2)
    return mainFunc_out1, mainFunc_out2


# main procedure when called
if __name__ == '__main__':
    main()
