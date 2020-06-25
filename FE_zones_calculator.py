##  FLATIRONS ENDURANCE TRAIANING ZONES CALCULATOR ##

## HEART RATE TRAINING ZONES CALCULATOR ##
LThr = 170

Z1hr = (LThr-40)
Z2hr = (LThr-20)
Z3hr = (LThr-8)
Z4hr = (LThr)
Z5hr = (LThr+8)
Z6hr = (LThr+20)

print(" ")
print("--- HEART RATE TRAINING ZONES ---")
print(" ")
print("Threshold HR = " + str(LThr))
print(" ")
print(f'Zone 1: Recovery        = < {Z1hr}')
print(f'Zone 2: Endurance       = {Z1hr} - {Z2hr}')
print(f'Zone 3: Tempo           = {Z2hr} - {Z3hr}')
print(f'Zone 4: Sub-Threshold   = {Z3hr} - {Z4hr}')
print(f'Zone 5: Supra-Threshold = {Z4hr} - {Z5hr}')
print(f'Zone 6: VO2             = > {Z5hr}')

## RUNNING POWER TRAINING ZONES CALCULATOR ##
LTpwr = 300

Z1pwr = int(LTpwr*0.6)
Z2pwr = int(LTpwr*0.8)
Z3pwr = int(LTpwr*0.92)
Z4pwr = int(LTpwr)
Z5pwr = int(LTpwr*1.08)
Z6pwr = int(LTpwr*1.15)

print(" ")
print("--- POWER TRAINING ZONES ---")
print(" ")
print("Threshold POWER = " + str(LTpwr))
print(" ")
print(f'Zone 1: Recovery        = < {Z1pwr}')
print(f'Zone 2: Endurance       = {Z1pwr} - {Z2pwr}')
print(f'Zone 3: Tempo           = {Z1pwr} - {Z2pwr}')
print(f'Zone 4: Sub-Threshold   = {Z1pwr} - {Z2pwr}')
print(f'Zone 5: Supra-Threshold = {Z1pwr} - {Z2pwr}')
print(f'Zone 6: VO2             = {Z1pwr} - {Z2pwr}')
print(f'Zone 7: Neuro/AC           = < {Z1pwr}')

## RUNNING PACE ZONES CALCULATOR ##
LTpace = '7:00'
split_pace = LTpace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds

Z1pace = int(pace*1.4)
Z2pace = int(pace*1.2)
Z3pace = int(pace*1.08)
Z4pace = int(pace)
Z5pace = int(pace*0.92)
Z6pace = int(pace*0.85)

Z1min = Z1pace//60
Z2min = Z2pace//60
Z3min = Z3pace//60
Z4min = Z4pace//60
Z5min = Z5pace//60
Z6min = Z6pace//60

Z1sec = Z1pace % 60
Z2sec = Z2pace % 60
Z3sec = Z3pace % 60
Z4sec = Z4pace % 60
Z5sec = Z5pace % 60
Z6sec = Z6pace % 60

print(" ")
print("--- PACE TRAINING ZONES ---")
print(" ")
print("Threshold PACE = " + str(LTpace))
print(" ")
print(f'Zone 1: Recovery        = < {Z1min}:{Z1sec:02d}')
print(f'Zone 2: Endurance       = {Z1min}:{Z1sec:02d} - {Z2min}:{Z2sec:02d}')
print(f'Zone 3: Tempo           = {Z2min}:{Z2sec:02d} - {Z3min}:{Z3sec:02d}')
print(f'Zone 4: Sub-Threshold   = {Z3min}:{Z3sec:02d} - {Z4min}:{Z4sec:02d}')
print(f'Zone 5: Supra-Threshold = {Z4min}:{Z4sec:02d} - {Z5min}:{Z5sec:02d}')
print(f'Zone 6: VO2             = {Z5min}:{Z5sec:02d} - {Z6min}:{Z6sec:02d}')
print(f'Zone 7: Neuro/AC       = > {Z6min}:{Z6sec:02d}')
