import expipe.io
import os
import os.path as op
import shutil
import json
import numpy as np
import exdir
import quantities as pq
import argparse
from expipe_io_neuro.axona import AxonaFilerecord
import datetime

for fname in os.listdir('templates'):
    name = fname.replace('.json', '')
    with open('templates/' + fname, 'r') as infile:
        try:
            result = json.load(infile)
        except:
            print(fname)
            raise

    template = {
        "identifier": name,
        "name": result["name"],
        "definition": result["definition"]
    }
    result.pop('name')
    result.pop('definition')
    expipe.io.core.db.child("templates").child(name).set(template, expipe.io.core.user["idToken"])
    expipe.io.core.db.child("templates_contents").child(name).set(result, expipe.io.core.user["idToken"])
