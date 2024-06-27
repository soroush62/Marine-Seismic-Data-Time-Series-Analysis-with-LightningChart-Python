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






# import segyio
# import numpy as np

# filename = 'D:/Computer Aplication/WorkPlacement/Projects/Project3/MGDS_Download/EW9907/ar42.0001.ew9907.nk-111.3dmigration.segy'

# with segyio.open(filename, "r", ignore_geometry=True) as segyfile:
#     segyfile.mmap()

#     # Print the binary header info
#     print("Binary Header Info:")
#     print(segyfile.bin)

#     # Print the number of traces in the file
#     print(f"Number of traces: {segyfile.tracecount}")

#     # Print the first few trace headers
#     print("Trace Headers:")
#     for i in range(5):
#         trace_header = segyfile.header[i]
#         print(f"Trace {i} header:")
#         for key in trace_header.keys():
#             print(f"{key}: {trace_header[key]}")
#         print("\n")

#     # Print the first few traces data
#     print("Trace Data:")
#     for i in range(5):
#         trace_data = segyfile.trace[i]
#         print(f"Trace {i} data (first 10 samples): {trace_data[:10]}")
#         print("\n")

#     # Identify trace fields
#     print("Trace Fields:")
#     for field in segyio.tracefield.keys.keys():
#         print(field)

#     # Optionally, you can retrieve specific trace field values, for example:
#     for i in range(5):
#         try:
#             inline = segyfile.header[i][segyio.TraceField.INLINE_3D]
#         except KeyError:
#             inline = 'N/A'
#         try:
#             crossline = segyfile.header[i][segyio.TraceField.CROSSLINE_3D]
#         except KeyError:
#             crossline = 'N/A'
#         print(f"Trace {i}: INLINE_3D = {inline}, CROSSLINE_3D = {crossline}")

