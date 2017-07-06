"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

GMapping_means=[0.196999999999999,
                    0.523999999999998,
                    0.334999999999997,
                    0.464999999999998,
                    0.567000000000004,
                    0.569999999999997,
                    0.441000000000000,
                    0.361000000000004,
                    0.803000000000000,
                    0.974000000000002,
                    1.14400000000000,
                    0.156999999999999,
                    0.466000000000000,
                    0.258000000000001,
                    0.603999999999998,
                    0.0829999999999991,
                    0.322999999999998,
                    0.396000000000001,
                    0.0889999999999993,
                    0.115000000000001,
                    0.0679999999999993]
 


GMapping_lims=[0.110466476362741,
                   0.341616811061752,
                   0.276908533635207,
                   0.200193636262496,
                   0.227786238390296,
                   0.159351736733555,
                   0.395953958939673,
                   0.303268438186363,
                   0.338952519388782,
                   0.271504220225028,
                   0.256946954836985,
                   0.154784167148968,
                   0.252497908110146,
                   0.274025244092584,
                   0.334054961944886,
                   0.0520969327312070,
                   0.165605502324047,
                   0.280995241240840,
                   0.0482494518103575,
                   0.0584724208494939,
                   0.0358203070896916]
 
GMapping_wpm_means=[0.0330000000000005,
                    0.180000000000001,
                    0.119000000000003,
                    0.0719999999999942,
                    0.0250000000000000,
                    0.0359999999999999,
                    0.139999999999999,
                    0.108000000000001,
                    0.0699999999999989,
                    0.0410000000000011,
                    0.0530000000000001,
                    0.213000000000000,
                    0.145999999999999,
                    0.0799999999999983,
                    0.139000000000001,
                    0.110000000000000,
                    0.0720000000000027,
                    0.141999999999996,
                    0.0730000000000004,
                    0.103999999999999,
                    0.0499999999999972]
                 
GMapping_wpm_lims=[0.0245195921662652,
                   0.0587999999999981,
                   0.114890110975666,
                   0.0864179981253893,
                   0.00819926826003314,
                   0.0394929056920351,
                   0.0650058458909663,
                   0.116186842628586,
                   0.0809909377646663,
                   0.0469378056581248,
                   0.0527382062645283,
                   0.160630340845058,
                   0.0811922754946583,
                   0.0391999999999992,
                   0.0341456527247592,
                   0.0400483208137376,
                   0.0863067923167126,
                   0.104387252095263,
                   0.0674422300936148,
                   0.0877852470521098,
                   0.0309903210696484]                 




N = 11


ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, GMapping_means[0:11], width, color='r', yerr=GMapping_lims[0:11])
rects2 = ax.bar(ind+width, GMapping_wpm_means[0:11], width, color='y', yerr=GMapping_wpm_lims[0:11])


# add some text for labels, title and axes ticks
ax.set_ylabel('Error [m]')
ax.set_title('')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '2-3', '2-4', '2-5','2-6', '2-7'))

ax.legend((rects1[0], rects2[0]), ('GMapping', 'GMapping with prior map'))

plt.ylim((-0.1,1.85))
plt.xlim((-0.5,11))
ax.yaxis.grid(which="major")

plt.show()


N = 10


ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, GMapping_means[11:], width, color='r', yerr=GMapping_lims[11:])
rects2 = ax.bar(ind+width, GMapping_wpm_means[11:], width, color='y', yerr=GMapping_wpm_lims[11:])


# add some text for labels, title and axes ticks
ax.set_ylabel('Error [m]')
ax.set_title('')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('3-4', '3-5', '3-6', '3-7', '4-5', '4-6', '4-7','5-6', '5-7', '6-7'))

ax.legend((rects1[0], rects2[0]), ('GMapping', 'GMapping with prior map'))

plt.ylim((-0.1,1.2))
plt.xlim((-1,10))
ax.yaxis.grid(which="major")

plt.show()

