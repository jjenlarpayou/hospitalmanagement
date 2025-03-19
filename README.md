# hospitalmanagement
## Overview
<p>Hospital management is designed for staff working in Hospital. Staff can see the combined result
and information from each page of the web app. The demonstration shows the initial working of
this web application.</p>

## Technologies Used
- **Programming:** Python, SQL, HTML(Bootstrap), CSS
- **Database:** MySQL
- **Web Framework:** Flask
- **Software:** VS Code, XAMPP (For localhost and SQL database):

## How to Run the Project ##
This project is a **Flask-based Hospital Management System** that uses **MySQL** as the database and **HTML/CSS** for the frontend.

### Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.x** (Download: [python.org](https://www.python.org/downloads/))
- **MySQL Server** (Download: [mysql.com](https://dev.mysql.com/downloads/))
- **MySQL Connector for Python** (`mysql-connector-python`)
- **Flask** (`flask`, `flask-mysqldb`)

## Key Features
<p>There are 7 pages (Patient Registration, Medical record, Medicine, Room
management, Inpatient, Outpatient, and Doctor) that staff can access and manage the database.
This can be useful for inserting, deleting, and updating information. For example, firstly, staff
need to log in with a username and password to access the web app's first page. Secondly, they
can input patient information, importantly, it must be defined that this patient is “Inpatient” to
select room type or “Outpatient”. In this part, information will be automatically sent to those
tables. In terms of staff, they must update data such as `Incomingdate`, Outgoingdate, and status
“Check, Not check, or Discharge” which is linked to Room management table to calculate the
number of available rooms. Doctors can fill information in the Medical record such as
`Description`, `Prescription` and etc.</p>

### Demo
<div align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/b76624bb-a361-4f05-8d3c-c0816b3b5a7e"/>
<div align="center"><figcaption><b>Figure 1:</b> Login Page</figcaption></div>
</div>
<div align="center"><img width="450" alt="image" src="https://github.com/user-attachments/assets/2ee61d2e-40d1-4697-9039-07fbd3bf77c4" />
  <div align="center"><b>Figure 2:</b> Registration Page</div>
</div>
<div align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/f89faac4-ed66-442f-b006-bc9f2a28d3b5" />
  <div align="center"><div align="center"><b>Figure 3:</b> Insert Patient Dialog</div></div>
</div>
