import expipe.io
import os
import os.path as op
import json
import quantities as pq




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

        template = {
            "identifier": name,
            "name": result["name"],
            "definition": result["definition"]
        }
        result.pop('name')
        result.pop('definition')
        # expipe.io.core.db.child("templates").child(name).set(template, expipe.io.core.user["idToken"])
        # expipe.io.core.db.child("templates_contents").child(name).set(result, expipe.io.core.user["idToken"])
