#!/usr/bin/env python3 
import os
import math
import array
import ROOT
import geant4_pybind as g4b
import json

class cflmdSidesG4Particles:

    def __init__(self, my_d, det_lab):

        global s_eventIDs,s_edep_devices,s_p_steps,s_energy_steps
        s_eventIDs,s_edep_devices,s_p_steps,s_energy_steps = {}, {}, {}, {}

        self.geant4_model = "cflm"

        for i in ('I', 'II'):
            s_eventIDs[f'detector_{i}'] = []
            s_edep_devices[f'detector_{i}'] = []
            s_p_steps[f'detector_{i}'] = []
            s_energy_steps[f'detector_{i}'] = []
        
        geant4_json = "./setting/absorber/cflm_dsides.json"
        with open(geant4_json) as f:
            g4_dic = json.load(f)

        runManager = g4b.G4RunManagerFactory.CreateRunManager(g4b.G4RunManagerType.Serial)
        rand_engine= g4b.RanecuEngine()
        g4b.HepRandom.setTheEngine(rand_engine)
        g4b.HepRandom.setTheSeed(3020122)
        UImanager = g4b.G4UImanager.GetUIpointer()

        physicsList = g4b.FTFP_BERT()
        physicsList.SetVerboseLevel(0)
        physicsList.RegisterPhysics(g4b.G4StepLimiterPhysics())
        runManager.SetUserInitialization(physicsList)

        detConstruction = cflmDetectorConstruction(g4_dic)
        runManager.SetUserInitialization(detConstruction)

        actionInitialization = cflmaActionInitialization(detConstruction,
                                                        g4_dic['par_in'],
                                                        g4_dic['par_direct'],
                                                        g4_dic['par_type'],
                                                        g4_dic['par_energy'],
                                                        g4_dic['NumofGun'],
                                                        )
        runManager.SetUserInitialization(actionInitialization)
        
        UImanager = g4b.G4UImanager.GetUIpointer()
        UImanager.ApplyCommand('/run/initialize')
        UImanager.ApplyCommand('/tracking/verbose 0')

        runManager.BeamOn(int(g4_dic['BeamOn']))

        self.HitFlagI = 0
        self.HitFlagII = 0
        if det_lab == 'I':
           self.HitFlagI = 1
           self.p_steps=s_p_steps['detector_I']
           self.init_tz_device = -31
           self.p_steps_current=[[[-single_step[1] + my_d.l_x/2,                                                                                  ### *1000: mm---->um
                                   single_step[2],
                                   self.init_tz_device*1000 - single_step[0]]\
                                for single_step in p_step] for p_step in self.p_steps]

           self.energy_steps=s_energy_steps['detector_I']
           self.edep_devices=s_edep_devices['detector_I']
        
        elif det_lab == 'II':
           self.HitFlagII = 1
           self.p_steps=s_p_steps['detector_II']
           self.init_tz_device = 31
           self.p_steps_current=[[[single_step[1] + my_d.l_x/2,                                                                                  ### *1000: mm---->um
                                   single_step[2] ,
                                   single_step[0] - self.init_tz_device*1000]\
                                for single_step in p_step] for p_step in self.p_steps]

           self.energy_steps=s_energy_steps['detector_II']
           self.edep_devices=s_edep_devices['detector_II']
        
        def __del__(self):
            pass

