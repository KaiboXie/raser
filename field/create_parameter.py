import math

import devsim

from . import model_create

def create_parameter(MyDetector, device, region):
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
    

def delete_init(device, region):
    devsim.delete_node_model(device=device, region=region, name="IntrinsicElectrons")
    devsim.delete_node_model(device=device, region=region, name="IntrinsicHoles")
    devsim.delete_node_model(device=device, region=region, name="IntrinsicElectrons:Potential")
    devsim.delete_node_model(device=device, region=region, name="IntrinsicHoles:Potential")
    devsim.delete_node_model(device=device, region=region, name="IntrinsicCharge")
    devsim.delete_node_model(device=device, region=region, name="IntrinsicCharge:Potential")
    devsim.delete_node_model(device=device, region=region, name="PotentialIntrinsicCharge")
    devsim.delete_node_model(device=device, region=region, name="PotentialIntrinsicCharge:Potential")