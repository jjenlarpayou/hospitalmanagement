import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import re
import mysql.connector
app = Flask(__name__, template_folder='templates', static_folder='templates')
connection = mysql.connector.connect(host= 'localhost',
                                     database= 'Hospital',
                                     user='root',
                                     password='')


# Render templete
@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': # Check username and password
            error = 'Please try again.'
        else:
            return redirect('/registration')
    return render_template('login.html')

# Render Patient Registration
@app.route("/registration" , methods=['GET', 'POST'])
def registration():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patient")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('registration.html', patients = fetchdata)

# Render Doctor Page
@app.route("/doctor" , methods=['GET', 'POST'])
def doctor():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Doctor")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('doctor.html', doctors = fetchdata)

# Render Room Management Page
@app.route("/room" , methods=['GET', 'POST'])
def room():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Roomtype")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('roommangement.html', rooms = fetchdata)

# Render Medical Record Page
@app.route("/medicalrecord" , methods=['GET', 'POST'])
def medicalrecord():
    cursor = connection.cursor()
    # Join Query
    cursor.execute("""SELECT `Medical Record`.Mrecord_id, Doctor.Doctor_id, Doctor.D_fname, Doctor.D_lname, Patient.Patient_id, Patient.P_fname, Patient.P_lname , 
                   `Medical Record`.Description, `Medical Record`.Prescription 
                   FROM `Medical Record` 
                   INNER JOIN Doctor ON `Medical Record`.Doctor_id = Doctor.Doctor_id 
                   INNER JOIN Patient ON `Medical Record`.Patient_id = Patient.Patient_id 
                   ORDER BY `Medical Record`.Mrecord_id;""")
    fetchdata_join = cursor.fetchall()
    cursor.execute("SELECT `Doctor_id` FROM `Doctor`")
    fetchdata_doctorid = cursor.fetchall()
    cursor.execute("SELECT `Patient_id` FROM `Patient`")
    fetchdata_patientid = cursor.fetchall()
    
    cursor.close()
    return render_template('medicalrecord.html', medicalrecords = fetchdata_join, doctors = fetchdata_doctorid, patients = fetchdata_patientid)

# Render Medicine Page
@app.route("/medicine" , methods=['GET', 'POST'])
def medicine():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Medicine")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('medicine.html', medicine = fetchdata)

# Render Outpatient Page
@app.route("/outpatient" , methods=['GET', 'POST'])
def outpatient():
    cursor = connection.cursor()
    # Join Query
    cursor.execute("""SELECT `Outpatient`.`Patient_id`, Patient.P_fname, Patient.P_lname, Patient.P_gender, 
                   Patient.P_phonenumber, `Outpatient`.`Opt_incomingdate`, `Outpatient`.`Opt_outgoingdate` 
                   FROM `Outpatient` 
                   INNER JOIN Patient ON `Outpatient`.Patient_id = Patient.Patient_id;""")
    fetchdata = cursor.fetchall()
    cursor.close()
    return render_template('outpatient.html', outpatients = fetchdata)

# Render Inpatient Page
@app.route("/inpatient" , methods=['GET', 'POST'])
def inpatient():
    cursor = connection.cursor()
    # Join Query
    cursor.execute("""SELECT `Inpatient`.`Patient_id`, Patient.P_fname, Patient.P_lname, Patient.P_gender, 
                   Patient.P_phonenumber, Roomtype.R_id, Roomtype.Type, `Inpatient`.`Ipt_incomingdate`, 
                   `Inpatient`.`Ipt_outgoingdate`, `Inpatient`.P_check 
                   FROM `Inpatient` 
                   INNER JOIN Patient ON `Inpatient`.Patient_id = Patient.Patient_id 
                   INNER JOIN Roomtype ON `Inpatient`.R_id = Roomtype.R_id
                   ORDER BY `Inpatient`.`Patient_id`;""")
    fetchdata = cursor.fetchall()
    cursor.execute("SELECT `R_id`  FROM `Roomtype`;")
    fetchdata_roomid = cursor.fetchall()
    cursor.close()
    return render_template('inpatient.html', inpatients = fetchdata, roomids = fetchdata_roomid)

