import expipe.io
import os
import os.path as op
import json
import quantities as pq


def list_convert(value):
    result = value
    if isinstance(value, dict):
        if 'value' in value and 'type' in value:
            if value['type'] == 'list':
                if isinstance(value['value'], str):
                    if not len(value['value']) == 0:
                        value['value'] = value['value'].split(',')
            del value['type']
        if 'note' in value:
            del value['note']
        if 'notes' in value:
            del value['notes']
        elif 'value' in value and 'unit' in value:
            if isinstance(value['value'], str):
                if not len(value['value']) == 0:
                    value['value'] = value['value'].split(',')
        elif 'value' in value and 'units' in value:
            value['unit'] = value['units']
            del(value['units'])
            if isinstance(value['value'], str):
                if not len(value['value']) == 0:
                    value['value'] = value['value'].split(',')
        else:
            for key, val in result.items():
                result[key] = list_convert(val)
    return result


for root, dirs, files in os.walk('templates'):
    for fname in files:
        group = op.split(root)[1]
        name = group + '_' + op.splitext(fname)[0]
        with open(op.join(root, fname), 'r') as infile:
            try:
                result = json.load(infile)
            except:
                print(fname)
                raise
        result = list_convert(result)
        with open(op.join(root, fname), 'w') as outfile:
            json.dump(result, outfile,
                      sort_keys=True, indent=4)
