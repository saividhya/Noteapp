from flask import Flask, request, session, abort, jsonify
from models import *

def getTags():
    if 'user' not in session:
        abort(403)
    userEmail = session['user']['email']
    page = "user"
    if request.args.get('page') is not None:
        if request.args.get('page').lower() == "general": page = "general"
    tag_freqs = None

    if page == "user":
        tag_freqs = Note.objects(contributors__in=[userEmail]).item_frequencies('tags', normalize=True)
    elif page == "general":
        tag_freqs = Note.objects.item_frequencies('tags', normalize=True)

    result = []
    for key, value in tag_freqs.items():
        item = {}
        item['name'] = key
        item['normValue'] = value
        result.append(item)
    return jsonify(result)
