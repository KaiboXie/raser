#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import sys
import os
import subprocess
import time
import math

import devsim 
import numpy as np

from gen_signal.build_device import Detector
from .create_mesh import DevsimMesh
from . import model_create
from . import save_milestone
from . import loop_section
from . import physics_drift_diffusion
from util.output import output
from .devsim_draw import *
import multiprocessing


v_current = 0
V = []
c = []
Current = []
noise = []

paras = {
    "absolute_error_Initial" : 1e10, 
    "relative_error_Initial" : 1e-10, 
    "maximum_iterations_Initial" : 1000,

    "absolute_error_DriftDiffusion" : 1e10, 
    "relative_error_DriftDiffusion" : 1e-10, 
    "maximum_iterations_DriftDiffusion" : 1000,

    "absolute_error_VoltageSteps" : 1e10, 
    "relative_error_VoltageSteps" : 1e-10, 
    "maximum_iterations_VoltageSteps" : 1000,

    "milestone_mode" : True,
    "milestone_step" : 50,

    "voltage_step" : 0.1,
    "acreal" : 1.0, 
    "acimag" : 0.0,
    "frequency" : 1000.0,
    
    "Cylindrical_coordinate": False,


    "ac-weightfield" : False,


    "Voltage-step-model" : False,
    "step":1,

}
os.environ["OMP_NUM_THREADS"] = "1"
def main (kwargs):
    simname = kwargs['label']
    is_cv = kwargs['cv']
    is_wf = kwargs["wf"]
    is_step = kwargs["step"]
    is_noise = kwargs["noise"]
    
    if is_wf:
        paras.update({"weightfield": True})
    else:
        paras.update({"weightfield": False})
    
    if is_step:
        paras.update({"Voltage-step-model": True})
    else:
        paras.update({"Voltage-step-model": False})

    

    device = simname
    region = simname
    MyDetector = Detector(device)
    MyDevsimMesh = DevsimMesh(MyDetector, devsim_solve_paras=paras)
    MyDevsimMesh.mesh_define()

    if "frequency" in MyDetector.device_dict:
        paras.update({"frequency": MyDetector.device_dict['frequency']})
    if "area_factor" in MyDetector.device_dict:
        paras.update({"area_factor": MyDetector.device_dict['area_factor']})
    if "default_dimension" in MyDetector.device_dict:
        default_dimension =MyDetector.device_dict["default_dimension"]
    if "irradiation" in MyDetector.device_dict and not is_wf:
        irradiation = True
    else:
        irradiation = False

    devsim.open_db(filename="./output/field/SICARDB.db", permission="readonly")
    
    T = MyDetector.device_dict['temperature']
    k = 1.3806503e-23  # J/K
    q = 1.60217646e-19 # coul
    devsim.add_db_entry(material="global",   parameter="T",    value=T,     unit="K",   description="T")
    devsim.add_db_entry(material="global",   parameter="k_T",    value=k*T,       unit="J",        description="k*T")
    devsim.add_db_entry(material="global",   parameter="Volt_thermal",    value=k*T/q,     unit="J/coul",   description="k*T/q")
    N_c=2.82e19*pow(T/300,1.5)
    N_v=1.83e19*pow(T/300,1.5)
    devsim.add_db_entry(material="Silicon",parameter="N_c",value=N_c, unit="/cm^3", description="effective density of states in conduction band")
    devsim.add_db_entry(material="Silicon",parameter="N_v",value=N_v, unit="/cm^3", description="effective density of states in valence band")
    E_g=1.12*1.6e-19
    N_i=pow(N_c*N_v,0.5)*math.exp(-E_g/(2*k*T))
    devsim.add_db_entry(material="Silicon",   parameter="n_i",    value=N_i,   unit="/cm^3",     description="Intrinsic Electron Concentration")
    devsim.add_db_entry(material="SiliconCarbide",   parameter="n_i",    value=N_i,   unit="/cm^3",     description="Intrinsic Electron Concentration")
    devsim.add_db_entry(material="gas",   parameter="n_i",    value="1e-9",   unit="/cm^3",     description="Intrinsic Electron Concentration")
    devsim.add_db_entry(material="gas",   parameter="Permittivity",    value="1",   unit="1",     description="Permittivity")
    devsim.add_db_entry(material="Silicon",   parameter="n1",     value=N_i,   unit="/cm^3",     description="n1")
    devsim.add_db_entry(material="Silicon",   parameter="p1",     value=N_i,   unit="/cm^3",     description="p1")

    if "parameter_alter" in MyDetector.device_dict:
        for material in MyDetector.device_dict["parameter_alter"]:
            print (material)
            for parameter in MyDetector.device_dict["parameter_alter"][material]:
                print (parameter)
                devsim.add_db_entry(material=material,
                                    parameter=parameter['name'],
                                    value=parameter['value'],
                                    unit=parameter['unit'],
                                    description=parameter['name'])
    if "parameter" in MyDetector.device_dict:
        devsim.add_db_entry(material=MyDetector.device_dict['parameter']['material'],parameter=MyDetector.device_dict['parameter']['name'],value=MyDetector.device_dict['parameter']['value'],unit=MyDetector.device_dict['parameter']['unit'],description=MyDetector.device_dict['parameter']['description'])
    if "U_const" in MyDetector.device_dict:
        U_const=MyDetector.device_dict["U_const"]
        model_create.CreateNodeModel(device,region,"U_const",U_const)
    else:
        model_create.CreateNodeModel(device,region,"U_const",0)
    if "irradiation" in MyDetector.device_dict:
        irradiation_model=MyDetector.device_dict['irradiation']['irradiation_model']
        irradiation_flux=MyDetector.device_dict['irradiation']['irradiation_flux']
    else:
        irradiation_model=None
        irradiation_flux=None
    if 'avalanche_model' in MyDetector.device_dict:
        impact_model=MyDetector.device_dict['avalanche_model']
    else:
        impact_model=None

        
    circuit_contacts=[]
    if is_wf == True:
        if MyDetector.device_dict.get("mesh", {}).get("2D_mesh", {}).get("ac_contact"):
            print("=========RASER info===================\nACLGAD is simulating\n=============info====================")
            for read_out_electrode in MyDetector.device_dict["mesh"]["2D_mesh"]["ac_contact"]:
                circuit_contacts.append(read_out_electrode["name"])
            for i,c in enumerate(circuit_contacts):
                devsim.circuit_element(name="V{}".format(i+1), n1=physics_drift_diffusion.GetContactBiasName(c), n2=0,
                        value=0.0, acreal=paras['acreal'], acimag=paras['acimag'])
        else:
            print("===============RASER info===================\nNot AC detector\n===========info=============")
            for read_out_electrode in MyDetector.device_dict["read_out_contact"]:
                circuit_contacts.append(read_out_electrode)
            for i,c in enumerate(circuit_contacts):
                devsim.circuit_element(name="V{}".format(i+1), n1=physics_drift_diffusion.GetContactBiasName(c), n2=0,
                        value=0.0, acreal=paras['acreal'], acimag=paras['acimag'])
            
    else:
        circuit_contacts=MyDetector.device_dict['bias']['electrode']
        devsim.circuit_element(name="V1", n1=physics_drift_diffusion.GetContactBiasName(circuit_contacts), n2=0,
                           value=0.0, acreal=paras['acreal'], acimag=paras['acimag'])
    T1 = time.time()
    print("================RASER info============\nWelcome to RASER TCAD PART, mesh load successfully\n=============info===============")
    devsim.set_parameter(name="debug_level", value="info")
    devsim.set_parameter(name = "extended_solver", value=True)
    devsim.set_parameter(name = "extended_model", value=True)
    devsim.set_parameter(name = "extended_equation", value=True)
    
    if is_cv ==True:
        solve_model = "cv"
    elif is_noise == True:
        solve_model = "noise"
    elif is_wf ==True:
        solve_model = "wf"
    elif is_step ==True:
        solve_model = "step"
    else :
        solve_model = None

    path = output(__file__, device)
    if irradiation:
        path = output(__file__, device, str(irradiation_flux))

    loop=loop_section.loop_section(paras=paras,device=device,region=region,solve_model=solve_model,irradiation=irradiation)
    def worker_function(queue, lock, circuit_contacts, v_current, area_factor, path, device, region, solve_model, irradiation, is_wf):
        try:
            print(f"运行 loop_solver,参数:{circuit_contacts}, {v_current}, {area_factor}")
            loop.loop_solver(circuit_contact=circuit_contacts, v_current=v_current, area_factor=area_factor)
            result_message = "Execution completed successfully"

        except Exception as e:
            result_message = f"Error: {e}"
        with lock:
            queue.put(result_message)  
    
    if is_wf == True:
        v_current=1
        print("=======RASER info========\nBegin simulation WeightingField\n======================")
        for contact in circuit_contacts:
            print(path)
            folder_path = os.path.join(path, "weightingfield")
            print(folder_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            paras["milestone_step"] == 1
            paras.update({"milestone_step":paras["milestone_step"]})

            loop.initial_solver(contact=contact,set_contact_type=None,irradiation_model=irradiation_model,irradiation_flux=irradiation_flux,impact_model=impact_model)
            loop.loop_solver(circuit_contact=contact,v_current=v_current,area_factor=paras["area_factor"])

            save_milestone.save_milestone(device=device, region=region, v=v_current, path=folder_path,dimension=default_dimension,contact=contact,is_wf=is_wf)
            devsim.write_devices(file=os.path.join(folder_path,"weightingfield.dat"), type="tecplot")
            
    elif is_wf == False:
        v_current = 0
        loop.initial_solver(contact=circuit_contacts,set_contact_type=None,irradiation_model=irradiation_model,irradiation_flux=irradiation_flux,impact_model=impact_model)
        v_current = 0
        v_goal =MyDetector.device_dict['bias']['voltage']
        if v_goal > 0:
            voltage_step = paras['voltage_step']
        else: 
            voltage_step = -1 * paras['voltage_step']
        if is_step == False:
            i = 0
            while abs(v_current) <= abs(v_goal):
                loop.loop_solver(circuit_contact=circuit_contacts,v_current=v_current,area_factor=paras["area_factor"])
                if(paras['milestone_mode']==True and abs(v_current%paras['milestone_step'])<0.01) or abs(v_current) == abs(v_goal) :
                    save_milestone.save_milestone(device=device, region=region, v=v_current, path=path,dimension=default_dimension,contact=circuit_contacts,is_wf=is_wf)
                    devsim.write_devices(file=os.path.join(path,"Ele_Characterization/{}".format(v_current)), type="tecplot")
                i += 1
                v_current = voltage_step*i

        if is_step:
            lock = multiprocessing.Lock()
            queue = multiprocessing.Queue() 

            while abs(v_current) <= abs(v_goal):
                print("voltage_step:", voltage_step)
                print("v_current:", v_current)
                print("============================check======================")
                print(queue)
                print("============================queue======================")
                time.sleep(5)
                p = multiprocessing.Process(target=worker_function, args=(queue, lock, circuit_contacts, v_current, paras['area_factor'], path, device, region, solve_model, irradiation, is_wf))
                p.start()
                p.join()
                while not queue.empty():
                    output_info = queue.get() 
                    print("队列输出:", output_info)  # 确认输出内容
                    if output_info is None:
                        print("警告: worker_function 返回了 None,可能发生了错误!")
                        # exit(1)
                if (paras['milestone_mode'] and v_current % paras['milestone_step'] == 0.0) or abs(v_current) == abs(v_goal):
                    save_milestone.save_milestone(device=device, region=region, v=v_current, path=path, dimension=default_dimension, contact=circuit_contacts, is_wf=is_wf)
                    devsim.write_devices(file=os.path.join(path, "Ele_Characterization_{}.dd".format(v_current)), type="tecplot")
                
                v_current += voltage_step

    if is_wf != True:
        if is_step ==False:
            draw_iv(device, V=loop.get_voltage_values(), I=loop.get_current_values(),path=path)
            if is_cv == True:
                draw_cv(device, V=loop.get_voltage_values(), C=loop.get_cap_values(),path=path)
            if is_noise == True:
                draw_noise(device, V=loop.get_voltage_values(), noise=loop.get_noise_values(),path=path)
        elif is_step == True:
            draw_iv(device, V=V, I=Current,path=path)
            if is_cv == True:
                draw_cv(device, V=V, C=c,path=path)
            if is_noise == True:
                draw_noise(device, V=V, noise=noise,path=path)
    T2 =time.time()
    print("=========RASER info===========\nSimulation finish ,total used time: {}s !^w^!\n================".format(T2-T1))