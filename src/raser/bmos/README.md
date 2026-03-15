cfg file path：/raser/setting/g4experiment/bmos.json

The electric field information of the detector needs to be obtained before operation
run steps:
```
raser field NJU-PiN-bmos
raser field -wf NJU-PiN-bmos
```

For single-event simulation
run steps:
```
raser bmos GetSignal
raser bmos DrawHistogram
raser bmos DrawSignal
```
GetSignal:Simulation
DrawHistogram:Draw histogram of the output signal amplitude
DrawSignal:Draw raw current signal from the last output of the detector and the voltage signal output through the USCS.

For beam test
run steps:
```
raser bmos BeamCreate
source src/raser/bmos/beam_run.sh
```
BeamCreate:Generate the particle position information for each beam pulse randomly based on the parameters in bmos.json
beam_run.sh:Perform single-event simulations in batch for each beam pulse, and verify that the internal parameters are consistent with the corresponding parameters in the bmos.json file before running