class cflmDetectorConstruction(g4b.G4VUserDetectorConstruction):

    def __init__(self,g4_dic):
        g4b.G4VUserDetectorConstruction.__init__(self)
        self.solid = {}
        self.logical = {}
        self.physical = {}
        self.checkOverlaps = True
        self.create_world(g4_dic['world'])

        self.maxStep = g4_dic['maxStep']*g4b.um

        self.rotation = g4b.G4RotationMatrix()
        self.rotation.rotateZ(3*math.pi/2)
        
        for object_type in g4_dic['object']:
            if(object_type=="pipe"):
                self.create_pipe(g4_dic['object'][object_type])
            if(object_type=="detector"):
                self.detMaterial(g4_dic['object'][object_type]['detMaterial'])
                self.SiCdetectorI(g4_dic['object'][object_type]['detectorI'])
                self.SiCdetectorII(g4_dic['object'][object_type]['detectorII'])

        self.fStepLimit = g4b.G4UserLimits(self.maxStep)
        self.logical['detectorI'].SetUserLimits(self.fStepLimit)
        self.logical['detectorII'].SetUserLimits(self.fStepLimit)

    def create_world(self,world_type):

        self.nist = g4b.G4NistManager.Instance()
        material = self.nist.FindOrBuildMaterial(world_type)
        self.solid['world'] = g4b.G4Box("world",
                                        800*g4b.mm,
                                        800*g4b.mm,
                                        800*g4b.mm)
        self.logical['world'] = g4b.G4LogicalVolume(self.solid['world'],
                                                    material,
                                                    "world")
        self.physical['world'] = g4b.G4PVPlacement(None,
                                                   g4b.G4ThreeVector(0,0,0),
                                                   self.logical['world'],
                                                   "world", 
                                                   None, 
                                                   False,
                                                   0,
                                                   self.checkOverlaps)

        self.logical['world'].SetVisAttributes(g4b.G4VisAttributes.GetInvisible())


    def create_pipe(self,object):
        
        material_type = self.nist.FindOrBuildMaterial(object['material'],
                                                    False)

        translation = g4b.G4ThreeVector(object['position_x']*g4b.mm, object['position_y']*g4b.mm, object['position_z']*g4b.mm)
        visual = g4b.G4VisAttributes(g4b.G4Color(object['colour'][0],object['colour'][1],object['colour'][2]))
        mother = self.physical['world']

        Rmin = object['Rmin']*g4b.mm
        Rmax = object['Rmax']*g4b.mm
        Pipe_Z = object['Pipe_Z']*g4b.mm
        PipeSphi = object['PipeSphi']*g4b.deg
        PipeDphi = object['PipeDphi']*g4b.deg

        self.solid['pipe'] = g4b.G4Tubs("Pipe",
                                        Rmin, Rmax, Pipe_Z/2,PipeSphi,PipeDphi)

        self.logical['pipe'] = g4b.G4LogicalVolume(self.solid['pipe'],
                                                    material_type,
                                                    'pipe')
        self.physical['pipe'] = g4b.G4PVPlacement(self.rotation,
                                                    translation,
                                                    'pipe',
                                                    self.logical['pipe'],
                                                    mother, 
                                                    False,
                                                    0,
                                                    self.checkOverlaps)
        self.logical['pipe'].SetVisAttributes(visual)                                                                                                                                  
    
    def SiCdetectorI(self, object):
        name = "detectorI"
        translation = g4b.G4ThreeVector(object['position_x']*g4b.mm, object['position_y']*g4b.mm, object['position_z']*g4b.mm)
        visual = g4b.G4VisAttributes(g4b.G4Color(object['colour'][0],object['colour'][1],object['colour'][2]))
        mother = self.physical['world']
        sidex = object['side_x']*g4b.mm
        sidey = object['side_y']*g4b.mm
        sidez = object['side_z']*g4b.mm
        
        self.solid[name] = g4b.G4Box(name, sidex/2., sidey/2., sidez/2.)

        self.logical[name] = g4b.G4LogicalVolume(self.solid[name],
                                                 self.compound,
                                                 name)
        self.physical[name] = g4b.G4PVPlacement(self.rotation,
                                                translation,
                                                name,
                                                self.logical[name],
                                                mother, 
                                                False,
                                                0,
                                                self.checkOverlaps)
        self.logical[name].SetVisAttributes(visual)

    def SiCdetectorII(self, object):
        name = "detectorII"
        translation = g4b.G4ThreeVector(object['position_x']*g4b.mm, object['position_y']*g4b.mm, object['position_z']*g4b.mm)
        visual = g4b.G4VisAttributes(g4b.G4Color(object['colour'][0],object['colour'][1],object['colour'][2]))
        mother = self.physical['world']
        sidex = object['side_x']*g4b.mm
        sidey = object['side_y']*g4b.mm
        sidez = object['side_z']*g4b.mm
        
        self.solid[name] = g4b.G4Box(name, sidex/2., sidey/2., sidez/2.)

        self.logical[name] = g4b.G4LogicalVolume(self.solid[name],
                                                 self.compound,
                                                 name)
        self.physical[name] = g4b.G4PVPlacement(self.rotation,
                                                translation,
                                                name,
                                                self.logical[name],
                                                mother, 
                                                False,
                                                0,
                                                self.checkOverlaps)
        self.logical[name].SetVisAttributes(visual)

    def detMaterial(self, object):
        material_1 = self.nist.FindOrBuildElement(object['material_1'], False)
        material_2 = self.nist.FindOrBuildElement(object['material_2'], False)
        material_density = object['density']*g4b.g/g4b.cm3
        self.compound = g4b.G4Material(object['compound_name'], material_density, 2)
        self.compound.AddElement(material_1, object['natoms_1']*g4b.perCent)
        self.compound.AddElement(material_2, object['natoms_2']*g4b.perCent)

        return self.compound
    
    def Construct(self): 
        self.fStepLimit.SetMaxAllowedStep(self.maxStep)
        return self.physical['world']

