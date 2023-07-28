import numpy as np
from scipy import stats
import matplotlib.pyplot as pl
from scipy.ndimage.filters import gaussian_filter1d

years = [2016,2017,2018,2019,2020,2021,2022,2023]
rounds = [1,2,3,4,5,6]

fig,axs = pl.subplots(2,3,figsize=(12,8),constrained_layout=True,sharex=True,sharey=True)

for i,year in enumerate(years):
    for j in range(5):

        try:
        
            pre_round = j + 1
            post_round = j + 2
            
            pre_data = np.load('{}/round{}.npy'.format(year,pre_round))
            post_data = np.load('{}/round{}.npy'.format(year,post_round))

            # print(year,j+1)
            
            pre_closing = pre_data[:,-1].astype(int)
            post_closing = post_data[:,-1].astype(int)

            jump_closing = post_closing - pre_closing

            hist,bins = np.histogram(jump_closing,bins=100,density=True)
            bpts = 0.5*(bins[1:] + bins[:-1])

            hist = gaussian_filter1d(hist,sigma=6)

            # axs[j//3,j%3].hist(jump_closing,density=False,histtype='step',bins=100)
            axs[j//3,j%3].plot(bpts,hist,label='{}'.format(year))
            # axs[j//3,j%3].set_xlim(1,5000)
            # axs[j//3,j%3].set_ylim(0,500)
            # axs[j//3,j%3].set_xscale('log')
            # axs[j//3,j%3].set_yscale('log')
            axs[j//3,j%3].set_title('Round {} -> Round {}'.format(j+1,j+2))
            axs[j//3,j%3].set_xlabel('Rank jump between rounds')
            axs[j//3,j%3].set_ylabel('Number of seat choices')
            axs[j//3,j%3].legend()
            # print(year,j+1)
        
        except:
            pass

    try:    
        pre_data = np.load('{}/round1.npy'.format(year))
        post_data = np.load('{}/round6.npy'.format(year))

        pre_closing = pre_data[:,-1].astype(int)
        post_closing = post_data[:,-1].astype(int)

        jump_closing = post_closing - pre_closing

        hist,bins = np.histogram(jump_closing,bins=100)
        bpts = 0.5*(bins[1:] + bins[:-1])

        kernel = stats.gaussian_kde(jump_closing)
        points = np.arange(0,np.amax(jump_closing)//10+1)
        values = kernel(points)

        print(points.shape,values.shape)

        # axs[-1,-1].hist(jump_closing,density=False,histtype='step',bins=100,label='{}'.format(year))
        # axs[-1,-1].plot(bpts,hist,label='{}'.format(year))
        axs[-1,-1].plot(points,values,label='{}'.format(year))
        # axs[-1,-1].set_xlim(0,5000)
        # axs[-1,-1].set_ylim(0,500)
        axs[-1,-1].set_title('Round 1 -> Round 6'.format(j+1,j+2))
        axs[-1,-1].set_xlabel('Rank jump between rounds')
        axs[-1,-1].set_ylabel('Number of seat choices')
        axs[-1,-1].legend()
    except Exception as e:
        print(e)

pl.show()      