#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import f90nml 
import sys
i = int(sys.argv[1])
data = np.loadtxt('./para_files/Paradat-size-mort-all-tree-exp.csv',delimiter=",", skiprows=1, usecols=[1,2,3,4]) 
nfile = f90nml.read("./para_files/parameters_TT_ushape.nml")
nfile['vegn_parameters_nml']["m0_a"]= data[i,0]
nfile['vegn_parameters_nml']["m0_b"]= data[i,1]
nfile['vegn_parameters_nml']["m0_c"]= data[i,2]
station = int(data[i,3])
nfile['initial_state_nml']["runid"]= 'TT_'+str(station)
nfile.write("./para_files/parameters_TT_update.nml",force=True)
# nfile.write("./para_files/parameters_TT_st"+str(station)+".nml")