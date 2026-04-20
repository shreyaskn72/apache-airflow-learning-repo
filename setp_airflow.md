# 1. Install Docker Desktop on Mac OS


Download dmg file for mac os from the official docker website:

https://docs.docker.com/desktop/install/mac-install/

Make sure to download the correct version for your mac os (Intel or Apple silicon).


After downloading the dmg file, drag and drop the Docker icon to the Applications folder to install it. Once the installation is complete, you can launch Docker Desktop from the Applications folder.

For first time users, Docker Desktop may ask for permissions to access certain resources on your Mac. Make sure to grant the necessary permissions for Docker to function properly.

# 2. Setup Airflow server using Docker


After installing docker desktop, you can run the following commands to stup and start the airflow server.



## Permission to execute the script the start and stop script

chmod +x *.sh

## To start the server
./start_airflow.sh


After running the start script, it may take a few moments for the Airflow server to start up. 

After starting up the server you can access the following ui:

- Airflow UI: http://localhost:8080
- Flower UI: http://localhost:5555
- pg admin ui: http://localhost:5050
- Redis UI: http://localhost:5540


# 3. Stop the server

## To stop the server
./stop_airflow.sh

