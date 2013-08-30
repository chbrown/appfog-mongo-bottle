import os
import sys
import json
import pymongo
from datetime import datetime
from bottle import Bottle, redirect, static_file, run, request

services = json.loads(os.getenv('VCAP_SERVICES', '{}'))
if services:
    assert 'mongodb-1.8' in services, 'Could not find mongodb service in VCAP_SERVICES! Did you run `af bind-service`?'

    print >> sys.stderr, 'Using mongodb from VCAP_SERVICES credentials'
    mongodb_uri = 'mongodb://%(username)s:%(password)s@%(hostname)s:%(port)d/%(db)s' % services['mongodb-1.8'][0]['credentials']
else:
    print >> sys.stderr, 'Using local mongodb'
    mongodb_uri = 'mongodb://localhost:27017'

print >> sys.stderr, 'Connecting to mongodb with pymongo==%s' % pymongo.version

connection = pymongo.Connection(mongodb_uri)
notes_collection = connection.db['notes']

# add a note at startup, just so there's at least one
startup_note = dict(text='Application started at %s' % datetime.now())
notes_collection.insert(startup_note)


application = Bottle()


@application.route('/')
def index():
    # redirect root url requests to a static page
    # which will get handled by static_dir below
    redirect('/static/basic.html')


@application.route('/static/<path:path>')
def static_dir(path):
    return static_file(path, root=os.path.join(os.getcwd(), 'static'))


@application.post('/notes/create')
def notes_create():
    text = request.forms.get('text')
    new_note = dict(text=text)
    notes_collection.insert(new_note)

    redirect('/static/basic.html')


@application.get('/notes/list')
def notes_list():
    print >> sys.stderr, 'Printing %d notes' % notes_collection.count()

    note_query = notes_collection.find(sort=[("_id", -1)])
    notes = [note.get('text', 'N/A') for note in note_query]

    # bottle will only jsonify dicts, not any json-friendly objects (like arrays)
    return dict(notes=notes)


if __name__ == '__main__':
    run(application)
