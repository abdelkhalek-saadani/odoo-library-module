# Library Management Odoo Module

An Odoo module designed to simplify and streamline library management tasks, including book inventory, member management, and borrowing/returning books.

## Quick Start 

### Prerequisites 
- Docker and Docker Compose installed on your system 
- Odoo 15 Recommended (Works on version 16 and 17 too)

### Steps to get Started 

#### 1. Clone the repository
```bash
git clone https://github.com/abdelkhalek-saadani/odoo-library-module.git
cd odoo-library-module
```

#### 2. Setup Environment Variables 
- Copy the example .env file: 

```bash
cp .env.example .env
```

#### 3. Start the Application 
- Run the following command to start Odoo and PostgreSQL:
```bash
docker compose up 
``` 
- Access Odoo in your browser at [http://localhost:8069](http://localhost:8069)

#### 4. Install the Module 
- Log in to Odoo with admin credentials (admin:admin by default) 
- Go to **Apps**, search for "library"
- Click **Install**


<!-- TODO: Add Module Overview Section in README, description for the models and views -->

<!-- Add screenshots to the module views-->
