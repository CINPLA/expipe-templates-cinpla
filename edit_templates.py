import expipe
import os
import os.path as op
import json
import ruamel.yaml as yaml



for root, dirs, files in os.walk('templates'):
    for fname in files:
        if not fname.endswith('.json'):
            continue
        name = op.splitext(fname)[0]
        with open(op.join(root, fname), 'r') as infile:
            try:
                result = json.load(infile)
            except:
                print(fname)
                raise
        result['identifier'] = name
        if 'registered' in result:
            del(result['registered'])
        yamlpath = 'templates/' + name + '.yaml'
        if op.exists(yamlpath):
            print(name)
            continue
        with open(yamlpath, 'w') as f:
            yaml.dump(
                result, f,
                default_flow_style=False,
                allow_unicode=True,
                Dumper=yaml.RoundTripDumper)
