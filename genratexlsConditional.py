import pandas as pd
from itertools import product

# Base parameters
base_params = {
    'site address': ['US pre 2411', 'Non US pre 2411', 'US 2411',
                     'Non US 2411', 'US 2502', 'Non US 2502'],
    'Frequency Configuration': ['auto', 'manual', 'N/A']
}

# Generate valid combinations
rows = []
case_id = 1

for site in base_params['site address']:
    # Determine edge cluster based on US/Non-US
    is_us = site.startswith('US')
    edge_options = ['SAS'] if is_us else ['NON SAS']  # Strict enforcement

    # Handle pre-2411 sites
    if 'pre 2411' in site:
        for edge in edge_options:
            if edge == 'SAS':
                for band in ['48']:
                    for tier in ['GAA', 'PAL', 'GAA+PAL']:
                        for tech in ['4g', '5g', '4g+5g']:
                            rows.append({
                                'Test Case ID': case_id,
                                'site address': site,
                                'Core service deployment': 'N/A',
                                'edge cluster': edge,
                                'Spectrum band': band,
                                'Band tier': tier,
                                'radio technology': tech,
                                'Frequency Configuration': 'N/A'
                            })
                            case_id += 1
            else:  # NON SAS (Non-US only)
                for band in ['48', '77', '78', '79']:
                    tech = '5g' if band != '48' else ['4g', '5g', '4g+5g']
                    if band == '48':
                        for t in ['4g', '5g', '4g+5g']:
                            rows.append({
                                'Test Case ID': case_id,
                                'site address': site,
                                'Core service deployment': 'N/A',
                                'edge cluster': edge,
                                'Spectrum band': band,
                                'Band tier': 'N/A',
                                'radio technology': t,
                                'Frequency Configuration': 'N/A'
                            })
                            case_id += 1
                    else:
                        rows.append({
                            'Test Case ID': case_id,
                            'site address': site,
                            'Core service deployment': 'N/A',
                            'edge cluster': edge,
                            'Spectrum band': band,
                            'Band tier': 'N/A',
                            'radio technology': tech,
                            'Frequency Configuration': 'N/A'
                        })
                        case_id += 1
        continue

    # Handle 2411 sites
    elif '2411' in site:
        for freq_config in ['auto', 'manual']:
            for edge in edge_options:
                if edge == 'SAS':
                    for band in ['48']:
                        for tier in ['GAA', 'PAL', 'GAA+PAL']:
                            for tech in ['4g', '5g', '4g+5g']:
                                rows.append({
                                    'Test Case ID': case_id,
                                    'site address': site,
                                    'Core service deployment': 'N/A',
                                    'edge cluster': edge,
                                    'Spectrum band': band,
                                    'Band tier': tier,
                                    'radio technology': tech,
                                    'Frequency Configuration': freq_config
                                })
                                case_id += 1
                else:  # NON SAS (Non-US only)
                    for band in ['48', '77', '78', '79']:
                        tech = '5g' if band != '48' else ['4g', '5g', '4g+5g']
                        if band == '48':
                            for t in ['4g', '5g', '4g+5g']:
                                rows.append({
                                    'Test Case ID': case_id,
                                    'site address': site,
                                    'Core service deployment': 'N/A',
                                    'edge cluster': edge,
                                    'Spectrum band': band,
                                    'Band tier': 'N/A',
                                    'radio technology': t,
                                    'Frequency Configuration': freq_config
                                })
                                case_id += 1
                        else:
                            rows.append({
                                'Test Case ID': case_id,
                                'site address': site,
                                'Core service deployment': 'N/A',
                                'edge cluster': edge,
                                'Spectrum band': band,
                                'Band tier': 'N/A',
                                'radio technology': tech,
                                'Frequency Configuration': freq_config
                            })
                            case_id += 1

    # Handle 2502 sites
    else:  # US 2502 or Non US 2502
        for freq_config in ['auto', 'manual']:
            for core in ['Edge (2025)', 'Edgeless (2025)']:
                for edge in edge_options:
                    if edge == 'SAS':
                        for band in ['48']:
                            for tier in ['GAA', 'PAL', 'GAA+PAL']:
                                for tech in ['4g', '5g', '4g+5g']:
                                    rows.append({
                                        'Test Case ID': case_id,
                                        'site address': site,
                                        'Core service deployment': core,
                                        'edge cluster': edge,
                                        'Spectrum band': band,
                                        'Band tier': tier,
                                        'radio technology': tech,
                                        'Frequency Configuration': freq_config
                                    })
                                    case_id += 1
                    else:  # NON SAS (Non-US only)
                        for band in ['48', '77', '78', '79']:
                            tech = '5g' if band != '48' else ['4g', '5g', '4g+5g']
                            if band == '48':
                                for t in ['4g', '5g', '4g+5g']:
                                    rows.append({
                                        'Test Case ID': case_id,
                                        'site address': site,
                                        'Core service deployment': core,
                                        'edge cluster': edge,
                                        'Spectrum band': band,
                                        'Band tier': 'N/A',
                                        'radio technology': t,
                                        'Frequency Configuration': freq_config
                                    })
                                    case_id += 1
                            else:
                                rows.append({
                                    'Test Case ID': case_id,
                                    'site address': site,
                                    'Core service deployment': core,
                                    'edge cluster': edge,
                                    'Spectrum band': band,
                                    'Band tier': 'N/A',
                                    'radio technology': tech,
                                    'Frequency Configuration': freq_config
                                })
                                case_id += 1

# Create DataFrame
df = pd.DataFrame(rows)

# Save to Excel
df.to_excel("siteArchit_testcases.xlsx", index = False)
print(f"Generated {len(df)} test cases in siteArchit_testcases.xlsx")
print("Key rules applied:")
print("1. Channel Width column removed from all cases")
print("2. US sites only have SAS edge clusters")
print("3. Non-US sites only have NON SAS edge clusters (strict enforcement)")
print("4. Band Tier only applies to SAS sites")
print("5. Core Service Deployment only for 2502 sites")
print("6. Pre-2411 sites have Frequency Configuration = 'N/A'")