# Insert Functions
# Insert Patient
@app.route("/insert", methods=['GET', 'POST'])
def insert():
     if request.method == 'POST':
        flash("Data Inserted Successfully")
        patient_id = request.form['Patient_id']
        p_fname = request.form['P_fname']
        p_lname = request.form['P_lname']
        p_gender = request.form['P_gender']
        p_dob = request.form['P_dob']
        p_address = request.form['P_address']
        p_phonenumber = request.form['P_phonenumber']
        p_status = request.form['P_status']
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO `Patient`(`Patient_id`, `P_fname`, `P_lname`, `P_gender`, `P_dob`, `P_address`, `P_phonenumber`, `P_status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                       ,(patient_id, p_fname, p_lname, p_gender, p_dob, p_address, p_phonenumber, p_status))
        connection.commit()
        # Check Status and Insert to Inpatient or Outpatient tables
        if p_status == 'Inpatient':
            r_id = request.form['R_id']
            cursor.execute("""INSERT INTO `Inpatient` (`Patient_id`,`R_id`) VALUES ("""+patient_id+""",'"""+r_id+"""')""")
        elif p_status == 'Outpatient':
            cursor.execute("""INSERT INTO `Outpatient` (`Patient_id`) VALUES ("""+patient_id+""")""")
        connection.commit()
        cursor.close()    
        return redirect(url_for('registration'))
    
# Insert Doctor
@app.route("/insert/doctor", methods=['GET', 'POST'])
def insertdoctor():
     if request.method == 'POST':
        flash("Data Inserted Successfully")
        doctor_id = request.form['Doctor_id']
        d_fname = request.form['D_fname']
        d_lname = request.form['D_lname']
        d_address = request.form['D_address']
        d_phonenumber = request.form['D_phonenumber']
        d_email = request.form['D_email']
        d_speciality = request.form['D_speciality']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `Doctor`(`Doctor_id`, `D_fname`, `D_lname`, `D_address`, `D_phonenumber`, `D_email`,`D_speciality`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                       ,(doctor_id, d_fname, d_lname, d_address, d_phonenumber, d_email, d_speciality))
        connection.commit()
        cursor.close()
        return redirect(url_for('doctor'))
    
# Insert Room
@app.route("/insert/room", methods=['GET', 'POST'])
def insertroom():
     if request.method == 'POST':
        flash("Data Inserted Successfully")
        r_id = request.form['R_id']
        type = request.form['Type']
        r_cost = request.form['R_cost']
        r_quantity = request.form['R_quantity']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `Roomtype`(`R_id`, `Type`, `R_cost`, `R_quantity`) VALUES (%s, %s, %s, %s)"
                       ,(r_id, type, r_cost, r_quantity))
        connection.commit()
        cursor.close()
        return redirect(url_for('room'))

# Insert Medicine
@app.route("/insert/medicine", methods=['GET', 'POST'])
def insertmedicine():
     if request.method == 'POST':
        flash("Data Inserted Successfully")
        medicine_id = request.form['Medicine_id']
        mdc_medname = request.form['Mdc_medname']
        mdc_incomingdate = request.form['Mdc_incomingdate']
        mdc_expdate = request.form['Mdc_expdate']
        mdc_tablet = request.form['Mdc_tablet']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `Medicine`(`Medicine_id`, `Mdc_medname`, `Mdc_incomingdate`, `Mdc_expdate`,`Mdc_tablet`) VALUES (%s, %s, %s, %s, %s)"
                       ,(medicine_id, mdc_medname, mdc_incomingdate, mdc_expdate, mdc_tablet))
        connection.commit()
        cursor.close()
        return redirect(url_for('medicine'))

# Insert Medicalrecord
@app.route("/insert/medicalrecord", methods=['GET', 'POST'])
def insertmedicalrecord():
    if request.method == 'POST':
        flash("Data Inserted Successfully")
        mrecord_id = request.form['Mrecord_id']
        doctor_id = request.form['Doctor_id']
        patient_id = request.form['Patient_id']
        description = request.form['Description']
        prescription = request.form['Prescription']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO `Medical Record`(`Mrecord_id`, `Doctor_id`, `Patient_id`,`Description`,`Prescription`) VALUES (%s, %s, %s, %s, %s)"
                       ,(mrecord_id, doctor_id, patient_id, description, prescription))
        connection.commit()
        cursor.close()
        return redirect(url_for('medicalrecord'))

# Update Functions
# Update Patient
@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        patient_id = request.form['Patient_id']
        p_fname = request.form['P_fname']
        p_lname = request.form['P_lname']
        p_gender = request.form['P_gender']
        p_dob = request.form['P_dob']
        p_address = request.form['P_address']
        p_phonenumber = request.form['P_phonenumber']
        p_status = request.form['P_status']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Patient` 
                       SET `P_fname`= %s, `P_lname`= %s, `P_gender`= %s, `P_dob`= %s, `P_address`= %s, `P_phonenumber`= %s, `P_status`= %s 
                       WHERE `Patient_id` = %s
                       """, (p_fname, p_lname, p_gender, p_dob, p_address, p_phonenumber, p_status, patient_id))
        connection.commit()
        cursor.close()
        return redirect(url_for('registration'))

# Update Doctor
@app.route("/update/doctor", methods=['GET', 'POST'])
def updatedoctor():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        doctor_id = request.form['Doctor_id']
        d_fname = request.form['D_fname']
        d_lname = request.form['D_lname']
        d_address = request.form['D_address']
        d_phonenumber = request.form['D_phonenumber']
        d_email = request.form['D_email']
        d_speciality = request.form['D_speciality']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Doctor` 
                       SET `D_fname`= %s, `D_lname`= %s, `D_address`= %s, `D_phonenumber`= %s, `D_email`= %s, `D_speciality`= %s 
                       WHERE `Doctor_id` = %s
                       """, (d_fname, d_lname, d_address, d_phonenumber, d_email, d_speciality, doctor_id))
        connection.commit()
        cursor.close()
        return redirect(url_for('doctor'))

