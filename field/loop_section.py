#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import pickle

import devsim
import numpy as np

from . import initial
from . import restart
from . import physics_drift_diffusion
from .create_parameter import delete_init
from util.output import output
from util.memory_decorator import memory_decorator

class loop_section():
    def __init__(self, paras,device,region,solve_model,irradiation):
        self.paras = paras
        self.step_model  = False
        self.solve_model = solve_model
        self.device = device
        self.region = region
        self.irradiation = irradiation
        self.voltage = []
        self.current = []
        self.capacitance = []
        self.noise = []
        self.voltage_milestone = []
        self.positions_mid = []
        self.intensities = []

        self.positions = []
        self.electrons = []
        self.holes = []

    def initial_solver(self,contact,set_contact_type,irradiation_model,irradiation_flux,impact_model):
        initial.PotentialOnlyInitialSolution(device=self.device, region=self.region, circuit_contacts=contact, paras=self.paras, set_contact_type=set_contact_type)
        devsim.solve(type="dc", absolute_error=self.paras['absolute_error_Initial'], relative_error=self.paras['relative_error_Initial'], maximum_iterations=self.paras['maximum_iterations_Initial'])
        print("======================\nFirst initialize successfully\n===============================")
        if self.solve_model == "wf":
            pass
        else:
            print("======RASER info ===========\nradiation\n================info=================")
            initial.DriftDiffusionInitialSolution(device=self.device, region=self.region, circuit_contacts=contact,paras=self.paras,set_contact_type=set_contact_type,
                                                irradiation_model=irradiation_model,irradiation_flux=irradiation_flux,impact_model=impact_model)
            devsim.solve(type="dc", absolute_error=self.paras['absolute_error_Initial'], relative_error=self.paras['relative_error_Initial'], maximum_iterations=self.paras['maximum_iterations_Initial'])
            
        # eliminate calculation fatals from intrinsic carrier concentration
        delete_init(device=self.device, region=self.region)

        print("=====================\nDriftDiffusion initialize successfully\n======================")
        print("=========RASER info =========\nAll initialization successfully\n=========info========== ")    
    
    def save_values(self, v_current):
        path = output(__file__, self.device, "temp_data")
        Holes_values = devsim.get_node_model_values(device=self.device, region=self.region, name="Holes")
        Electrons_values = devsim.get_node_model_values(device=self.device, region=self.region, name="Electrons")
        Potential_values = devsim.get_node_model_values(device=self.device, region=self.region, name="Potential")
        with open(os.path.join(path,'Holes_{}.pkl'.format(v_current),), 'wb') as file:
            file.truncate(0)
        with open(os.path.join(path,'Holes_{}.pkl'.format(v_current),), 'wb') as file:
            pickle.dump(Holes_values, file)
        with open(os.path.join(path,'Electrons_{}.pkl'.format(v_current),), 'wb') as file:
            file.truncate(0)
        with open(os.path.join(path,'Electrons_{}.pkl'.format(v_current),), 'wb') as file:
            pickle.dump(Electrons_values, file)
        with open(os.path.join(path,'Potential_{}.pkl'.format(v_current),), 'wb') as file:
            file.truncate(0)
        with open(os.path.join(path,'Potential_{}.pkl'.format(v_current),), 'wb') as file:
            pickle.dump(Potential_values, file)
    
    def load_values(self, values, v_current):
        path = output(__file__, self.device, "temp_data")
        if values=="Holes":
            with open(os.path.join(path,'Holes_{}.pkl'.format(v_current),), 'rb') as file:
                return pickle.load(file)
        elif values=="Electrons":
            with open(os.path.join(path,'Electrons_{}.pkl'.format(v_current),), 'rb') as file:
                return pickle.load(file)
        elif values=="Potential":
            with open(os.path.join(path,'Potential_{}.pkl'.format(v_current),), 'rb') as file:
                return pickle.load(file)
        
    def set_values(self, v_current):
        for i in ("Holes","Electrons","Potential"):
            value = self.load_values(i, v_current)
            devsim.set_node_values(device=self.device, region=self.region, name=i, values=value)

    @memory_decorator
    def loop_solver(self,circuit_contact,v_current,area_factor):
        if self.solve_model =="step":
            if v_current == 0:
                pass
            else:
                print("=================RASER info==================\n Load last voltage successfully\n===============info===================")
                self.set_values(v_current)

        self.voltage.append(v_current)
        devsim.set_parameter(device=self.device, name=physics_drift_diffusion.GetContactBiasName(circuit_contact), value=v_current)
        devsim.solve(type="dc", absolute_error=self.paras['absolute_error_VoltageSteps'], relative_error=self.paras['relative_error_VoltageSteps'], maximum_iterations=self.paras['maximum_iterations_VoltageSteps'])
        if self.solve_model !="wf":     
            physics_drift_diffusion.PrintCurrents(device=self.device, contact=circuit_contact)
            electron_current= devsim.get_contact_current(device=self.device, contact=circuit_contact, equation="ElectronContinuityEquation")
            hole_current    = devsim.get_contact_current(device=self.device, contact=circuit_contact, equation="HoleContinuityEquation")
            total_current   = electron_current + hole_current
            if(abs(total_current/area_factor)>105e-6): 
                print("==========RASER info===========\nCurrent is too large !\n==============Warning==========")
                # break
            self.current.append(total_current)
            if self.solve_model == "cv":
                devsim.circuit_alter(name="V1", value=v_current)
                devsim.solve(type="ac", frequency=self.paras["frequency"])
                cap=1e12*devsim.get_circuit_node_value(node="V1.I", solution="ssac_imag")/ (-2*np.pi*self.paras["frequency"])
                self.capacitance.append(cap*area_factor)
            if self.solve_model == "noise":
                devsim.solve(type="noise", frequency=self.paras["frequency"],output_node="V1.I")
                noise=devsim.get_circuit_node_value(node="V1.I")
                self.noise.append(noise)
            self.save_values(v_current)  

    def get_voltage_values(self):
        return self.voltage
    def get_current_values(self):
        return self.current
    def get_cap_values(self):
        return self.capacitance
    def get_noise_values(self):
        return self.noise