class cflmPrimaryGeneratorAction(g4b.G4VUserPrimaryGeneratorAction):

    def __init__(self, par_in, par_direct, par_type, par_energy, numofgun):
        super().__init__()
        self.nofParticles = numofgun
        self.fParticleGun = g4b.G4ParticleGun(1)
        particleDefinition = g4b.G4ParticleTable.GetParticleTable().FindParticle(par_type)
        self.fParticleGun.SetParticleDefinition(particleDefinition)
        self.directions = []
        self.par_in = []
        self.energy = []    

        self.directions = [g4b.G4ThreeVector(direction[0], direction[1], direction[2]) for direction in par_direct]
        self.par_in = [g4b.G4ThreeVector(position[0], position[1], position[2]) for position in par_in]
        self.energy = par_energy

    def GeneratePrimaries(self, anEvent):
        
        for i in range(self.nofParticles):
       
            self.fParticleGun.SetParticlePosition(self.par_in[i])
            self.fParticleGun.SetParticleMomentumDirection(self.directions[i])
            self.fParticleGun.SetParticleEnergy(self.energy[i]*g4b.GeV)            
            self.fParticleGun.GeneratePrimaryVertex(anEvent)

class cflmaSteppingAction(g4b.G4UserSteppingAction):

    def __init__(self, detectorConstruction, eventAction):
        super().__init__()
        self.fDetConstruction = detectorConstruction
        self.fEventAction = eventAction

    def UserSteppingAction(self, step):
        volume_pre = step.GetPreStepPoint().GetTouchable().GetVolume()
        edep = step.GetTotalEnergyDeposit()
        point_in = step.GetPreStepPoint().GetPosition()
        
        if volume_pre == self.fDetConstruction.physical['pipe']:
            self.fEventAction.AddPipe(edep)
        
        if volume_pre == self.fDetConstruction.physical['detectorI']:
            self.fEventAction.RecordDetector(edep, point_in, 1)
        if volume_pre == self.fDetConstruction.physical['detectorII']:
            self.fEventAction.RecordDetector(edep, point_in, 2) 

class cflmaEventAction(g4b.G4UserEventAction):

    def BeginOfEventAction(self, event):
        self.edepdSides = {}
        self.p_stepdSides = {}
        self.edepStepdSides = {}
        for i in ('I','II'):
            self.edepdSides[f'detector_{i}'] = 0
            self.p_stepdSides[f'detector_{i}'] = []
            self.edepStepdSides[f'detector_{i}'] = []
        self.totalSingleEdep = 0
        self.fEnergyPipe = 0       
        self.dividedAreaIndex = []

    def EndOfEventAction(self, event):
        eventID = event.GetEventID()  
        for i in ('I','II'):
            print(f'detector_{i}')
            print(len(self.p_stepdSides[f'detector_{i}']))
            save_geant4_events(eventID, self.edepdSides[f'detector_{i}'], self.p_stepdSides[f'detector_{i}'], self.edepStepdSides[f'detector_{i}'], i)
        printModulo = g4b.G4RunManager.GetRunManager().GetPrintProgress()
        if printModulo > 0 and eventID % printModulo == 0:
            print("---> End of event:", eventID)
            print("Pipe: total energy:", g4b.G4BestUnit(self.fEnergyPipe, "Energy"))
            print("Detector I total energy:", g4b.G4BestUnit(self.edepdSides['detector_I'], "Energy"))
            print("Detector II total energy:", g4b.G4BestUnit(self.edepdSides['detector_II'], "Energy"))
    
    def AddPipe(self, de):
        self.fEnergyPipe += de

    def RecordDetector(self, edep, point_in, i):
        if i==1:
           detector_label = 'detector_I'
        elif i==2:
           detector_label = 'detector_II'
        self.edepdSides[detector_label] += edep 
        self.p_stepdSides[detector_label].append([point_in.getX()*1000,
                                              point_in.getY()*1000,
                                              point_in.getZ()*1000])
        self.edepStepdSides[detector_label].append(edep)

