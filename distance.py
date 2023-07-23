import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import threading
import socket

# Load the pre-downloaded graph for a city (replace 'your_city_graph.graphml' with the file path of your pre-downloaded graph)
def get_distance(latitude1, longitude1, latitude2, longitude2, G):
    # location1 = (latitude1, longitude1)
    # location2 = (latitude2, longitude2)


    node1 = ox.distance.nearest_nodes(G, longitude1, latitude1)
    node2 = ox.distance.nearest_nodes(G, longitude2, latitude2)


    shortest_path = nx.shortest_path(G, node1, node2, weight='length')


    distance = nx.shortest_path_length(G, node1, node2, weight='length')

    # subgraph = G.subgraph(shortest_path)

    # fig, ax = ox.plot_graph_route(subgraph, shortest_path, route_linewidth=6, node_size=0, bgcolor='w', edge_color='r', edge_linewidth=2)


    # ax.scatter([longitude1, longitude2], [latitude1, latitude2], c='b', edgecolor='k', s=100, zorder=5)


    # plt.show()
    route_map = ox.plot_route_folium(G, shortest_path)
    route_map.save('test.html')

    return distance

def handle_client(client_socket, address, G):
    print(f"Connected: {address}")


    st = str(client_socket.recv(1024).decode()) 
    print(st)
    values = st.split(' ')


    result = get_distance(float(values[0]), float(values[1]), float(values[2]), float(values[3]), G)


    client_socket.send(str(result).encode('utf-8'))


    client_socket.close()


def start_server():

    HOST = '127.0.0.1'
    PORT = 8888
    g = ox.load_graphml(r'C:\Users\nirob\OneDrive\Desktop\LTMS\Dhaka\dhaka_drive.graphml')


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((HOST, PORT))


    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:

        client_socket, address = server_socket.accept()


        client_thread = threading.Thread(target=handle_client, args=(client_socket, address, g))
        client_thread.start()
        
start_server()