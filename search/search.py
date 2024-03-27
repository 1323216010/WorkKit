from utils import find_files_plus


search_module = r'\\10.188.40.112\TEST_build data\PDX-L\PDX C3.0\PDX-L C3051\完成品'

module_paths = find_files_plus([search_module],
                        ['FTU', 'FTD', 'ListLog', 'GRR', 'PDX-R 97', '外观', '不良', '先行品', 'Debug', 'Raw'],
                        ['LimitLog'],
                        ['PDX_OQC_Tester'])

print(module_paths)



search_cube = r'\\10.188.40.112\TEST_build data\PDX-R\PDX-R C3054\Cube'

cube_mfg_paths = find_files_plus([search_cube],
                        ['FTU', 'FTD', 'ListLog', 'GRR', 'PDX-R 97', '外观', '不良', '先行品', 'Debug', 'Raw', 'OQC'],
                        ['LimitLog'],
                        ['PDX_MFG_Tester'])

cube_oqc_paths = find_files_plus([search_cube],
                        ['FTU', 'FTD', 'ListLog', 'GRR', 'PDX-R 97', '外观', '不良', '先行品', 'Debug', 'Raw', 'MFG'],
                        ['LimitLog'],
                        ['PDX_OQC_Tester'])

print(cube_mfg_paths)
print(cube_oqc_paths)

print()
