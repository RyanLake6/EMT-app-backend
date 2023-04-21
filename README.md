# EmergenKnow
EmergenKnow is a service designed to assist in managing critical emergency services. This specialized software enables organizations to optimize the efficiency and effectiveness of their operations by providing real-time information about resources and facilities. The relational database maintains a comprehensive record of every activity related to patient care - from dispatch to transportation and documentation. EmergenKnow helps managers track performance metrics such as response times and resource utilization, and allows patients to review their treatment from the EMS service.

## Setup
This repo contains setup for spinning up 3 Docker containers: 
- A MySQL 8 container for obvious reasons
- A Python Flask container to implement a REST API
- A Local AppSmith Server

### Spinning up Docker Containers
**Important - Docker Desktop must be installed and running.**

1. Clone this repository.
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL.
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp.
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`.