# Update Room
@app.route("/update/room", methods=['GET', 'POST'])
def updateroom():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        r_id = request.form['R_id']
        type = request.form['Type']
        r_cost = request.form['R_cost']
        r_quantity = request.form['R_quantity']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Roomtype` 
                       SET `Type`= %s, `R_cost`= %s, `R_quantity`= %s
                       WHERE `R_id` = %s
                       """, (type, r_cost, r_quantity, r_id))
        connection.commit()
        return redirect(url_for('room'))

# Update Medicine
@app.route("/update/medicine", methods=['GET', 'POST'])
def updatemedicine():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        medicine_id = request.form['Medicine_id']
        mdc_medname = request.form['Mdc_medname']
        mdc_incomingdate = request.form['Mdc_incomingdate']
        mdc_expdate = request.form['Mdc_expdate']
        mdc_tablet = request.form['Mdc_tablet']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Medicine` 
                       SET `Mdc_medname`= %s, `Mdc_incomingdate`= %s, `Mdc_expdate`= %s, `Mdc_tablet`= %s
                       WHERE `Medicine_id` = %s
                       """, (mdc_medname, mdc_incomingdate, mdc_expdate, mdc_tablet, medicine_id))
        connection.commit()
        cursor.close()
        return redirect(url_for('medicine'))

# Update Medical Record
@app.route("/update/medicalrecord", methods=['GET', 'POST'])
def updatemedicalrecord():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        mrecord_id = request.form['Mrecord_id']
        doctor_id = request.form['Doctor_id']
        patient_id = request.form['Patient_id']
        description = request.form['Description']
        prescription = request.form['Prescription']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Medical Record`
                       SET `Doctor_id`= %s, `Patient_id`= %s, `Description`= %s, `Prescription`= %s
                       WHERE `Mrecord_id` = %s
                       """,(doctor_id, patient_id, description, prescription, mrecord_id))
        connection.commit()
        cursor.close()
        return redirect(url_for('medicalrecord'))
    
