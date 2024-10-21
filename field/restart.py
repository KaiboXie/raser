import devsim

from .physics_drift_diffusion import *
from .initial import switch_cylindrical_coordinate

def PotentialOnlyRestartSolution(device, region, paras, circuit_contacts, set_contact_type=None):
    if paras["Cylindrical_coordinate"]==True:
        switch_cylindrical_coordinate(device,region)
    else:
        pass
    CreateSiliconPotentialOnly(device=device, region=region)
    
    for i in devsim.get_contact_list(device=device):
        if set_contact_type and i in set_contact_type:
            contact_type = set_contact_type[i]
        else:
            contact_type = {"type" : "Ohmic"}
        devsim.set_parameter(device=device, name=GetContactBiasName(i), value=0)
        if str(circuit_contacts) in i :
            CreateSiliconPotentialOnlyContact(device, region, i, contact_type,True)
        else:
            devsim.set_parameter(device=device, name=GetContactBiasName(i), value="0.0")
            CreateSiliconPotentialOnlyContact(device, region, i, contact_type)

def DriftDiffusionRestartSolution(device, region, paras, irradiation_model=None, irradiation_flux=1e15, impact_model=None, circuit_contacts=None, set_contact_type=None):
    if paras["Cylindrical_coordinate"]==True:
        switch_cylindrical_coordinate(device,region)
    else:
        pass
    CreateSolution(device, region, "Electrons")
    CreateSolution(device, region, "Holes")
    CreateSiliconDriftDiffusion(device=device, region=region, impact_model=impact_model, irradiation_model=irradiation_model, irradiation_flux=irradiation_flux)
            
    for i in devsim.get_contact_list(device=device):
        if set_contact_type and i in set_contact_type:
            contact_type = set_contact_type[i]
        else:
            contact_type = {"type" : "Ohmic"}

        if str(circuit_contacts) in i:
            devsim.set_parameter(device=device, name=GetContactBiasName(i), value="0.0")
            CreateSiliconDriftDiffusionAtContact(device, region, i, contact_type, True)
        else:
            devsim.set_parameter(device=device, name=GetContactBiasName(i), value="0.0")
            CreateSiliconDriftDiffusionAtContact(device, region, i, contact_type)

