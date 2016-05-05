import logging

# Set the log output file, and the log level
logging.bbasicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associated name.
    
    Returns the name and the snippet
    """
    logging.error("FIXME: unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