class cflmRunAction(g4b.G4UserRunAction):

    def __init__(self):
        super().__init__()

        g4b.G4RunManager.GetRunManager().SetPrintProgress(1)

        analysisManager = g4b.G4AnalysisManager.Instance()
        print("Using", analysisManager.GetType())

        analysisManager.SetVerboseLevel(1)
        
    def BeginOfRunAction(self, run):
        if self.IsMaster():
            print("Begin of run for the entire run \n")
        else:
            print("Begin of run for the local thread \n")

    def EndOfRunAction(self, run):
        if self.IsMaster():
            print("End of run for the entire run \n")
        else:
            print("End of run for the local thread \n")

class cflmaActionInitialization(g4b.G4VUserActionInitialization):

    def __init__(self, detConstruction, par_in, par_direct, par_type, par_energy, numofgun):
        super().__init__()
        self.fDetConstruction = detConstruction
        self.par_in = par_in
        self.par_direct = par_direct
        self.par_type=par_type
        self.par_energy=par_energy
        self.numofgun = numofgun

    def BuildForMaster(self):
        self.SetUserAction(cflmRunAction())
    def Build(self):
        self.SetUserAction(cflmPrimaryGeneratorAction(self.par_in,
                                                      self.par_direct,
                                                      self.par_type,
                                                      self.par_energy,
                                                      self.numofgun))
        self.SetUserAction(cflmRunAction())
        eventAction = cflmaEventAction()
        self.SetUserAction(eventAction)
        self.SetUserAction(cflmaSteppingAction(self.fDetConstruction, eventAction))

def save_geant4_events(eventID,edep_device,p_step,energy_step, i):
    detector_lab = f'detector_{i}'
    if(len(p_step)>0):
        s_eventIDs[detector_lab].append(eventID)
        s_edep_devices[detector_lab].append(edep_device)
        s_p_steps[detector_lab].append(p_step)
        s_energy_steps[detector_lab].append(energy_step)
    else:
        s_eventIDs[detector_lab].append(eventID)
        s_edep_devices[detector_lab].append(edep_device)
        s_p_steps[detector_lab].append([[0,0,0]])
        s_energy_steps[detector_lab].append([0]) 

def main():
    
    global s_eventIDs,s_edep_devices,s_p_steps,s_energy_steps
    s_eventIDs,s_edep_devices,s_p_steps,s_energy_steps = {}, {}, {}, {}
    
    geant4_json = "./setting/absorber/cflm_dsides.json"
    with open(geant4_json) as f:
        g4_dic = json.load(f)

    runManager = g4b.G4RunManagerFactory.CreateRunManager(g4b.G4RunManagerType.Serial)
    
    physicsList = g4b.FTFP_BERT()
    physicsList.RegisterPhysics(g4b.G4StepLimiterPhysics())
    runManager.SetUserInitialization(physicsList)

    detConstruction = cflmDetectorConstruction(g4_dic)
    runManager.SetUserInitialization(detConstruction)

    actionInitialization = cflmaActionInitialization(detConstruction,
                                                     g4_dic['par_in'],
                                                     g4_dic['par_direct'],
                                                     g4_dic['par_type'],
                                                     g4_dic['par_energy'],
                                                     g4_dic['NumofGun']
                                                    )
    runManager.SetUserInitialization(actionInitialization)

    visManager = g4b.G4VisExecutive()
    visManager.Initialize()
    UImanager = g4b.G4UImanager.GetUIpointer()

    if g4_dic['vis']:

         UImanager.ApplyCommand("/control/execute param_file/g4macro/init_vis.mac")
    
    UImanager.ApplyCommand('/run/initialize')
    UImanager.ApplyCommand('/tracking/verbose 1')
    
    UImanager.ApplyCommand(f"/run/beamOn {g4_dic['BeamOn']}")
    
    if g4_dic['vis']:
      
         UImanager.ApplyCommand('/vis/ogl/set/printMode vectored')
         UImanager.ApplyCommand("/vis/viewer/set/background 0 0 0")
         UImanager.ApplyCommand('/vis/ogl/export')
         
         for i in range(1000):
             UImanager.ApplyCommand("/vis/viewer/refresh")
                    
if __name__ == '__main__':
    main()
