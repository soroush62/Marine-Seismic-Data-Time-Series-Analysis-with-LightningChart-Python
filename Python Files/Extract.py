import obspy
import pandas as pd
import json

segy_file = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/f1289stk16.sgy'
st = obspy.read(segy_file, format='SEGY')

valid_keys = [
    'trace_sequence_number_within_line', 
    'trace_sequence_number_within_segy_file',
    'original_field_record_number',
    'trace_number_within_the_original_field_record',
    'energy_source_point_number',
    'source_coordinate_x',
    'source_coordinate_y',
    'sample_interval_in_ms_for_this_trace',
    'year_data_recorded'
]

data = []
for tr in st:
    trace_header = tr.stats.segy.trace_header
    trace_data = tr.data
    for i, value in enumerate(trace_data):
        row = {key: trace_header[key] for key in valid_keys if key in trace_header}
        row['trace_value'] = value
        row['sample_number'] = i
        data.append(row)

df = pd.DataFrame(data)

df.to_csv('D:/Computer Aplication/WorkPlacement/Projects/Project3/namss.F-12-89-HW.mcs.airgun/Data/output.csv', index=False)
