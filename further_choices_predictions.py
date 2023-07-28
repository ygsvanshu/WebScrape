import numpy as np
import matplotlib.pyplot as pl

years = [2016,2017,2018,2019,2020,2021,2022,2023]
rounds = [1,2,3,4,5,6]
colors = ['m','r','darkorange','goldenrod','g','deepskyblue','blue','k']

fig,axs = pl.subplots(3,5,constrained_layout=True,figsize=(15,9),sharex=True,sharey=True)

choices = np.genfromtxt('FurtherChoices.csv',dtype=str,delimiter=';')
choices = np.flip(choices,axis=0)

for c,choice in enumerate(choices):
    for i,year in enumerate(years):
        aaaa = []
        bbbb = []
        for j in range(6):
            try:
                
                data = np.load('{}/round{}.npy'.format(year,j+1))
                data = data[data[:,0]==choice[0]]
                data = data[data[:,1]==choice[1]]
                    
                aaaa += [j+1]
                bbbb += [int(data[:,-1])]
            except Exception as e:
                print(e)
                
        try:
            # print(aaaa,bbbb)
            axs[c//5,c%5].plot(aaaa,bbbb,'.-',color=colors[i],label='{}'.format(year))
        except Exception as e:
        #     print(e)
            pass

    axs[c//5,c%5].legend(ncol=2)
    axs[c//5,c%5].set_title('{}'.format(choice[2]))
    axs[c//5,c%5].set_xlabel('Round number')
    axs[c//5,c%5].set_ylabel('Closing rank')
    axs[c//5,c%5].axhline(26574,color='gray',linestyle='--')

    print(choice[0],'>---<',choice[1])

for i,year in enumerate(years):
    aaaa = []
    bbbb = []
    for j in range(6):
        try:
            
            data = np.load('{}/round{}.npy'.format(year,j+1))
            data = data[data[:,0]=='Maulana Azad National Institute of Technology Bhopal']
            data = data[data[:,1]=='Mathematics and Data Science (5 Years, Bachelor and Master of Technology (Dual Degree))']

            # print(year,j+1,int(data[:,-1]))
                  
            aaaa += [j+1]
            bbbb += [int(data[:,-1])]
        except:
            pass
            
    try:
        print(aaaa,bbbb)
        axs[-1,-1].plot(aaaa,bbbb,'.-',color=colors[i],label='{}'.format(year))
    except:
        pass
axs[-1,-1].legend()
pl.savefig('DashboardFurtherRounds.png')
pl.show()