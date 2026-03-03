require 'webrick'
server = WEBrick::HTTPServer.new(
  Port: 8080,
  DocumentRoot: '/Users/fabianwillisimon/Documents/VD Wireframes'
)
trap('INT') { server.shutdown }
server.start
