import json
import io
import os
from datetime import datetime

# edi_good_file = 'justin.edi'
# edi_999_file = 'justin-999.edi'
json_in_file = 'justin.json'
# json_out_file = 'justin-updated.json'

def edi_envelope_to_json(edi_good_file, edi_999_file):
    head, tail = os.path.split(edi_good_file)
    json_out_file = '999/' + tail + '.json'
    edi_delim = '*'

    envelope_info = {}
    with open(edi_good_file) as edi_good:
        for line in edi_good:
            elements = line.split(edi_delim)
            segment = elements[0]
            if segment in ['ISA', 'IEA', 'GS', 'GE']:
                envelope_info[segment] = elements

    envelope_info_999 = {}
    with open(edi_999_file) as edi_999:
        for line in edi_999:
            elements = line.split(edi_delim)
            segment = elements[0]
            if segment in ['ISA', 'IEA', 'GS', 'GE']:
                envelope_info_999[segment] = elements

    if envelope_info_999['ISA'][13] not in envelope_info['ISA'][13]:
        print(edi_good_file + ' ' + edi_999_file)
        print('ISA[13] does not match between 837 and 999') 
        return   

    job_part_0_json = None

    with open(json_in_file) as json_data:
        job_part_0_json = json.load(json_data)

    job_part_0_json[0]['ISAForCXM']['AuthorizationInformationQualifier_1'] = envelope_info['ISA'][1]
    job_part_0_json[0]['ISAForCXM']['AuthorizationInformation_2'] = envelope_info['ISA'][2]
    job_part_0_json[0]['ISAForCXM']['SecurityInformationQualifier_3'] = envelope_info['ISA'][3]
    job_part_0_json[0]['ISAForCXM']['SecurityInformation_4'] = envelope_info['ISA'][4]
    job_part_0_json[0]['ISAForCXM']['SenderIDQualifier_5'] = envelope_info['ISA'][5]
    job_part_0_json[0]['ISAForCXM']['InterchangeSenderID_6'] = envelope_info['ISA'][6]
    job_part_0_json[0]['ISAForCXM']['ReceiverIDQualifier_7'] = envelope_info['ISA'][7]
    job_part_0_json[0]['ISAForCXM']['InterchangeReceiverID_8'] = envelope_info['ISA'][8]
    job_part_0_json[0]['ISAForCXM']['InterchangeDate_9'] = envelope_info['ISA'][9]
    job_part_0_json[0]['ISAForCXM']['InterchangeTime_10'] = envelope_info['ISA'][10]
    job_part_0_json[0]['ISAForCXM']['InterchangeControlStandardsIdentifier_11'] = envelope_info['ISA'][11]
    job_part_0_json[0]['ISAForCXM']['InterchangeControlVersionNumber_12'] = envelope_info['ISA'][12]
    job_part_0_json[0]['ISAForCXM']['InterchangeControlNumber_13'] = envelope_info['ISA'][13]
    job_part_0_json[0]['ISAForCXM']['AcknowledgementRequested_14'] = envelope_info['ISA'][14]
    job_part_0_json[0]['ISAForCXM']['UsageIndicator_15'] = envelope_info['ISA'][15]
    job_part_0_json[0]['ISAForCXM']['ComponentElementSeparator_16'] = envelope_info['ISA'][16]

    job_part_0_json[0]['GSForCXM']['CodeIdentifyingInformationType_1'] = envelope_info['GS'][1]
    job_part_0_json[0]['GSForCXM']['SenderIDCode_2'] = envelope_info['GS'][2]
    job_part_0_json[0]['GSForCXM']['ReceiverIDCode_3'] = envelope_info['GS'][3]
    job_part_0_json[0]['GSForCXM']['Date_4'] = envelope_info['GS'][4]
    job_part_0_json[0]['GSForCXM']['Time_5'] = envelope_info['GS'][5]
    job_part_0_json[0]['GSForCXM']['GroupControlNumber_6'] = envelope_info['GS'][6]
    job_part_0_json[0]['GSForCXM']['TransactionTypeCode_7'] = envelope_info['GS'][7]
    job_part_0_json[0]['GSForCXM']['VersionAndRelease_8'] = envelope_info['GS'][8]

    job_part_0_json[0]['GEForCXM']['NumberOfIncludedSets_1'] = envelope_info['GE'][1]
    job_part_0_json[0]['GEForCXM']['GroupControlNumber_2'] = envelope_info['GE'][1]

    job_part_0_json[0]['IEAForCXM']['NumberOfIncludedGroups_1'] = envelope_info['IEA'][1]
    job_part_0_json[0]['IEAForCXM']['InterchangeControlNumber_2'] = envelope_info['IEA'][2]

    job_part_0_json[0]['TS999'][0]['ISA']['AuthorizationInformationQualifier_1'] = envelope_info_999['ISA'][1]
    job_part_0_json[0]['TS999'][0]['ISA']['AuthorizationInformation_2'] = envelope_info_999['ISA'][2]
    job_part_0_json[0]['TS999'][0]['ISA']['SecurityInformationQualifier_3'] = envelope_info_999['ISA'][3]
    job_part_0_json[0]['TS999'][0]['ISA']['SecurityInformation_4'] = envelope_info_999['ISA'][4]
    job_part_0_json[0]['TS999'][0]['ISA']['SenderIDQualifier_5'] = envelope_info_999['ISA'][5]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeSenderID_6'] = envelope_info_999['ISA'][6]
    job_part_0_json[0]['TS999'][0]['ISA']['ReceiverIDQualifier_7'] = envelope_info_999['ISA'][7]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeReceiverID_8'] = envelope_info_999['ISA'][8]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeDate_9'] = envelope_info_999['ISA'][9]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeTime_10'] = envelope_info_999['ISA'][10]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeControlStandardsIdentifier_11'] = envelope_info_999['ISA'][11]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeControlVersionNumber_12'] = envelope_info_999['ISA'][12]
    job_part_0_json[0]['TS999'][0]['ISA']['InterchangeControlNumber_13'] = envelope_info_999['ISA'][13]
    job_part_0_json[0]['TS999'][0]['ISA']['AcknowledgementRequested_14'] = envelope_info_999['ISA'][14]
    job_part_0_json[0]['TS999'][0]['ISA']['UsageIndicator_15'] = envelope_info_999['ISA'][15]
    job_part_0_json[0]['TS999'][0]['ISA']['ComponentElementSeparator_16'] = envelope_info_999['ISA'][16]

    job_part_0_json[0]['TS999'][0]['GS']['CodeIdentifyingInformationType_1'] = envelope_info_999['GS'][1]
    job_part_0_json[0]['TS999'][0]['GS']['SenderIDCode_2'] = envelope_info_999['GS'][2]
    job_part_0_json[0]['TS999'][0]['GS']['ReceiverIDCode_3'] = envelope_info_999['GS'][3]
    job_part_0_json[0]['TS999'][0]['GS']['Date_4'] = envelope_info_999['GS'][4]
    job_part_0_json[0]['TS999'][0]['GS']['Time_5'] = envelope_info_999['GS'][5]
    job_part_0_json[0]['TS999'][0]['GS']['GroupControlNumber_6'] = envelope_info_999['GS'][6]
    job_part_0_json[0]['TS999'][0]['GS']['TransactionTypeCode_7'] = envelope_info_999['GS'][7]
    job_part_0_json[0]['TS999'][0]['GS']['VersionAndRelease_8'] = envelope_info_999['GS'][8]

    job_part_0_json[0]['TS999'][0]['GE']['NumberOfIncludedSets_1'] = envelope_info_999['GE'][1]
    job_part_0_json[0]['TS999'][0]['GE']['GroupControlNumber_2'] = envelope_info_999['GE'][2]

    job_part_0_json[0]['TS999'][0]['IEA']['NumberOfIncludedGroups_1'] = envelope_info_999['IEA'][1]
    job_part_0_json[0]['TS999'][0]['IEA']['InterchangeControlNumber_2'] = envelope_info_999['IEA'][2]

    with io.open(json_out_file, 'w', newline='\n') as file:
            file.write(json.dumps(job_part_0_json, indent=2))