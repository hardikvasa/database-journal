from __future__  import print_function  # Python 2/3 compatibility

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

#initializing the graph object
graph = Graph()

#creating connection with the remote
remoteConn = DriverRemoteConnection('wss://<endpoint>:8182/gremlin','g')
g = graph.traversal().withRemote(DriverRemoteConnection('wss://<endpoint>:8182/gremlin','g'))

#clearing out all the vertices to start fresh
g.V().drop().iterate()

#Adding some vertices (nodes)
gerald = g.addV('person').property('age','81').property('first_name','Gerald').property('stays_in','Portland').next()
edith = g.addV('person').property('age','78').property('first_name','Edith').property('stays_in','Portland').next()
peter = g.addV('person').property('age','52').property('first_name','Shane').property('stays_in','Seattle').next()
mary = g.addV('person').property('age','50').property('first_name','Mary').property('stays_in','Seattle').next()
betty = g.addV('person').property('age','19').property('first_name','Betty').property('stays_in','Chicago').next()

#Adding relationships (edges)
edge = g.V().has('first_name', 'Gerald').addE('husband_of').to(g.V().has('first_name', 'Edith')).property('married_since','1947').next()
edge = g.V().has('first_name', 'Edith').addE('wife_of').to(g.V().has('first_name', 'Gerald')).property('married_since','1947').next()
edge = g.V().has('first_name', 'Shane').addE('son_of').to(g.V().has('first_name', 'Gerald')).property('known_since','1964').next()
edge = g.V().has('first_name', 'Gerald').addE('father_of').to(g.V().has('first_name', 'Shane')).property('known_since','1964').next()
edge = g.V().has('first_name', 'Shane').addE('son_of').to(g.V().has('first_name', 'Edith')).property('known_since','1964').next()
edge = g.V().has('first_name', 'Edith').addE('mother_of').to(g.V().has('first_name', 'Shane')).property('known_since','1964').next()
edge = g.V().has('first_name', 'Shane').addE('husband_of').to(g.V().has('first_name', 'Mary')).property('known_since','1989').next()
edge = g.V().has('first_name', 'Mary').addE('wife_of').to(g.V().has('first_name', 'Shane')).property('known_since','1989').next()
edge = g.V().has('first_name', 'Shane').addE('father_of').to(g.V().has('first_name', 'Betty')).property('known_since','1991').next()
edge = g.V().has('first_name', 'Betty').addE('daughter_of').to(g.V().has('first_name', 'Shane')).property('known_since','1991').next()
edge = g.V().has('first_name', 'Mary').addE('mother_of').to(g.V().has('first_name', 'Betty')).property('known_since','1991').next()
edge = g.V().has('first_name', 'Betty').addE('daughter_of').to(g.V().has('first_name', 'Mary')).property('known_since','1991').next()


#print out all the node's first names
print(g.V().first_name.toList()) 

#print out all the properties of person whose's first name is Shane
print(g.V().has('person','first_name','Shane').valueMap().next()) 

#traversing the graph starting with Betty to then Shane to then Edith
print(g.V().has('first_name', 'Betty').out('daughter_of').out('son_of').valueMap().toList())
print("\n\n\n")

#Print out all the nodes
people = g.V().valueMap().toList()
print(people)

#Print out all the connections (edges)
connections = g.E().valueMap().toList()
print(connections)

#Closing the connection
remoteConn.close()