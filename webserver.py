import traceback
from WebApp.WebServer.Server import Server
from WebApp.WebServer.NetworkDeviceDatabase import NetworkDeviceDatabase
from switch_src import SSH

def main():
    database=NetworkDeviceDatabase('Network.db')
    try:
        # Pass connection method to server class
        server = Server(database=database, connect_method=SSH.connect)
        server.run(debug=False)
    except:
        print('Error starting server: ')
        print(traceback.print_exc())
    finally:
        database.close()

if __name__ == "__main__":
    main()