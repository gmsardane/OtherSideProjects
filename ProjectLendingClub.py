import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit
from scipy.misc import factorial

rcParams['axes.linewidth'] = 2
rcParams.update({'figure.autolayout': True})

def make_boxplot(data_to_plot, xlab, ylab, xticklab, figfile):
    plt.clf()
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot)
    bp = ax.boxplot(data_to_plot, patch_artist=True)

    for box in bp['boxes']:
        box.set( color='#7570b3', linewidth=2)
        box.set( facecolor = '#1b9e77' )

##the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

## Custom x-axis labels 
    ax.set_xticklabels(xticklab, fontsize=18)
    plt.ylabel(ylab, fontsize=18) #
    plt.xlabel(xlab, fontsize=18) #
## Remove top axes and right axes ticks
    plt.yscale('log', nonposy='clip')
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.minorticks_on()
    ax.tick_params(axis='x',which='minor',bottom='off')
# Save the figure
    fig.savefig(figfile, bbox_inches='tight')

def replace(x):
    if x == "A":
        return 1
    elif x == "B":
        return 2
    elif x =="C":
        return 3
    elif x =="D":
        return 4
    elif x =="E":
        return 5
    elif x =="F":
        return 6
    else:
        return 7


df = pd.read_csv("LoanStats3a.csv")
#dr = pd.read_csv("RejectStatsA.csv") 
x = df.groupby(["purpose"]).id.count()

#Histogram of Lending Purposes
purposes = x.index.tolist()
plt.bar(range(len(purposes)),df.groupby(["purpose"]).id.count(), align='center', color='pink')
plt.xticks(range(len(purposes)),purposes,rotation=90)
plt.ylabel('Number of Loans')
plt.yscale('log', nonposy='clip')
plt.gcf().subplots_adjust(bottom=0.35, top=0.7) #adjusting the plotting area
plt.tight_layout() #may raise an exception, depends on which backend is in use
plt.savefig("HistogramLendingPurpose.pdf",dpi=400)

for index, row in df.iterrows():
    df.loc[index, "grade"] = replace(row["grade"])


data_to_plot = [ df[(df['grade']==1) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==2) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==3) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==4) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==5) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==6) & (df["is_inc_v"]!="Not Verified")]['annual_inc'], \
 	             df[(df['grade']==7) & (df["is_inc_v"]!="Not Verified")]['annual_inc']]                

make_boxplot(data_to_plot, 'Lending Club Grade', 'Annual Income [USD]', \
['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'fig1.pdf')  #'A', 'B', 'C', 'D', 'E', 'F', 'G'
good_debtors = df[(df['loan_status']=='Fully Paid')  & (df["is_inc_v"]!="Not Verified") ]
data_to_plot = [ good_debtors[(good_debtors['grade']==1)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==2)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==3)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==4)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==5)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==6)]['annual_inc'], \
 	             good_debtors[(good_debtors['grade']==7)]['annual_inc']]    
plt.clf()
tmp = df[(df["is_inc_v"]!="Not Verified")]
wgt = tmp.groupby(['grade'], as_index=False).id.count() ["id"].tolist()

entries, bin_edges, patches = plt.hist(good_debtors['grade'], bins=np.arange(8)+0.5, \
alpha =0.65, color = 'pink')#, weights=wgt)
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1])

#Linear?
#m, b = np.polyfit(bin_middles, entries,1)
#plt.plot(bin_middles, m*bin_middles+b, '-k', lw =2 )
plt.xticks( np.arange(8)+1.0, ('A', 'B', 'C', 'D', 'E', 'F', 'G'), fontsize=18 )
plt.ylim(0, 0.35)
plt.xlim(0,8)
plt.xlabel('Lending Club Grade', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.clf()
print len(entries) , '= Lengths enntries', len(wgt)

plt.bar(bin_middles, entries/wgt,  color='pink', alpha=0.85, linewidth=1.5)
plt.xticks(bin_middles+0.5,['A', 'B', 'C', 'D', 'E', 'F', 'G'])
plt.xlabel('Lending Club Grade', fontsize=18)
plt.ylabel('Fraction', fontsize=18)
plt.savefig('fig2.pdf', dpi=400)

#print df.columns.values.tolist()
#print dr.columns.values.tolist()
# fit with curve_fit
#parameters, cov_matrix = curve_fit(poisson, bin_middles, entries) 
# plot poisson-deviation with fitted parameter
#x_plot = np.linspace(0, 20, 1000)
#plt.plot(x_plot, poisson(x_plot, *parameters), 'r-', lw=2)
#print good_debtors.groupby(["purpose"]).id.count()
#print df.groupby(["loan_status"]).id.count()
#plt.xticks(range(len(purposes)), LABELS)

'''
LC Grade vs Loan Status. We are asking the question, how accurate is their grading system
with respect to how well the debtor paid his debt
'''
#print tmp.groupby(["grade"]).id.count()
#print good_debtors.groupby(["grade"]).id.count()

# poisson function, parameter lamb is the fit parameter
def poisson(k, lamb):
    return (lamb**k/factorial(k)) * np.exp(-lamb)



