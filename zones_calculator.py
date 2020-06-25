##  FLATIRONS ENDURANCE TRAIANING ZONES CALCULATOR ##

## HEART RATE TRAINING ZONES CALCULATOR ##
LThr = 170

Z1hr = (LThr-20)
Z2hr = (LThr-10)
Z3hr = (LThr)
Z4hr = (LThr+10)
Z5hr = (LThr+20)

print(" ")
print("--- HEART RATE TRAINING ZONES ---")
print(" ")
print("Threshold HR = " + str(LThr))
print(" ")
print(f'Zone 1: Endurance        = < {Z1hr} bpm')
print(f'Zone 2: Tempo            = {Z1hr} bpm - {Z2hr} bpm')
print(f'Zone 3: Threshold        = {Z2hr} bpm - {Z3hr} bpm')
print(f'Zone 4: Interval         = {Z3hr} bpm - {Z4hr} bpm')
print(f'Zone 5: Speed            = {Z4hr} bpm - {Z5hr} bpm')

## RUNNING POWER TRAINING ZONES CALCULATOR ##
LTpwr = 300

Z1pwr = int(LTpwr*0.8)
Z2pwr = int(LTpwr*0.9)
Z3pwr = int(LTpwr)
Z4pwr = int(LTpwr*1.1)
Z5pwr = int(LTpwr*1.20)

print(" ")
print("--- POWER TRAINING ZONES ---")
print(" ")
print("Threshold POWER = " + str(LTpwr))
print(" ")
print(f'Zone 1: Endurance        = < {Z1pwr}W')
print(f'Zone 2: Tempo            = {Z1pwr}W - {Z2pwr}W')
print(f'Zone 3: Threshold        = {Z2pwr}W - {Z3pwr}W')
print(f'Zone 4: Interval         = {Z3pwr}W - {Z4pwr}W')
print(f'Zone 5: Speed            = {Z4pwr}W - {Z5pwr}W')
    
## RUNNING PACE ZONES CALCULATOR ##
LTpace = '7:00'
split_pace = LTpace.split(":")
minutes = int(split_pace[0])
seconds = int(split_pace[1])
pace = minutes * 60 + seconds

Z1pace = int(pace*1.2)
Z2pace = int(pace*1.1)
Z3pace = int(pace)
Z4pace = int(pace*0.90)
Z5pace = int(pace*0.80)

Z1min = Z1pace//60
Z2min = Z2pace//60
Z3min = Z3pace//60
Z4min = Z4pace//60
Z5min = Z5pace//60

Z1sec = Z1pace % 60
Z2sec = Z2pace % 60
Z3sec = Z3pace % 60
Z4sec = Z4pace % 60
Z5sec = Z5pace % 60

print(" ")
print("--- PACE TRAINING ZONES ---")
print(" ")
print("Threshold PACE = " + str(LTpace))
print(" ")
print(f'Zone 1: Endurance        = < {Z1min}:{Z1sec:02d}/mi')
print(f'Zone 2: Tempo            = {Z1min}:{Z1sec:02d}/mi - {Z2min}:{Z2sec:02d}/mi')
print(f'Zone 3: Threshold        = {Z2min}:{Z2sec:02d}/mi - {Z3min}:{Z3sec:02d}/mi')
print(f'Zone 4: Interval         = {Z3min}:{Z3sec:02d}/mi - {Z4min}:{Z4sec:02d}/mi')
print(f'Zone 5: Speed            = {Z4min}:{Z4sec:02d}/mi - {Z5min}:{Z5sec:02d}/mi')
