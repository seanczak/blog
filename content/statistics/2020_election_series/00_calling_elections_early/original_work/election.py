import json
import pandas as pd
import numpy as np
import scipy

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

class Experiment():
    def __init__(self, p_hat, nsample, N=1e6):
        '''
        N is total sample size (if not infinite)
        p is proportion that is "True"
        nsample is the amount to be sampled
        '''
        self.nsample = int(nsample)
        self.p       = p_hat
        # for normal approx
        self.mean    = self.nsample * p_hat
        self.var     = self.nsample * p_hat * (1 - p_hat)
        self.std     = np.sqrt(self.var)
        # for hypergeometric
        self.K       = p_hat*N
        self.N       = N
        # for beta
        self.a       = self.mean
        self.b       = self.nsample - self.mean
        return
    
    def plot_binomial(self,N = int(1e6), bins = None, xlims = None, ylims = None):
        
        fig, axes = plt.subplots(1,2,figsize = (20,5))

        # plot pmf
        ax = axes[0];
        # generate a random sample and plot it
        x = np.random.binomial(self.nsample,self.p,N)
        axes[0].hist(x, bins = 50,color='grey',edgecolor='w')
        # set x lims 
        xlims = [self.mean - 5*self.std , self.mean + 5*self.std] if xlims is None else xlims
        ax.set_xlim(xlims)
        ylims = [0,N//10] if ylims is None else ylims
        ax.set_ylim(ylims)
        # plt pmf
        x = np.arange(0,self.nsample,step = 1)
        cdf = scipy.stats.binom.cdf(x,self.nsample,self.p)
        axes[1].plot(x,cdf, c= 'c')
        axes[1].set_title('cdf')
        return axes
        
    def plot_hypergeometric(self, N = int(1e6), bins = None, xlims = None, ylims = None):
        
        fig, axes = plt.subplots(1,2,figsize = (20,5))

        # plot pmf
        ax = axes[0];
        # generate a random sample and plot it
        ngood = self.K
        nbad  = self.N - ngood
        x = np.random.hypergeometric(ngood, nbad, self.nsample, size=N)
        axes[0].hist(x, bins = 50, color='grey', edgecolor='w')
        # set x lims 
        xlims = [self.mean - 5*self.std , self.mean + 5*self.std] if xlims is None else xlims
        ax.set_xlim(xlims)
        ylims = [0,N//10] if ylims is None else ylims
        ax.set_ylim(ylims)
        # plt pmf
        x = np.arange(0,self.nsample,step = 1)
        cdf = scipy.stats.hypergeom.cdf(x,self.N, ngood, self.nsample)
        axes[1].plot(x,cdf, c= 'c')
        axes[1].set_title('cdf')
        return axes
        
    def plot_normal_approx_bin(self,N = int(1e6), bins = None, xlims = None, ylims = None):
        
        fig, axes = plt.subplots(1,2,figsize = (20,5))

        # plot pmf
        ax = axes[0];
        # generate a random sample and plot it
        x = np.random.normal(self.mean, self.std, size=N)
        axes[0].hist(x, bins = 50, color='grey', edgecolor='w')
        # set x lims 
        xlims = [self.mean - 5*self.std , self.mean + 5*self.std] if xlims is None else xlims
        ax.set_xlim(xlims)
        ylims = [0,N//10] if ylims is None else ylims
        ax.set_ylim(ylims)
        # plt pmf
        x = np.arange(0,nsample,step = 1)
        cdf = scipy.stats.norm.cdf(x,self.mean, self.std)
        axes[1].plot(x,cdf, c= 'c')
        axes[1].set_title('cdf')
        return axes
        
    def plot_beta(self,N = int(1e6), bins = None, xlims = None, ylims = None):
        
        fig, axes = plt.subplots(1,2,figsize = (20,5))
        # plot pmf
        ax = axes[0];
        # generate a random sample and plot it
        x = np.random.beta(self.a, self.b, size=N)
        x = np.linspace(0,1,N)
        y = np.zeros(N)
        pdf = scipy.stats.beta.pdf(x,self.a, self.b)
        axes[0].plot(x,pdf, color='grey')
        axes[0].fill_between(x,pdf,y, color='grey')
        # set x lims 
        xlims = [(self.mean - 5*self.std)/self.nsample , (self.mean + 5*self.std)/self.nsample] if xlims is None else xlims
        ax.set_xlim(xlims)
        # ylims = [0,N//10] if ylims is None else ylims
        # ax.set_ylim(ylims)
        # plt pmf
        x = np.linspace(0,1,N)
        cdf = scipy.stats.beta.cdf(x,self.a, self.b)
        axes[1].plot(x,cdf, c= 'c')
        axes[1].set_title('cdf')
        return axes
    
    def plot_normal_approx_beta(self,N = int(1e6), bins = None, xlims = None, ylims = None):
        
        fig, axes = plt.subplots(1,2,figsize = (20,5))

        # plot pmf
        ax = axes[0];
        # generate a random sample and plot it
        x = np.random.normal(self.p, self.std/self.nsample, size=N)
        axes[0].hist(x, bins = 50, color='grey', edgecolor='w')
        # set x lims 
        xlims = [(self.mean - 5*self.std)/self.nsample , (self.mean + 5*self.std)/self.nsample] if xlims is None else xlims
        ax.set_xlim(xlims)
        ylims = [0,N//10] if ylims is None else ylims
        ax.set_ylim(ylims)
        # plt pmf
        x = np.linspace(0,1,N)
        cdf = scipy.stats.norm.cdf(x,self.p, self.std/self.nsample)
        axes[1].plot(x,cdf, c= 'c')
        axes[1].set_title('cdf')
        return axes

def calc_CI(p1, N, eps = 1e-15):
    # z score given an alpha of 0.0001 (two tailed)
#     z = 1.96
#     z = 2.576 #99%
    z = 3.891 # 99.99
    # normal approximation using CLT
    interval = z * np.sqrt(p1 * (1 - p1) / N)
    # upper lower bounds are just +/- above
    upper = p1 + interval
    lower = p1 - interval
    # bound them to (0,1) - this made vectorization break, it worked anyways
#     upper = 1 - eps if upper > 1 else upper
#     lower = 0 + eps if lower < 0 else lower
    return upper, lower

