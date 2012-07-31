#import lib.bottle as bottle
import bottle

bottle.debug(True)

@bottle.route('/')
def index(name='World'):
    return bottle.template('index', name='bonk')

@bottle.route('/static/<filename:re:.*\.css>')
def static_css(filename):
    return bottle.static_file(filename, root='htdocs/css', mimetype='text/css')

@bottle.route('/static/<filename:re:.*\.js>')
def static_js(filename):
    return bottle.static_file(filename, root='htdocs/js',
                              mimetype='application/x-javascript')

bottle.run(host='localhost', port=8080)
