import traceback, argparse, logging
from WebApp.WebServer.Server import Server
from WebApp.WebServer.NetworkDeviceDatabase import NetworkDeviceDatabase
from switch_src import SSH

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=0)
    parser.add_argument('-l','--logfile', help='Saves all logging to a text file')
    args = parser.parse_args()

    logmap = [logging.ERROR,logging.WARNING,logging.INFO,logging.DEBUG]
    logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
    log_args = {'level':logmap[args.verbose]}
    if args.logfile:
        log_args['filename'] = args.logfile
        log_args['filemode'] = 'w'
    logging.basicConfig(**log_args)

    database=NetworkDeviceDatabase('Network.db')
    try:
        # Pass connection method to server class
        server = Server(database=database, connect_method=SSH.connect)
        server.run()
    except:
        print('Error starting server: ')
        print(traceback.print_exc())
    finally:
        database.close()

if __name__ == "__main__":
    main()