# Update Outpatient
@app.route("/update/outpatient", methods=['GET', 'POST'])
def updateoutpatient():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        patient_id = request.form['Patient_id']
        incomingdate = request.form['Opt_incomingdate']
        outgoingdate = request.form['Opt_outgoingdate']
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE `Outpatient`
                       SET `Opt_incomingdate`= %s, `Opt_outgoingdate`= %s
                       WHERE `Patient_id` = %s
                       """,(incomingdate, outgoingdate, patient_id))
        connection.commit()
        cursor.close()
        return redirect(url_for('outpatient'))
    
 # Update Inpatient
@app.route("/update/inpatient", methods=['GET', 'POST'])
def updateinpatient():
    if request.method == 'POST':
        flash("Data Updated Successfully")
        patient_id = request.form['Patient_id']
        p_check = request.form['P_check']
        r_id = request.form['R_id']
        incomingdate = request.form['Ipt_incomingdate']
        outgoingdate = request.form['Ipt_outgoingdate']
        cursor = connection.cursor()
        cursor.execute("UPDATE `Inpatient` SET `Ipt_incomingdate`= %s, `Ipt_outgoingdate`= %s ,`P_check` = %s WHERE `Inpatient`.`Patient_id` = %s ",(incomingdate, outgoingdate, p_check, patient_id))
        connection.commit()
        cursor.execute("SELECT `R_id`,COUNT(R_id),`P_check` FROM `Inpatient` WHERE `P_check` = 'Not check'")
        count_patientroom = cursor.fetchall()
        if p_check == 'Not check' :
            cursor.execute("SELECT `R_id`, `R_quantity` FROM Roomtype WHERE `R_id`='"+r_id+"'")
            count_roomtpye = cursor.fetchall()
            qty = count_roomtpye[0][1] - count_patientroom[0][1]
            cursor.execute("UPDATE `Roomtype` SET `R_quantity`= '"+str(qty)+"' WHERE `R_id`='"+r_id+"'")
            connection.commit()
        elif p_check == 'Check':
            pass
        elif p_check == 'Discharge':
            cursor.execute("SELECT `R_id`, `R_quantity` FROM Roomtype WHERE `R_id`='"+r_id+"'")
            count_roomtpye = cursor.fetchall()
            cursor.execute("SELECT `R_id`,COUNT(R_id),`P_check` FROM `Inpatient` WHERE `P_check` = 'Discharge'")
            count_discharge = cursor.fetchall()
            qty = count_roomtpye[0][1] + count_discharge[0][1]
            cursor.execute("UPDATE `Roomtype` SET `R_quantity`= '"+str(qty)+"' WHERE `R_id`='"+r_id+"'")
            connection.commit()
        cursor.close()
        return redirect(url_for('inpatient'))   

# Delete Functions
# Delete Patient
@app.route("/delete/<string:patient_id>", methods=['GET', 'POST'])
def delete(patient_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Patient` WHERE `Patient_id` = %s",(patient_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('registration'))

# Delete Doctor
@app.route("/delete/doctor/<string:doctor_id>", methods=['GET', 'POST'])
def deletedoctor(doctor_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Doctor` WHERE `Doctor_id` = %s",(doctor_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('doctor'))

# Delete Room
@app.route("/delete/room/<string:r_id>", methods=['GET', 'POST'])
def deleteroom(r_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Roomtype` WHERE `R_id` = %s",(r_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('room'))

# Delete Medicine
@app.route("/delete/medicine/<string:medicine_id>", methods=['GET', 'POST'])
def deletemedicine(medicine_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Medicine` WHERE `medicine_id` = %s",(medicine_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('medicine'))

# Delete Medical Record
@app.route("/delete/medicalrecord/<string:mrecord_id>", methods=['GET', 'POST'])
def deletemedicalrecord(mrecord_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Medical Record` WHERE `mrecord_id` = %s",(mrecord_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('medicalrecord'))

# Delete Outpatient
@app.route("/delete/outpatient/<string:patient_id>", methods=['GET', 'POST'])
def deleteoutpatient(patient_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Outpatient` WHERE `Patient_id` = %s",(patient_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('outpatient'))

# Delete Inpatient
@app.route("/delete/inpatient/<string:patient_id>", methods=['GET', 'POST'])
def deleteinpatient(patient_id):
    flash("Data Deleted Successfully")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM `Inpatient` WHERE `Patient_id` = %s",(patient_id,))
    connection.commit()
    cursor.close()
    return redirect(url_for('inpatient'))

if __name__== '__main__':
    app.secret_key = 'super secret key'
    app.secret_key = 'flash message'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
    