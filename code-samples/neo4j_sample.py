#pip install neo4j
#brew install neo4j <--installing the server
#<path/to/neo4j/dir>/bin/neo4j console

from neo4j.v1 import GraphDatabase

#configurations
uri = "bolt://localhost:7687"
userName = "neo4j"
password = "<password>"

#connect to the neo4j server
graphDB_Driver = GraphDatabase.driver(uri, auth=(userName, password), encrypted=False)

#executing the queries
with graphDB_Driver.session() as graphDB_Session:
    # Create nodes and relationships
    create_n_r = """CREATE
    (walter:person { name: "Walter", age: 72}),
    (edith:person { name: "Edith", age: 68}),
    (diana:person { name: "Diana", age: 51}),
    (edward:person { name: "Edward", age: 47}),
    (peter:person { name: "Peter", age: 15}),
    (john:person { name: "John", age: 12}),

    (walter)-[:husband_of {married_since: 1940}]->(edith),
    (edith)-[:wife_of {married_since: 1940}]->(walter),
    (edward)-[:son_of {}]->(walter),
    (walter)-[:father_of {}]->(edward),
    (edward)-[:son_of {}]->(edith),
    (edith)-[:mother_of {}]->(edward),
    (diana)-[:wife_of {married_since: 1968}]->(edward),
    (edward)-[:husband_of {married_since: 1968}]->(diana),
    (peter)-[:son_of {like_playing: 'tennis'}]->(edward),
    (edward)-[:father_of {like_playing: 'tennis'}]->(peter),
    (peter)-[:son_of {like_playing: 'chess'}]->(diana),
    (diana)-[:mother_of {like_playing: 'chess'}]->(peter),
    (john)-[:son_of {like_playing: 'baseball'}]->(edward),
    (edward)-[:father_of {like_playing: 'baseball'}]->(john),
    (john)-[:son_of {like_playing: 'baseball'}]->(diana),
    (diana)-[:mother_of {like_playing: 'baseball'}]->(john)
    """
    graphDB_Session.run(create_n_r)
    print("Nodes and relationships created...")

    #printing all the nodes
    person_list = "MATCH (x:person) RETURN x"
    nodes = graphDB_Session.run(person_list)

    print("\nNames of all the family members...")

    for node in nodes:
        print(node['x']['name'])
    print("")

    #query to identify the relationships of one node
    relationship_list = "MATCH (x:person {name:'Edward'})-[rel]->(y:person) RETURN y.name,rel"
    nodes = graphDB_Session.run(relationship_list)
    print("\nRelation between Edward and the rest of the family:")

    for node in nodes:
        print(node["rel"].type, node["y.name"])
    print("")


    #delete all the nodes and relationships
    clean = """
    MATCH (n)
    DETACH DELETE n
    """
    nodes = graphDB_Session.run(clean)
    print("All nodes and relationships cleaned...")