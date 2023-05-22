"""OBJECT RELATIONAL MAPPER (ORM) USING SQLALCHEMY"""

from .database import Base
from sqlalchemy import Float, ForeignKey, Text, func
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP, TIME
from sqlalchemy.types import Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import sessionmaker
from .database import engine, SessionLocal
import uuid
import bcrypt


""" ADMINISTRATORS """
class Administrator(Base):
    __tablename__ = "administrators"

    id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    hospital_id = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, address, city, state, zip_code, country, hospital_id):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.hospital_id})"


session = SessionLocal()
"""
administrator = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                              "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 1)
administrator1 = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 2)
administrator2 = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 3)
administrator3 = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 4)
administrator4 = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 5)
administrator5 = Administrator("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 6)


session.add(administrator)
session.add(administrator1)
session.add(administrator2)
session.add(administrator3)
session.add(administrator4)
session.add(administrator5)
"""
session.commit()
session.close()


""" ADMISSION """
class Admission(Base):
    __tablename__ = 'admissions'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    admission_date = Column(Date)
    admission_time = Column(TIME)
    discharge_date = Column(Date)
    discharge_time = Column(TIME)
    reason = Column(Text)
    diagnosis = Column(Text)
    treatment = Column(Text)
    doctor_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, admission_date, admission_time, discharge_date, discharge_time, reason, diagnosis, treatment, doctor_id):
        self.patient_id = patient_id
        self.admission_date = admission_date
        self.admission_time = admission_time
        self.discharge_date = discharge_date
        self.discharge_time = discharge_time
        self.reason = reason
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"({self.id}), {self.patient_id}, {self.admission_date}, {self.admission_time},  {self.discharge_date}, {self.discharge_time}, {self.reason}, {self.diagnosis}, {self.treatment}, {self.doctor_id})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
admission = Admission(1, "2023-09-12", "12:45", "2023-10-12",
                      "19:01", "Referral", "Medical pills", "Surgery", 1)
admission1 = Admission(2, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "Death", "Medical pills", "Surgery", 2)
admission2 = Admission(3, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "End of Treatment", "Medical pills", "Surgery", 3)
admission3 = Admission(4, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "Referral", "Medical pills", "Surgery", 4)
admission4 = Admission(5, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "Transfer", "Medical pills", "Surgery", 5)
admission5 = Admission(6, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "Transfer", "Medical pills", "Surgery", 6)
admission6 = Admission(7, "2023-09-12", "12:45", "2023-10-12",
                       "19:01", "Transfer", "Medical pills", "Surgery", 7)
session.add(admission)
session.add(admission1)
session.add(admission2)
session.add(admission3)
session.add(admission5)
session.add(admission4)
session.add(admission6)
"""
session.commit()
session.close()

""" ADVERSE REACTION """
class AdverseReaction(Base):
    __tablename__ = "adverse_reactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    reaction_date = Column(Date)
    reaction_time = Column(TIME(timezone=True))
    reaction_type = Column(String)  # Foreign Key
    reaction_details = Column(String)
    medication_name = Column(String)
    dosage = Column(String)
    severity = Column(String)
    treatment = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, reaction_date, reaction_time, reaction_type, reaction_details, medication_name, dosage, severity, treatment):
        self.patient_id = patient_id
        self.reaction_date = reaction_date
        self.reaction_time = reaction_time
        self.reaction_type = reaction_type
        self.reaction_details = reaction_details
        self.medication_name = medication_name
        self.dosage = dosage
        self.severity = severity
        self.treatment = treatment

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.reaction_date}, {self.reaction_time}, {self.reaction_type}, {self.reaction_details}, {self.medication_name}, {self.dosage}, {self.severity}, {self.treatment})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
adverse_reaction = AdverseReaction(1, "2023-09-12", "10:25", "allergic_reaction",
                                   "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
adverse_reaction1 = AdverseReaction(2, "2023-09-12", "10:25", "allergic_reaction",
                                    "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
adverse_reaction3 = AdverseReaction(4, "2023-09-12", "10:25", "allergic_reaction",
                                    "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
adverse_reaction2 = AdverseReaction(3, "2023-09-12", "10:25", "allergic_reaction",
                                    "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
adverse_reaction4 = AdverseReaction(5, "2023-09-12", "10:25", "allergic_reaction",
                                    "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
adverse_reaction5 = AdverseReaction(6, "2023-09-12", "10:25", "allergic_reaction",
                                    "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")

session.add(adverse_reaction)
session.add(adverse_reaction1)
session.add(adverse_reaction2)
session.add(adverse_reaction3)
session.add(adverse_reaction4)
session.add(adverse_reaction5)
"""
session.commit()
session.close()

"""ADVERSE REACTION TYPE """
class AdverseReactionType(Base):
    __tablename__ = "adverse_reaction_types"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"({self.id}), {self.name}, {self.description})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
adverse_reaction_type = AdverseReactionType(
    "Allergic reactions", "Any allergic reactions a patient may have experienced, including reactions to medications, food, or other allergens.")
adverse_reaction_type1 = AdverseReactionType(
    "Adverse drug reactions (ADR)", "Any negative reaction a patient may have experienced after taking a medication, including side effects and adverse drug interactions.")
adverse_reaction_type3 = AdverseReactionType(
    "Anaphylaxis", "A severe, potentially life-threatening allergic reaction that requires immediate medical attention.")
adverse_reaction_type2 = AdverseReactionType(
    "Toxicity", "If a patient has been exposed to toxic substances or overdose of medication, record the resulting adverse reaction.")
adverse_reaction_type4 = AdverseReactionType(
    "Delayed reactions", "Some reactions may occur after a delay of several hours, days or even weeks. It is important to note any such delayed reactions.")
adverse_reaction_type5 = AdverseReactionType(
    "Drug-drug interactions", "Any negative effects caused by two or more medications interacting with each other.")
adverse_reaction_type6 = AdverseReactionType(
    "Drug-food interactions", "Any negative effects caused by a medication interacting with food or beverages.")
adverse_reaction_type7 = AdverseReactionType(
    "Medical device malfunction", "Adverse reactions that result from the use of medical devices, such as implant failure or pacemaker malfunction.")
adverse_reaction_type8 = AdverseReactionType(
    "Infection", "Adverse reactions resulting from infections, such as sepsis or pneumonia.")
adverse_reaction_type9 = AdverseReactionType(
    "Other adverse reactions", "Any other negative reactions a patient may have experienced that are not listed above.")

session.add(adverse_reaction_type)
session.add(adverse_reaction_type1)
session.add(adverse_reaction_type2)
session.add(adverse_reaction_type3)
session.add(adverse_reaction_type4)
session.add(adverse_reaction_type5)
session.add(adverse_reaction_type6)
session.add(adverse_reaction_type7)
session.add(adverse_reaction_type8)
session.add(adverse_reaction_type9)
"""
session.commit()
session.close()

""" ALLERGIES """
class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"({self.id}, {self.name})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
allergy = Allergy("Milk")
allergy1 = Allergy("Egg")
allergy2 = Allergy("Peanut")
allergy3 = Allergy("Almond")
allergy4 = Allergy(
    "Tree nut(including almonds,cashews,walnuts,and hazelnuts)")
allergy5 = Allergy("Soy")
allergy6 = Allergy("Fish")
allergy7 = Allergy("Wheat")
allergy8 = Allergy("Shellfish(including crab,lobster,and shrimp)")
allergy9 = Allergy("Sesame")
allergy10 = Allergy("Mustard")
allergy11 = Allergy("Corn")
allergy12 = Allergy("Meat(including beef,pork, and lamb)")
allergy13 = Allergy("Fruit(including apples,bananas, and kiwi)")
allergy14 = Allergy("Vegetable(including tomatoes,carrots, and celery)")

session.add(allergy)
session.add(allergy1)
session.add(allergy2)
session.add(allergy3)
session.add(allergy4)
session.add(allergy5)
session.add(allergy6)
session.add(allergy7)
session.add(allergy8)
session.add(allergy9)
session.add(allergy10)
session.add(allergy11)
session.add(allergy12)
session.add(allergy13)
session.add(allergy14)
"""
session.commit()
session.close()


""" APPOINTMENT REMINDER """
# Fetch only
class AppointmentReminder(Base):
    __tablename__ = "appointment_reminders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    appointment_id = Column(Integer)  # Foreign
    # Foreign key to the users table(either patient or doctor)
    user_id = Column(Integer)
    reminder_date = Column(Date)
    reminder_time = Column(TIME)
    reminder_type = Column(String)  # email, sms, push notification
    status = Column(String)  # sent, pending
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, appointment_id, user_id, reminder_date, reminder_time, reminder_type, status):
        self.appointment_id = appointment_id
        self.user_id = user_id
        self.reminder_date = reminder_date
        self.reminder_time = reminder_time
        self.reminder_type = reminder_type
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.appointment_id}, {self.user_id}, {self.reminder_date}, {self.reminder_time}, {self.reminder_type}, {self.status})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
appointment_reminder = AppointmentReminder(
    2, 3, "2025-12-12", "12:45", "SMS", "Sent")
appointment_reminder1 = AppointmentReminder(
    2, 2, "2025-12-12", "12:45", "Email", "Pending")
appointment_reminder3 = AppointmentReminder(
    4, 4, "2025-12-12", "12:45", "Push notification", "Pending")
appointment_reminder2 = AppointmentReminder(
    3, 3, "2025-12-12", "12:45", "Email", "Sent")
appointment_reminder4 = AppointmentReminder(
    5, 5, "2025-12-12", "12:45", "Push notification", "Sent")


session.add(appointment_reminder)
session.add(appointment_reminder1)
session.add(appointment_reminder3)
session.add(appointment_reminder2)
session.add(appointment_reminder4)
"""
session.commit()
session.close()

""" APPOINTMENTS """
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    appointment_type = Column(String)  # In-person, Online
    appointment_date = Column(Date)
    appointment_start_time = Column(TIME)
    appointment_end_time = Column(TIME)
    description = Column(Text)  # check-up, follow-up, consultation
    status = Column(String)  # confirmed, cancelled, rescheduled
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, doctor_id, appointment_type, appointment_date, appointment_start_time, appointment_end_time, description, status):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_type = appointment_type
        self.appointment_date = appointment_date
        self.appointment_start_time = appointment_start_time
        self.appointment_end_time = appointment_end_time
        self.description = description
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.appointment_type}, {self.appointment_date}, {self.appointment_start_time}, {self.appointment_end_time}, {self.description}, {self.status})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
appointment = Appointment(1, 1, "check-up", "2025-09-12",
                          "03:00", "3:30", "Eye checkup", "Confirmed")
appointment1 = Appointment(
    2, 2, "check-up", "2025-09-12", "03:30", "4:30", "Eye checkup", "Cancelled")
appointment2 = Appointment(
    3, 3, "check-up", "2025-09-12", "03:00", "5:30", "Eye checkup", "Rescheduled")
appointment3 = Appointment(
    4, 4, "check-up", "2025-09-12", "06:00", "6:30", "Eye checkup", "Confirmed")
appointment4 = Appointment(
    5, 5, "check-up", "2025-09-12", "07:00", "7:30", "Eye checkup", "Cancelled")
appointment5 = Appointment(
    6, 6, "check-up", "2025-09-12", "08:00", "8:30", "Eye checkup", "Rescheduled")


session.add(appointment)
session.add(appointment1)
session.add(appointment3)
session.add(appointment2)
session.add(appointment4)
session.add(appointment5)
"""
session.commit()
session.close()


""" APPOINTMENT TYPE """
class AppointmentType(Base):
    __tablename__ = "appointment_types"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description):
        self.name = name
        self.description = description
        

    def __repr__(self):
        return f"({self.name}, {self.description})"


Session = sessionmaker(bind=engine)

session = SessionLocal()
"""
appointment_type = AppointmentType("In-person", "An appointment where the patient and doctor meet face-to-face in person.")
appointment_type1 = AppointmentType("Online", "An appointment that takes place over video call or chat, often using a telemedicine platform.")
appointment_type2 = AppointmentType("Phone", "An appointment that takes place over the phone.")
appointment_type3 = AppointmentType("Follow-up", "An appointment to follow up on a previous visit or treatment.")
appointment_type4 = AppointmentType("Routine check-up", "An appointment for a routine check-up, such as a yearly physical or dental exam.")
appointment_type5 = AppointmentType("Emergency", "An appointment for urgent or emergency care.")
appointment_type6 = AppointmentType("Specialty", "An appointment with a specialist, such as a cardiologist, neurologist, or dermatologist.")
appointment_type7 = AppointmentType("Diagnostic", "An appointment for diagnostic testing, such as an X-ray, MRI, or blood test.")
appointment_type8 = AppointmentType("Therapy", "An appointment for therapy, such as physical therapy, occupational therapy, or counseling.")



session.add(appointment_type)
session.add(appointment_type1)
session.add(appointment_type2)
session.add(appointment_type3)
session.add(appointment_type4)
session.add(appointment_type5)
session.add(appointment_type6)
session.add(appointment_type7)
session.add(appointment_type8)
"""
session.commit()
session.close()

"""  BED """
class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ward = Column(String)  # Foreign key
    bed_no = Column(Integer)
    bed_type = Column(String)  # ICU, general ward, private room
    availability = Column(Boolean)
    occupied_by = Column(String)  # Foreing key
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, ward, bed_no, bed_type, availability, occupied_by):
        self.ward = ward
        self.bed_no = bed_no
        self.bed_type = bed_type
        self.availability = availability
        self.occupied_by = occupied_by

    def __repr__(self):
        return f"({self.id}, {self.ward}, {self.bed_no}, {self.bed_type}, {self.availability}, {self.occupied_by})"


session = SessionLocal()
"""
bed = Bed("Orthopedic", 3, "ICU", True, 1)
bed2 = Bed("Eye Clinic", 1, "ICU", True, 3)
bed1 = Bed("Orthopedic", 1, "ICU", False, 2)
bed3 = Bed("Eye Clinic", 1, "ICU", False, 4)
bed4 = Bed("Eye Clinic", 1, "ICU", True, 5)
bed5 = Bed("Eye Clinic", 1, "ICU", False, 6)


session.add(bed)
session.add(bed1)
session.add(bed2)
session.add(bed3)
session.add(bed4)
session.add(bed5)
"""

session.commit()
session.close()

""" BED ASSIGNMENT """
class BedAssignment(Base):
    __tablename__ = "bed_assignments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bed_id = Column(Integer)
    patient_id = Column(Integer)
    assigned_by = Column(Integer)  # Foreign key to the users table
    assigned_at = Column(TIMESTAMP(timezone=True))
    discharged_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, bed_id, patient_id, assigned_by, assigned_at, discharged_at):
        self.bed_id = bed_id
        self.patient_id = patient_id
        self.assigned_by = assigned_by
        self.assigned_at = assigned_at
        self.discharged_at = discharged_at

    def __repr__(self):
        return f"({self.id}, {self.bed_id}, {self.patient_id}, {self.assigned_by}, {self.assigned_at}, {self.discharged_at})"


session = SessionLocal()
"""
bed_assignment = BedAssignment(
    1, 1, 1, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment1 = BedAssignment(
    2, 2, 2, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment2 = BedAssignment(
    3, 3, 3, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment3 = BedAssignment(
    4, 4, 4, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment4 = BedAssignment(
    5, 5, 5, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment5 = BedAssignment(
    6, 6, 6, "2023-05-12 12:45:00", "2023-06-12 12:45:00")

session.add(bed_assignment)
session.add(bed_assignment1)
session.add(bed_assignment2)
session.add(bed_assignment3)
session.add(bed_assignment4)
session.add(bed_assignment5)
"""
session.commit()
session.close()

""" BILLING """
class Billing(Base):
    __tablename__ = "billings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    bill_date = Column(DateTime)
    amount_due = Column(Float)
    amount_paid = Column(Float)
    payment_method = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __init__(self, patient_id, bill_date, amount_due, amount_paid, payment_method):
        self.patient_id = patient_id
        self.bill_date = bill_date
        self.amount_due = amount_due
        self.amount_paid = amount_paid
        self.payment_method = payment_method

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.bill_date}, {self.amount_due}, {self.amount_paid}, {self.payment_method})"


session = SessionLocal()
"""
bill = Billing(1, "2023-05-12", 2000, 800, "M-PESA")
bill2 = Billing(1, "2023-05-12", 3000, 800, "Card")
bill3 = Billing(1, "2023-05-12", 4000, 800, "Card")
bill4 = Billing(1, "2023-05-12", 5000, 800, "M-PESA")
bill5 = Billing(1, "2023-05-12", 6000, 800, "M-PESA")
bill6 = Billing(1, "2023-05-12", 7000, 800, "M-PESA")

session.add(bill)
session.add(bill2)
session.add(bill3)
session.add(bill4)
session.add(bill5)
session.add(bill6)
"""
session.commit()
session.close()

""" CHRONIC CONDITION """  # main
class ChronicCondition(Base):
    __tablename__ = "chronic_conditions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description):
        self.name = name
        self.description = description
   

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description})"


session = SessionLocal()
"""
chronic_condition = ChronicCondition(
    "Diabetes", "A condition where the body is unable to properly regulate blood sugar levels due to either inadequate insulin production or insulin resistance.")
chronic_condition1 = ChronicCondition(
    "Hypertension", "Also known as high blood pressure, hypertension occurs when the force of blood against the walls of the arteries is consistently too high, which can lead to various health problems over time.")
chronic_condition2 = ChronicCondition(
    "Asthma", "A chronic respiratory condition characterized by inflamed airways that can cause difficulty breathing, coughing, and wheezing.")
chronic_condition3 = ChronicCondition(
    "Chronic obstructive pulmonary disease (COPD)", "A group of lung diseases, including chronic bronchitis and emphysema, that can cause difficulty breathing and other respiratory problems.")
chronic_condition4 = ChronicCondition(
    "Arthritis", "A condition that affects the joints, causing pain, stiffness, and inflammation.")
chronic_condition5 = ChronicCondition(
    "Chronic kidney disease", "A condition where the kidneys are damaged and are no longer able to filter waste and excess fluid from the body as effectively as they should.")
chronic_condition6 = ChronicCondition(
    "Heart disease", "A group of conditions that affect the heart, including coronary artery disease, heart failure, and arrhythmias.")
chronic_condition7 = ChronicCondition(
    "Chronic pain", "A condition characterized by persistent pain that lasts for more than three months and can be caused by a variety of factors.")
chronic_condition8 = ChronicCondition(
    "Multiple sclerosis", "A chronic condition that affects the nervous system, causing a range of symptoms such as muscle weakness, numbness, and difficulty with coordination and balance.")
chronic_condition9 = ChronicCondition(
    "Fibromyalgia", "A chronic condition characterized by widespread pain, fatigue, and tenderness in the muscles, tendons, and other soft tissues.")
chronic_condition10 = ChronicCondition(
    "Chronic fatigue syndrome", "A condition characterized by persistent fatigue that is not improved by rest and is often accompanied by other symptoms such as muscle pain, headaches, and difficulty concentrating.")
chronic_condition11 = ChronicCondition(
    "Irritable bowel syndrome (IBS)", "A chronic condition that affects the digestive system, causing symptoms such as abdominal pain, bloating, and changes in bowel habits.")


session.add(chronic_condition)
session.add(chronic_condition1)
session.add(chronic_condition2)
session.add(chronic_condition3)
session.add(chronic_condition4)
session.add(chronic_condition5)
session.add(chronic_condition6)
session.add(chronic_condition7)
session.add(chronic_condition8)
session.add(chronic_condition9)
session.add(chronic_condition10)
session.add(chronic_condition11)

"""
session.commit()
session.close()

""" COUNTRY """  # main
class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    code = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.code})"


session = SessionLocal()
"""
country = Country("Kenya", "254")
country1 = Country("Uganda", "254")
country2 = Country("Tanzania", "254")
country3 = Country("Rwanda", "254")
country4 = Country("Burundi", "254")
country5 = Country("DRC", "254")


session.add(country)
session.add(country1)
session.add(country2)
session.add(country3)
session.add(country4)
session.add(country5)
"""
session.commit()
session.close()


""" DEPARTMENT """
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, )
    description = Column(Text)
    hospital = Column(String)
    head_doctor = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description, hospital, head_doctor):
        self.name = name
        self.description = description
        self.hospital = hospital
        self.head_doctor = head_doctor

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.hospital}, {self.head_doctor})"


session = SessionLocal()
"""
department = Department(
    "Emergency department", "This department is responsible for providing immediate medical care to patients with urgent and life-threatening conditions. Patients are typically seen on a first-come, first-served basis, with the most critical cases receiving priority.", 1, 1)
department1 = Department("Intensive care unit (ICU)", "This department provides advanced, round-the-clock care to critically ill patients who require close monitoring and specialized medical equipment. Patients in the ICU are often in need of life support and may be unconscious or in a coma.", 1, 1)
department2 = Department(
    "Surgery department", "This department is responsible for performing surgical procedures on patients who require them. Surgeons work closely with anesthesiologists, nurses, and other healthcare professionals to ensure that each procedure is safe and successful.", 1, 1)
department3 = Department("Obstetrics and gynecology (OB/GYN) department", "This department provides care for women during pregnancy, childbirth, and throughout their reproductive years. OB/GYNs also diagnose and treat conditions related to the female reproductive system.", 1, 1)
department4 = Department(
    "Cardiology department", "This department specializes in diagnosing and treating heart and cardiovascular conditions, such as heart attacks, arrhythmias, and congestive heart failure.", 1, 1)
department5 = Department("Oncology department", "This department provides care for patients with cancer, including diagnosis, treatment, and supportive care. Oncologists work closely with other healthcare professionals to provide comprehensive cancer care.", 1, 1)
department6= Department("Pediatrics department", "This department provides care for infants, children, and adolescents, including preventive care, diagnosis, and treatment of acute and chronic illnesses.", 1, 1)
department7 = Department("Neurology department", "This department specializes in diagnosing and treating conditions related to the nervous system, including stroke, Parkinson's disease, and multiple sclerosis.", 1, 1)
department8 = Department("Radiology department", "This department uses medical imaging technology, such as X-rays, CT scans, and MRIs, to diagnose and treat a variety of conditions.", 1, 1)
department9 = Department("Psychiatry department", "This department provides care for patients with mental health conditions, including diagnosis, medication management, and therapy.", 1, 1)
department10 = Department("Respiratory therapy department", "This department provides diagnostic and therapeutic services to patients with respiratory conditions, such as asthma, chronic obstructive pulmonary disease (COPD), and pneumonia.", 1, 1)
department11 = Department("Rehabilitation department", "This department helps patients recover from injuries, surgeries, and illnesses through physical therapy, occupational therapy, and speech therapy.", 1, 1)
department12 = Department("Anesthesiology department", "This department provides anesthesia and sedation services to patients undergoing surgery or other medical procedures. Anesthesiologists also monitor patients' vital signs during and after procedures to ensure their safety.", 1, 1)
department13 = Department("Infectious disease department", "This department specializes in the diagnosis, treatment, and prevention of infectious diseases, such as HIV/AIDS, tuberculosis, and hepatitis.", 1, 1)
department14 = Department("Endocrinology department", "This department specializes in the diagnosis and treatment of conditions related to the endocrine system, including diabetes, thyroid disorders, and pituitary gland disorders.", 1, 1)
department15 = Department("Hematology/oncology department", "This department provides care for patients with blood disorders and cancers of the blood, such as leukemia, lymphoma, and myeloma.", 1, 1)
department16 = Department("Dermatology department", "This department specializes in the diagnosis and treatment of skin conditions, such as acne, psoriasis, and skin cancer.", 1, 1)
department17 = Department("Gastroenterology department", "This department specializes in the diagnosis and treatment of conditions related to the digestive system, such as irritable bowel syndrome (IBS), inflammatory bowel disease (IBD), and gastroesophageal reflux disease (GERD).", 1, 1)
department18 = Department("Ophthalmology department", "This department specializes in the diagnosis and treatment of eye conditions, such as cataracts, glaucoma, and macular degeneration.", 1, 1)
department19 = Department("Ear, nose, and throat (ENT) department", "This department specializes in the diagnosis and treatment of conditions related to the ears, nose, and throat, such as ear infections, sinusitis, and tonsillitis.", 1, 1)



session.add(department)
session.add(department1)
session.add(department2)
session.add(department3)
session.add(department4)
session.add(department5)
session.add(department6)
session.add(department7)
session.add(department8)
session.add(department9)
session.add(department10)
session.add(department11)
session.add(department12)
session.add(department13)
session.add(department14)
session.add(department15)
session.add(department16)
session.add(department17)
session.add(department18)
session.add(department19)

"""
session.commit()
session.close()

""" DIAGNOSIS """
class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(String)
    disease = Column(String)
    diagnosis = Column(String)
    date = Column(Date)
    doctor_id = Column(String)
    notes = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __init__(self, patient_id, disease, diagnosis, date, doctor_id, notes):
        self.patient_id = patient_id
        self.disease = disease
        self.diagnosis = diagnosis
        self.date = date
        self.doctor_id = doctor_id
        self.notes = notes

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.disease}, {self.diagnosis}, {self.date}, {self.doctor_id}, {self.notes})"


session = SessionLocal()
"""
diagnosis = Diagnosis(1, "1", "1", "2023-12-12", "1", "Doing well")
diagnosis1 = Diagnosis(2, "2", "2", "2023-12-12", "2", "Doing well")
diagnosis2 = Diagnosis(3, "3", "3", "2023-12-12", "3", "Doing well")
diagnosis3 = Diagnosis(4, "4", "4", "2023-12-12", "4", "Doing well")
diagnosis4 = Diagnosis(5, "5", "5", "2023-12-12", "5", "Doing well")
diagnosis5 = Diagnosis(6, "6", "6", "2023-12-12", "6", "Doing well")


session.add(diagnosis)
session.add(diagnosis1)
session.add(diagnosis2)
session.add(diagnosis3)
session.add(diagnosis4)
session.add(diagnosis5)
"""
session.commit()
session.close()


""" DISEASES """
class Disease(Base):
    __tablename__ = 'diseases'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    symptoms = Column(Text)
    treatment = Column(Text)
    prevention = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description, symptoms, treatment, prevention):
        self.name = name
        self.description = description
        self.symptoms = symptoms
        self.treatment = treatment
        self.prevention = prevention

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.symptoms}, {self.treatment}, {self.prevention})"


session = SessionLocal()
"""
disease = Disease("Cholera", "Description", "Diarrhoea, Coughing",
                  "Injection", "Drinking clean water")
disease1 = Disease("HIV/AIDS", "Description",
                   "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease2 = Disease("Hepatitis B", "Description",
                   "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease3 = Disease("Malaria", "Description",
                   "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease4 = Disease("Typhoid", "Description",
                   "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease5 = Disease("Polio", "Description", "Diarrhoea, Coughing",
                   "Injection", "Drinking clean water")


session.add(disease)
session.add(disease1)
session.add(disease2)
session.add(disease3)
session.add(disease4)
session.add(disease5)
"""
session.commit()
session.close()

""" DOCTOR """
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(String, primary_key=True)

    #user_id = Column(String, ForeignKey('users.id'))
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    specialty = Column(String)
    licence_number = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    consultation_fee = Column(Float)
    rating = Column(Float)
    verified = Column(Boolean)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    #user = relationship("User", backref="doctor")

    def __init__(self, firstname, middlename, lastname, dob, gender, phone_number, email, specialty, licence_number, address, city, state, postal_code, country, consultation_fee, rating, verified):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.specialty = specialty
        self.licence_number = licence_number
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.consultation_fee = consultation_fee
        self.rating = rating
        self.verified = verified

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.middlename}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.specialty}, {self.licence_number}, {self.address}, {self.city}, {self.state}, {self.postal_code}, {self.country}, {self.consultation_fee}, {self.rating}, {self.verified})"


session = SessionLocal()
"""
doctor = Doctor("Susan", "Njeri", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "4500", "2", True)
doctor1 = Doctor("Michael", "Okumu", "Owino", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                 "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Uganda", "3500", "2",  True)
doctor2 = Doctor("Dennis", "Karuri", "Wambua", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                 "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Tanzania", "4000", "2",  True)
doctor3 = Doctor("Shirleen", "Oketch", "Okello", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                 "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Rwanda", "4000", "2",  True)
doctor4 = Doctor("Susan", "Nyambura", "Kihika", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                 "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Burundi", "5500", "2",   True)
doctor5 = Doctor("Sisa", "Ian", "Lumbugu", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                 "Neurosurgeon", "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "DRC", "2500", "2",  True)


session.add(doctor)
session.add(doctor1)
session.add(doctor2)
session.add(doctor3)
session.add(doctor4)
session.add(doctor5)
"""
session.commit()
session.close()

""" GENETIC CONDITION """
class GeneticCondition(Base):
    __tablename__ = "genetic_conditions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    patient_id = Column(Integer)
    inheritance_pattern = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description, patient_id, inheritance_pattern):
        self.name = name
        self.description = description
        self.patient_id = patient_id
        self.inheritance_pattern = inheritance_pattern

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.patient_id}, {self.inheritance_pattern})"


session = SessionLocal()
"""
genetic_condition = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition1 = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition2 = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition3 = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition4 = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition5 = GeneticCondition(
    "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")

session.add(genetic_condition)
session.add(genetic_condition1)
session.add(genetic_condition2)
session.add(genetic_condition3)
session.add(genetic_condition4)
session.add(genetic_condition5)
"""
session.commit()
session.close()


""" HOSPITAL """
class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(String, primary_key=True)
    #user_id = Column(String, ForeignKey('users.id'))
    name = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(10))
    country = Column(String)
    phone_number = Column(String(20))
    website = Column(String(255))
    rating = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    #user = relationship("User", backref="hospital")

    def __init__(self, name, address, city, state, zip_code, country, phone_number, website, rating):
        self.id = str(uuid.uuid4().hex[:4].upper())
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.phone_number = phone_number
        self.website = website
        self.rating = rating

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.phone_number}, {self.website}, {self.rating})"


session = SessionLocal()
"""
hospital = Hospital("Nairobi Hospital", "Upper Hill", "Nairobi", "Nairobi",
                    "00100", "Kenya", "725348900", "www.nairobihospital.com", 5.0)
hospital1 = Hospital("Karen Hospital", "Karen", "Nairobi", "Nairobi",
                     "00100", "Uganda", "725348900", "www.karenhospital.com", 5.0)
hospital2 = Hospital("Kenyatta Hospital", "Kenyatta", "Nairobi", "Nairobi",
                     "00100", "Tanzania", "725348900", "www.nairobihospital.com", 5.0)
hospital3 = Hospital("Eldoret Teaching and Referral Hospital", "Upper Hill", "Nairobi",
                     "Nairobi", "00100", "Rwanda", "725348900", "www.nairobihospital.com", 5.0)
hospital4 = Hospital("Pwani Hospital", "Pwani", "Pwani", "Nairobi",
                     "00100", "Burundi", "725348900", "www.nairobihospital.com", 5.0)
hospital5 = Hospital("Kakamega Teaching and Referral Hospital", "Upper Hill",
                     "Nairobi", "Nairobi", "00100", "DRC", "725348900", "www.nairobihospital.com", 5.0)


session.add(hospital)
session.add(hospital1)
session.add(hospital2)
session.add(hospital3)
session.add(hospital4)
session.add(hospital5)
"""
session.commit()
session.close()


""" IMMUNIZATION """
class Immunization(Base):
    __tablename__ = "immunizations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    vaccine_name = Column(String(50))
    dose_number = Column(Integer)
    date_given = Column(Date)
    administering_provider = Column(String)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # update_at

    def __init__(self, patient_id, vaccine_name, dose_number, date_given, administering_provider, expiration_date):
        self.patient_id = patient_id
        self.vaccine_name = vaccine_name
        self.dose_number = dose_number
        self.date_given = date_given
        self.administering_provider = administering_provider
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.vaccine_name}, {self.dose_number}, {self.date_given}, {self.administering_provider}, {self.expiration_date})"


session = SessionLocal()
"""
immunization = Immunization(1, "Pfizer vaccine", 2,
                            "2023-12-17", "Kikuyu Hospital", "2025-09-16")
immunization1 = Immunization(
    2, "Pfizer vaccine", 1, "2023-12-17", "Nairobi Hospital", "2025-09-16")
immunization2 = Immunization(3, "Pfizer vaccine", 2, "2023-12-17",
                             "Eldoret Teaching and Referral Hospital", "2025-09-16")
immunization3 = Immunization(
    4, "Pfizer vaccine", 1, "2023-12-17", "Pumwani Hospital", "2025-09-16")
immunization4 = Immunization(
    5, "Pfizer vaccine", 2, "2023-12-17", "Pwani Hospital", "2025-09-16")
immunization5 = Immunization(
    6, "Pfizer vaccine", 1, "2023-12-17", "Kikuyu Hospital", "2025-09-16")


session.add(immunization)
session.add(immunization1)
session.add(immunization2)
session.add(immunization3)
session.add(immunization4)
session.add(immunization5)
"""
session.commit()
session.close()


""" INSURANCE CLAIMS"""
class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"

    id = Column(String, primary_key=True)
    patient_id = Column(String)
    provider_id = Column(String)
    date_of_service = Column(Date)
    procedure_code = Column(String)
    diagnosis_code = Column(String)
    billed_amount = Column(Float)
    insurance_paid = Column(Float)
    patient_paid = Column(Float)
    status = Column(String)  # pending denied paids
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, provider_id, date_of_service, procedure_code, diagnosis_code, billed_amount, insurance_paid, patient_paid, status):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.date_of_service = date_of_service
        self.procedure_code = procedure_code
        self.diagnosis_code = diagnosis_code
        self.billed_amount = billed_amount
        self.insurance_paid = insurance_paid
        self.patient_paid = patient_paid
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.provider_id}, {self.date_of_service}, {self.procedure_code}, {self.diagnosis_code}, {self.billed_amount}, {self.insurance_paid}, {self.patient_paid}, {self.status})"


session = SessionLocal()
"""
insurance_claim = InsuranceClaim(
    "1", "1", "2023-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Paid")
insurance_claim1 = InsuranceClaim(
    "2", "2", "2024-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Denied")
insurance_claim2 = InsuranceClaim(
    "3", "3", "2025-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Pending")
insurance_claim3 = InsuranceClaim(
    "4", "4", "2026-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Paid")
insurance_claim4 = InsuranceClaim(
    "5", "5", "2027-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Pending")
insurance_claim5 = InsuranceClaim(
    "6", "6", "2028-12-17", "1", "1", 1300.00, 300.00, 1000.00, "Paid")


session.add(insurance_claim)
session.add(insurance_claim1)
session.add(insurance_claim2)
session.add(insurance_claim3)
session.add(insurance_claim4)
session.add(insurance_claim5)
"""
session.commit()
session.close()

""" INSURANCE PROVIDER """
class InsuranceProvider(Base):
    __tablename__ = "insurance_providers"

    id = Column(String, primary_key=True)
    #user_id = Column(String, ForeignKey('users.id'))
    name = Column(String(50))
    type = Column(String)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    postal_code = Column(String(10))
    country = Column(String)
    phone_number = Column(String(20))
    email = Column(String)
    website = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    #user = relationship("User", backref="insurance_provider")

    def __init__(self, name, type, address, city, state, postal_code, country, phone_number, email, website):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.name = name
        self.type = type
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone_number = phone_number
        self.email = email
        self.website = website

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.type}, {self.address}, {self.city}, {self.state}, {self.postal_code}, {self.country}, {self.phone_number}, {self.email}, {self.website})"


session = SessionLocal()
"""
insurance_provider = InsuranceProvider("AAR Insurance Kenya", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider1 = InsuranceProvider("APA Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider2 = InsuranceProvider("Britam Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider3 = InsuranceProvider("CIC Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider4 = InsuranceProvider("First Assurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider5 = InsuranceProvider("GA Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider6 = InsuranceProvider("Heritage Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")

insurance_provider7 = InsuranceProvider("Jubilee Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")

insurance_provider8 = InsuranceProvider("Madison Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")

insurance_provider9 = InsuranceProvider("Resolution Insurance", "Health Insurance",
                                       "P.O Box 980", "Nairobi", "Upper Hill", "00100", "Kenya", "780900900", "britam@gmail.com", "www.britam.co.ke")




session.add(insurance_provider)
session.add(insurance_provider1)
session.add(insurance_provider2)
session.add(insurance_provider3)
session.add(insurance_provider4)
session.add(insurance_provider5)
session.add(insurance_provider6)
session.add(insurance_provider7)
session.add(insurance_provider8)
session.add(insurance_provider9)
"""
session.commit()
session.close()


""" INSURANCE PROVIDER TYPES"""
class InsuranceProviderType(Base):
    __tablename__ = "insurance_provider_types"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description})"


session = SessionLocal()
"""
insurance_provider_type = InsuranceProviderType(
    "Health Maintenance Organizations (HMOs)", "HMOs provide healthcare coverage through a network of healthcare providers. Members pay a fixed monthly premium and usually have to choose a primary care physician (PCP) who coordinates their care and refers them to specialists within the network.")
insurance_provider_type1 = InsuranceProviderType(
    "Preferred Provider Organizations (PPOs)", "PPOs also have a network of healthcare providers, but members have more flexibility to see providers outside the network for a higher cost. Members typically pay a higher premium than HMOs.")
insurance_provider_type2 = InsuranceProviderType(
    "Point of Service (POS) Plans", "POS plans combine features of HMOs and PPOs, giving members the option to see providers both within and outside the network, but with different costs and restrictions.")
insurance_provider_type3 = InsuranceProviderType(
    "Exclusive Provider Organizations (EPOs)", "EPOs are similar to PPOs, but they do not cover out-of-network care except in emergency situations.")
insurance_provider_type4 = InsuranceProviderType(
    "Consumer-Driven Health Plans (CDHPs)", "CDHPs usually have high deductibles and are paired with a tax-advantaged savings account, such as a Health Savings Account (HSA) or a Health Reimbursement Arrangement (HRA).")
insurance_provider_type5 = InsuranceProviderType(
    "Self-Funded Plans", "Self-funded plans are employer-sponsored plans in which the employer assumes the risk and pays for employees’ healthcare costs directly, rather than purchasing insurance coverage from a traditional insurance company.")
insurance_provider_type6 = InsuranceProviderType(
    "Short-term Health Insurance", "Short-term health insurance provides coverage for a limited period, usually up to six months, and is designed to bridge the gap between long-term plans.")


session.add(insurance_provider_type)
session.add(insurance_provider_type1)
session.add(insurance_provider_type2)
session.add(insurance_provider_type3)
session.add(insurance_provider_type4)
session.add(insurance_provider_type5)
session.add(insurance_provider_type6)
"""

session.commit()
session.close()



""" IT STAFF """
class Itstaff(Base):
    __tablename__ = "it_staff"

    id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    hospital_id = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, address, city, state, zip_code, country, hospital_id):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.hospital_id})"


session = SessionLocal()
"""
ITStaff = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                  "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 1)
ITStaff1 = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                   "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 2)
ITStaff2 = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                   "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 3)
ITStaff3 = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                   "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 4)
ITStaff4 = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                   "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 5)
ITStaff5 = Itstaff("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                   "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 6)


session.add(ITStaff)
session.add(ITStaff1)
session.add(ITStaff2)
session.add(ITStaff3)
session.add(ITStaff4)
session.add(ITStaff5)
"""
session.commit()
session.close()


""" LAB TECHNICIANS """
class LabTechnician(Base):
    __tablename__ = "lab_technicians"

    id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    hospital_id = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, address, city, state, zip_code, country, hospital_id):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.hospital_id})"


session = SessionLocal()
"""
labtechnician = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                              "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 1)
labtechnician1 = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 2)
labtechnician2 = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 3)
labtechnician3 = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 4)
labtechnician4 = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 5)
labtechnician5 = LabTechnician("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                               "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 6)


session.add(labtechnician)
session.add(labtechnician1)
session.add(labtechnician2)
session.add(labtechnician3)
session.add(labtechnician4)
session.add(labtechnician5)
"""
session.commit()
session.close()


""" LAB TESTS """
class LabTest(Base):
    __tablename__ = "lab_tests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    test_name = Column(String)
    test_description = Column(String)
    test_type = Column(String)  # blood test urine test
    test_cost = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, test_name, test_description, test_type, test_cost):
        self.test_name = test_name
        self.test_description = test_description
        self.test_type = test_type
        self.test_cost = test_cost

    def __repr__(self):
        return f"({self.id}, {self.test_name}, {self.test_description}, {self.test_type}, {self.test_cost})"


session = SessionLocal()
"""
lab_test = LabTest("Blood test", "Haemoglobin blood test",
                   "Blood test", 900.00)
lab_test1 = LabTest("Urine test", "Urine test", "Urine test", 1900.00)
lab_test2 = LabTest("Blood test", "Haemoglobin blood test",
                    "Blood test", 2900.00)
lab_test3 = LabTest("Urine test", "Urine test", "Urine test", 3900.00)
lab_test4 = LabTest("Blood test", "Haemoglobin blood test",
                    "Blood test", 4900.00)
lab_test5 = LabTest("Urine test", "Urine test", "Urine test", 5900.00)


session.add(lab_test)
session.add(lab_test1)
session.add(lab_test2)
session.add(lab_test3)
session.add(lab_test4)
session.add(lab_test5)
"""
session.commit()
session.close()


""" LAB TEST RESULTS """
class LabTestResult(Base):
    __tablename__ = "lab_test_results"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    lab_test_name = Column(String)
    test_date = Column(Date)
    test_result = Column(String)
    units = Column(String)
    comments = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at

    def __init__(self, patient_id, lab_test_name, test_date, test_result, units, comments):
        self.patient_id = patient_id
        self.lab_test_name = lab_test_name
        self.test_date = test_date
        self.test_result = test_result
        self.units = units
        self.comments = comments

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.lab_test_name}, {self.test_date}, {self.test_result}, {self.units}, {self.comments})"


session = SessionLocal()
"""
test_result = LabTestResult(
    1, "test name", "2023-12-12", "Positive", "milligrams", "No comment")
test_result1 = LabTestResult(
    2, "test name", "2023-12-12", "Positive", "milligrams", "No comment")
test_result2 = LabTestResult(
    3, "test name", "2023-12-12", "Positive", "milligrams", "No comment")
test_result3 = LabTestResult(
    4, "test name", "2023-12-12", "Positive", "milligrams", "No comment")
test_result4 = LabTestResult(
    5, "test name", "2023-12-12", "Positive", "milligrams", "No comment")
test_result5 = LabTestResult(
    6, "test name", "2023-12-12", "Positive", "milligrams", "No comment")


session.add(test_result)
session.add(test_result1)
session.add(test_result2)
session.add(test_result3)
session.add(test_result4)
session.add(test_result5)
"""
session.commit()
session.close()

""" MEDICATION ALERTS """
class MedicationAlert(Base):
    __tablename__ = "medication_alerts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    medication_id = Column(Integer)
    dosage = Column(Text)
    frequency = Column(Text)
    alert_date = Column(Date)
    alert_text = Column(Text)
    status = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, medication_id, dosage, frequency, alert_date, alert_text, status):
        self.patient_id = patient_id
        self.medication_id = medication_id
        self.dosage = dosage
        self.frequency = frequency
        self.alert_date = alert_date
        self.alert_text = alert_text
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.medication_id}, {self.dosage}, {self.frequency}, {self.alert_date}, {self.alert_text}, {self.status})"


session = SessionLocal()
"""
medication_alert = MedicationAlert(
    1, 1, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert1 = MedicationAlert(
    2, 2, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Pending")
medication_alert2 = MedicationAlert(
    3, 3, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert3 = MedicationAlert(
    4, 4, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Failed")
medication_alert4 = MedicationAlert(
    5, 5, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert5 = MedicationAlert(
    6, 6, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")

session.add(medication_alert)
session.add(medication_alert1)
session.add(medication_alert2)
session.add(medication_alert3)
session.add(medication_alert4)
session.add(medication_alert5)
"""
session.commit()
session.close()

""" MEDICAL CONDITION """
class MedicalCondition(Base):
    __tablename__ = "medical_conditions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer, )
    name = Column(String(50))
    description = Column(Text)
    diagnosis_date = Column(Date)
    treatment = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, name, description, diagnosis_date, treatment):
        self.patient_id = patient_id
        self.name = name
        self.description = description
        self.diagnosis_date = diagnosis_date
        self.treatment = treatment

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.name}, {self.description}, {self.diagnosis_date}, {self.treatment})"


session = SessionLocal()
"""
medication_condition = MedicalCondition(
    1, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition1 = MedicalCondition(
    2, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition2 = MedicalCondition(
    3, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition3 = MedicalCondition(
    4, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition4 = MedicalCondition(
    5, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition5 = MedicalCondition(
    6, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")

session.add(medication_condition)
session.add(medication_condition1)
session.add(medication_condition2)
session.add(medication_condition3)
session.add(medication_condition4)
session.add(medication_condition5)
"""
session.commit()
session.close()

""" MEDICAL DEVICES """
class MedicalDevice(Base):
    __tablename__ = "medical_devices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String)
    hospital = Column(String)
    department = Column(String)
    last_maintenance = Column(Date)
    next_maintenance = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, manufacturer, model, serial_number, hospital, department, last_maintenance, next_maintenance):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.hospital = hospital
        self.department = department
        self.last_maintenance = last_maintenance
        self.next_maintenance = next_maintenance

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.manufacturer}, {self.model}, {self.serial_number}, {self.hospital}, {self.department}, {self.last_maintenance}, {self.next_maintenance})"


session = SessionLocal()
"""
medical_device = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "1", "1", "2021-07-16", "2022-07-16")
medical_device1 = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "2", "2", "2021-07-16", "2022-07-16")
medical_device2 = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "3", "3", "2021-07-16", "2022-07-16")
medical_device3 = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "4", "4", "2021-07-16", "2022-07-16")
medical_device4 = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "5", "5", "2021-07-16", "2022-07-16")
medical_device5 = MedicalDevice(
    "Printer", "HP", "HP-900GHES", "239-GTJD-249", "6", "6", "2021-07-16", "2022-07-16")

session.add(medical_device)
session.add(medical_device1)
session.add(medical_device2)
session.add(medical_device3)
session.add(medical_device4)
session.add(medical_device5)
"""
session.commit()
session.close()


""" MEDICAL IMAGES """
class MedicalImage(Base):
    __tablename__ = "medical_images"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    image_type = Column(String)
    image_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, doctor_id, image_type, image_date):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.image_type = image_type
        self.image_date = image_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.image_type}, {self.image_date})"


session = SessionLocal()
"""
medical_image = MedicalImage(1, 1, "X-Ray", "2024-04-14")
medical_image1 = MedicalImage(2, 2, "X-Ray", "2024-04-14")
medical_image2 = MedicalImage(3, 3, "X-Ray", "2024-04-14")
medical_image3 = MedicalImage(4, 4, "X-Ray", "2024-04-14")
medical_image4 = MedicalImage(5, 5, "X-Ray", "2024-04-14")
medical_image5 = MedicalImage(6, 6, "X-Ray", "2024-04-14")

session.add(medical_image)
session.add(medical_image1)
session.add(medical_image2)
session.add(medical_image3)
session.add(medical_image4)
session.add(medical_image5)
"""
session.commit()
session.close()


"""MEDICAL NOTES """
class MedicalNote(Base):
    __tablename__ = "medical_notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    date = Column(Date)
    content = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at

    def __init__(self, patient_id, doctor_id, date, content):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.content = content

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.date}, {self.content})"


session = SessionLocal()

medical_note = MedicalNote(1, 1, "2024-04-14", "Needs monitoring")
medical_note1 = MedicalNote(2, 2, "2024-04-14", "Needs monitoring")
medical_note2 = MedicalNote(3, 3, "2024-04-14", "Needs monitoring")
medical_note3 = MedicalNote(4, 4, "2024-04-14", "Needs monitoring")
medical_note4 = MedicalNote(5, 5, "2024-04-14", "Needs monitoring")
medical_note5 = MedicalNote(6, 6, "2024-04-14", "Needs monitoring")


session.add(medical_note)
session.add(medical_note1)
session.add(medical_note2)
session.add(medical_note3)
session.add(medical_note4)
session.add(medical_note5)

session.commit()
session.close()

""" MEDICAL PROCEDURES"""
class MedicalProcedure(Base):
    __tablename__ = "medical_procedures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    name = Column(String)
    date = Column(Date)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, doctor_id, name, date, notes):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.name = name
        self.date = date
        self.notes = notes

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.name}, {self.date}, {self.notes})"


session = SessionLocal()
"""
medical_procedure = MedicalProcedure(
    1, 1, "Colon surgery", "2017-08-01", "Successful")
medical_procedure1 = MedicalProcedure(
    2, 2, "Colon surgery", "2017-08-01", "Successful")
medical_procedure2 = MedicalProcedure(
    3, 3, "Colon surgery", "2017-08-01", "Successful")
medical_procedure3 = MedicalProcedure(
    4, 4, "Colon surgery", "2017-08-01", "Successful")
medical_procedure4 = MedicalProcedure(
    5, 5, "Colon surgery", "2017-08-01", "Successful")
medical_procedure5 = MedicalProcedure(
    6, 6, "Colon surgery", "2017-08-01", "Successful")

session.add(medical_procedure)
session.add(medical_procedure1)
session.add(medical_procedure2)
session.add(medical_procedure3)
session.add(medical_procedure4)
session.add(medical_procedure5)
"""
session.commit()
session.close()

""" MEDICATION """
class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    route_of_administration = Column(String)  # oral topical intravenous
    dosage = Column(String)
    unit = Column(String)
    frequency = Column(String)  # twice daily once weekly
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description, route_of_administration, dosage, unit, frequency, patient_id, doctor_id):
        self.name = name
        self.description = description
        self.route_of_administration = route_of_administration
        self.dosage = dosage
        self.unit = unit
        self.frequency = frequency
        self.patient_id = patient_id
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.route_of_administration}, {self.dosage}, {self.unit}, {self.frequency}, {self.patient_id}, {self.doctor_id})"


session = SessionLocal()
"""
medication = Medication("Malaria", "Caused by mosquitos",
                        "oral", "4", "milligram", "Twice daily", 1, 1)
medication1 = Medication("Malaria", "Caused by mosquitos",
                         "oral", "5", "milligram", "Twice daily", 2, 2)
medication2 = Medication("Malaria", "Caused by mosquitos",
                         "oral", "6", "milligram", "Twice daily", 3, 3)
medication3 = Medication("Malaria", "Caused by mosquitos",
                         "oral", "7", "milligram", "Twice daily", 4, 4)
medication4 = Medication("Malaria", "Caused by mosquitos",
                         "oral", "8", "milligram", "Twice daily", 5, 5)
medication5 = Medication("Malaria", "Caused by mosquitos",
                         "oral", "9", "milligram", "Twice daily", 6, 6)


session.add(medication)
session.add(medication1)
session.add(medication2)
session.add(medication3)
session.add(medication4)
session.add(medication5)
"""
session.commit()
session.close()


""" NURSE """
class Nurse(Base):
    __tablename__ = "nurses"

    id = Column(String, primary_key=True)
    #user_id = Column(String, ForeignKey('users.id'))
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    licence_number = Column(String)
    hospital_id = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)
    work_schedule = Column(String)
    verified = Column(Boolean)
    
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    #user = relationship("User", backref="nurse")

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, licence_number, hospital_id, address, city, state, postal_code, country, work_schedule, verified):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.licence_number = licence_number
        self.hospital_id = hospital_id
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.work_schedule = work_schedule
        self.verified = verified
       

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.licence_number}, {self.hospital_id}, {self.address}, {self.city}, {self.state}, {self.postal_code}, {self.country}, {self.work_schedule}, {self.verified})"


session = SessionLocal()
"""
nurse = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
              "134", 1, "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)
nurse1 = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
               "134", 2, "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)
nurse2 = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
               "134", 3,  "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)
nurse3 = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
               "134", 4, "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)
nurse4 = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
               "134", 5, "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)
nurse5 = Nurse("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
               "134", 6, "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", "Mon, Tue, Wed", True)


session.add(nurse)
session.add(nurse1)
session.add(nurse2)
session.add(nurse3)
session.add(nurse4)
session.add(nurse5)
"""
session.commit()
session.close()


""" PATIENT CONSENT"""
class PatientConsent(Base):
    __tablename__ = "patient_consents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    consent_type = Column(String)  # treatment release of medical information
    consent_date = Column(Date)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, consent_type, consent_date, expiration_date):
        self.patient_id = patient_id
        self.consent_type = consent_type
        self.consent_date = consent_date
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.consent_type}, {self.consent_date}, {self.expiration_date})"


session = SessionLocal()
"""
patient_consent = PatientConsent(1, "Treatment", "2015-08-15", "2019-09-18")
patient_consent1 = PatientConsent(2, "Treatment", "2015-08-15", "2019-09-18")
patient_consent2 = PatientConsent(3, "Treatment", "2015-08-15", "2019-09-18")
patient_consent3 = PatientConsent(4, "Treatment", "2015-08-15", "2019-09-18")
patient_consent4 = PatientConsent(5, "Treatment", "2015-08-15", "2019-09-18")
patient_consent5 = PatientConsent(6, "Treatment", "2015-08-15", "2019-09-18")

session.add(patient_consent)
session.add(patient_consent1)
session.add(patient_consent2)
session.add(patient_consent3)
session.add(patient_consent4)
session.add(patient_consent5)
"""
session.commit()
session.close()

""" PATIENT FEEDBACK """
class PatientFeedback(Base):
    __tablename__ = "patient_feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    date = Column(Date)
    text = Column(Text)
    rating = Column(Integer)

    def __init__(self, patient_id, doctor_id, date, text, rating):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.text = text
        self.rating = rating

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.date}, {self.text}, {self.rating})"


session = SessionLocal()
"""
patient_feedback = PatientFeedback(
    1, 1, "2015-08-15", "Good doctor. Highly recommend", 5)
patient_feedback1 = PatientFeedback(
    2, 2, "2015-08-15", "Good doctor. Highly recommend", 1)
patient_feedback2 = PatientFeedback(
    3, 3, "2015-08-15", "Good doctor. Highly recommend", 2)
patient_feedback3 = PatientFeedback(
    4, 4, "2015-08-15", "Good doctor. Highly recommend", 3)
patient_feedback4 = PatientFeedback(
    5, 5, "2015-08-15", "Good doctor. Highly recommend", 4)
patient_feedback5 = PatientFeedback(
    6, 6, "2015-08-15", "Good doctor. Highly recommend", 5)

session.add(patient_feedback)
session.add(patient_feedback1)
session.add(patient_feedback2)
session.add(patient_feedback3)
session.add(patient_feedback4)
session.add(patient_feedback5)
"""
session.commit()
session.close()

""" PATIENT VISIT """
class PatientVisit(Base):
    __tablename__ = "patient_visits"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    #user_id = Column(String, ForeignKey('users.id'))
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    appointment_id = Column(Integer)
    visit_date = Column(Date)
    chief_complaint = Column(Text)
    diagnosis_id = Column(Integer)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    #user = relationship("User", backref="patient")

    def __init__(self, patient_id, doctor_id, appointment_id, visit_date, chief_complaint, diagnosis_id, notes):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id
        self.visit_date = visit_date
        self.chief_complaint = chief_complaint
        self.diagnosis_id = diagnosis_id
        self.notes = notes

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.appointment_id}, {self.visit_date}, {self.chief_complaint}, {self.diagnosis_id}, {self.notes})"


session = SessionLocal()
"""
patient_visit = PatientVisit(
    1, 1, 1, "2015-08-15", "Fever and nausea", 1, "Patient doing okay")
patient_visit1 = PatientVisit(
    2, 2, 2, "2015-08-15", "Fever and nausea", 2, "Patient doing okay")
patient_visit2 = PatientVisit(
    3, 3, 3, "2015-08-15", "Fever and nausea", 3, "Patient doing okay")
patient_visit3 = PatientVisit(
    4, 4, 4, "2015-08-15", "Fever and nausea", 4, "Patient doing okay")
patient_visit4 = PatientVisit(
    5, 5, 5, "2015-08-15", "Fever and nausea", 5, "Patient doing okay")
patient_visit5 = PatientVisit(
    6, 6, 6, "2015-08-15", "Fever and nausea", 6, "Patient doing okay")

session.add(patient_visit)
session.add(patient_visit1)
session.add(patient_visit2)
session.add(patient_visit3)
session.add(patient_visit4)
session.add(patient_visit5)
"""
session.commit()
session.close()

""" PATIENT """
class Patient(Base):
    __tablename__ = "patients"

    id = Column(String, primary_key=True)
    #user_id = Column(String, ForeignKey('users.id'))
    # Personal Information
    firstname = Column(String)
    middlename = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phonenumber = Column(String(12))
    email = Column(String)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    postal_code = Column(String(10))
    country = Column(String)
    # Emergency Contact Information
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String(20))
    relationship = Column(String)
    # Insurance Information
    insurance = Column(Boolean)
    provider_name = Column(String)
    policy_number = Column(String)
    group_number = Column(String)
    effective_date = Column(Date)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    #user = relationship("User", backref="patient")

    def __init__(self, firstname, middlename, lastname, dob, gender, phonenumber, email, address, city, state, postal_code, country, emergency_contact_name, emergency_contact_phone, relationship, insurance, provider_name, policy_number, group_number, effective_date, expiration_date):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phonenumber = phonenumber
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.relationship = relationship
        self.insurance = insurance
        self.provider_name = provider_name
        self.policy_number = policy_number
        self.group_number = group_number
        self.effective_date = effective_date
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.middlename}, {self.lastname}, {self.dob}, {self.gender}, {self.phonenumber}, {self.email}, {self.address}, {self.city}, {self.state}, {self.postal_code}, {self.country}, {self.emergency_contact_name}, {self.emergency_contact_phone}, {self.relationship}, {self.insurance}, {self.provider_name}, {self.policy_number}, {self.group_number}, {self.effective_date}, {self.expiration_date})"


session = SessionLocal()
"""
patient = Patient("fortune", "amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                  "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", True, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
patient1 = Patient("fortune","amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                   "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", False, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
patient2 = Patient("fortune","amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                   "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", True, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
patient3 = Patient("fortune", "amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                   "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", False, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
patient4 = Patient("fortune", "amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                   "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", True, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
patient5 = Patient("fortune","amombo", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa",
                   "00100", "Kenya", "Dennis Okutoyi", "735400400", "son", False, "Britam Insurance", "28930", "34829", "2023-12-12", "2025-12-19")
session.add(patient)
session.add(patient1)
session.add(patient2)
session.add(patient3)
session.add(patient4)
session.add(patient5)
"""
session.commit()
session.close()

""" PHARMACIST """
class Pharmacist(Base):
    __tablename__ = "pharmacists"

    id = Column(String, primary_key=True)
    #user_id = Column(String, ForeignKey('users.id'))
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    licence_number = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    verified = Column(Boolean)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    #user = relationship("User", backref="pharmacist")

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, licence_number, address, city, state, zip_code, country, verified):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.licence_number = licence_number
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.verified = verified

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.licence_number}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.verified})"


session = SessionLocal()
"""
pharmacist = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                        "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)
pharmacist1 = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                         "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)
pharmacist2 = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                         "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)
pharmacist3 = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                         "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)
pharmacist4 = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                         "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)
pharmacist5 = Pharmacist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                         "134", "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", True)


session.add(pharmacist)
session.add(pharmacist1)
session.add(pharmacist2)
session.add(pharmacist3)
session.add(pharmacist4)
session.add(pharmacist5)
"""
session.commit()
session.close()


"""PRESCRIPTION """
class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctor_id = Column(Integer)
    patient_id = Column(Integer)
    medication = Column(String)
    dosage = Column(String)
    instructions = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    # updated_at

    def __init__(self, doctor_id, patient_id, medication, dosage, instructions):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions

    def __repr__(self):
        return f"({self.id}, {self.doctor_id}, {self.patient_id}, {self.medication}, {self.dosage}, {self.instructions})"


session = SessionLocal()

prescription = Prescription(1, 1, "malaria", "10", "Twice a day")
prescription1 = Prescription(2, 2, "malaria", "10", "Twice a day")
prescription2 = Prescription(3, 3, "malaria", "10", "Twice a day")
prescription3 = Prescription(4, 4, "malaria", "10", "Twice a day")
prescription4 = Prescription(5, 5, "malaria", "10", "Twice a day")
prescription5 = Prescription(6, 6, "malaria", "10", "Twice a day")

session.add(prescription)
session.add(prescription1)
session.add(prescription2)
session.add(prescription3)
session.add(prescription4)
session.add(prescription5)

session.commit()
session.close()

""" RECEPTIONISTS """
class Receptionist(Base):
    __tablename__ = "receptionists"

    id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    dob = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    hospital_id = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, firstname, lastname, dob, gender, phone_number, email, address, city, state, zip_code, country, hospital_id):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.dob},{self.gender}, {self.phone_number}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.hospital_id})"


session = SessionLocal()
"""
receptionist = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                            "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 1)
receptionist1 = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                             "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 2)
receptionist2 = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                             "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 3)
receptionist3 = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                             "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 4)
receptionist4 = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                             "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 5)
receptionist5 = Receptionist("Susan", "Koech", "2019-09-15", "female", "725490873", "susankoech@gmail.com",
                             "Dagoretti", "Nairobi", "Nairobi", "00100", "Kenya", 6)


session.add(receptionist)
session.add(receptionist1)
session.add(receptionist2)
session.add(receptionist3)
session.add(receptionist4)
session.add(receptionist5)
"""
session.commit()
session.close()


""" REFERRALS """
class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    referring_patient = Column(String)
    referred_patient = Column(String)
    referring_doctor = Column(String)
    referred_doctor = Column(String)
    referring_hospital = Column(String)
    referred_hospital = Column(String)
    referral_date = Column(Date)
    referral_reason = Column(Text)
    status = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, referring_patient, referred_patient, referring_doctor, referred_doctor, referring_hospital, referred_hospital, referral_date, referral_reason, status):
        self.referring_patient = referring_patient
        self.referred_patient = referred_patient
        self.referring_doctor = referring_doctor
        self.referred_doctor = referred_doctor
        self.referring_hospital = referring_hospital
        self.referred_hospital = referred_hospital
        self.referral_date = referral_date
        self.referral_reason = referral_reason
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.referring_patient}, {self.referred_patient}, {self.referring_doctor}, {self.referred_doctor}, {self.referring_hospital}, {self.referred_hospital}, {self.referral_date}, {self.referral_reason}, {self.status})"


session = SessionLocal()
"""
referral = Referral("1", "1", "1", "1", "1", "1", "2024-09-18", "Good services", "Done")
referral1 = Referral("2", "2", "2", "2", "2", "2", "2024-09-18",
                     "Good services", "Pending")
referral2 = Referral("3", "3", "3", "3", "3", "3", "2024-09-18",
                     "Good services", "Done")
referral3 = Referral("4", "4", "4", "4", "4", "4", "2024-09-18",
                     "Good services", "Pending")
referral4 = Referral("5", "5", "5", "5", "5", "5",  "2024-09-18",
                     "Good services", "Done")
referral5 = Referral("6", "6", "6", "6", "6", "6", "2024-09-18",
                     "Good services", "Done")


session.add(referral)
session.add(referral1)
session.add(referral2)
session.add(referral3)
session.add(referral4)
session.add(referral5)
"""
session.commit()
session.close()


""" SPECIALTY """
class Specialty(Base):
    __tablename__ = "specialties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description})"


session = SessionLocal()
"""
specialty = Specialty("Cardiologist", "A physician who specializes in diagnosing and treating diseases of the heart and blood vessels.")
specialty1 = Specialty("Neurologist", "A physician who specializes in diagnosing and treating diseases of the nervous system, including the brain, spinal cord, and nerves.")
specialty2 = Specialty("Gastroenterologist", "A physician who specializes in diagnosing and treating diseases of the digestive system.")
specialty3 = Specialty("Endocrinologist", "A physician who specializes in diagnosing and treating disorders of the endocrine system, which produces hormones.")
specialty4 = Specialty("Rheumatologist", "A physician who specializes in diagnosing and treating diseases of the joints, muscles, and bones.")
specialty5 = Specialty("Dermatologist", "A physician who specializes in diagnosing and treating diseases of the skin.")
specialty6 = Specialty("Ophthalmologist", "A physician who specializes in diagnosing and treating diseases of the eye.")
specialty7 = Specialty("Psychiatrist", "A physician who specializes in diagnosing and treating mental illness.")
specialty8 = Specialty("Obstetrician-gynecologist", "A physician who specializes in women's reproductive health, including pregnancy, childbirth, and disorders of the female reproductive system.")
specialty9 = Specialty("Pulmonologist", "A physician who specializes in diagnosing and treating diseases of the respiratory system, including the lungs.")
specialty10 = Specialty("Nephrologist", "A physician who specializes in diagnosing and treating diseases of the kidneys.")
specialty11 = Specialty("Immunologist", "A physician who specializes in diagnosing and treating disorders of the immune system.")
specialty12 = Specialty("Hematologist", "A physician who specializes in diagnosing and treating diseases of the blood and blood-forming tissues.")
specialty13 = Specialty("Urologist", "A physician who specializes in diagnosing and treating diseases of the urinary tract and male reproductive system.")
specialty14 = Specialty("Audiologist", "A healthcare professional who specializes in diagnosing and treating hearing and balance disorders.")
specialty15 = Specialty("Otolaryngologist", "A physician who specializes in diagnosing and treating disorders of the ear, nose, and throat.")
specialty16 = Specialty("Anesthesiologist", "A physician who specializes in administering anesthesia and monitoring patients during surgery.")
specialty17 = Specialty("Physical Therapist", "A healthcare professional who specializes in helping patients recover from injuries and disabilities through physical exercise and therapy.")
specialty18 = Specialty("Occupational Therapist", "A healthcare professional who specializes in helping patients regain the ability to perform daily activities, such as dressing and cooking, after an injury or disability.")
specialty19 = Specialty("Speech Therapist", "A healthcare professional who specializes in helping patients improve their communication skills, including speech and language, after an injury or disability.")
specialty20 = Specialty("Dentist", "A healthcare professional who specializes in diagnosing and treating diseases and conditions of the teeth and mouth.")
specialty21 = Specialty("Optometrist", "A healthcare professional who specializes in diagnosing and treating vision problems and prescribing corrective eyewear.")
specialty22 = Specialty("Podiatrist", "A healthcare professional who specializes in diagnosing and treating conditions of the foot and ankle.")
specialty23 = Specialty("Chiropractor", "A healthcare professional who specializes in diagnosing and treating disorders of the musculoskeletal system, particularly the spine.")
specialty24 = Specialty("Acupuncturist", "A healthcare professional who specializes in using acupuncture to treat a variety of conditions, including pain, stress, and fertility issues.")
specialty25 = Specialty("Naturopath", "A healthcare professional who specializes in using natural remedies and alternative therapies to promote healing and wellness.")
specialty26 = Specialty("Nutritionist", "A healthcare professional who specializes in providing advice and guidance on healthy eating and nutrition.")
specialty27 = Specialty("Psychologist", "A healthcare professional who specializes in diagnosing and treating mental and emotional disorders through therapy and counseling.")
specialty28 = Specialty("Social Worker", "A healthcare professional who specializes in helping individuals and families cope with social, emotional, and economic challenges.")
specialty29 = Specialty("Massage Therapist", "A healthcare professional who specializes in using touch and pressure to manipulate the muscles and soft tissues of the body to relieve pain and promote relaxation.")

session.add(specialty)
session.add(specialty1)
session.add(specialty2)
session.add(specialty3)
session.add(specialty4)
session.add(specialty5)
session.add(specialty6)
session.add(specialty7)
session.add(specialty8)
session.add(specialty9)
session.add(specialty10)
session.add(specialty11)
session.add(specialty12)
session.add(specialty13)
session.add(specialty14)
session.add(specialty15)
session.add(specialty16)
session.add(specialty17)
session.add(specialty18)
session.add(specialty19)
session.add(specialty20)
session.add(specialty21)
session.add(specialty22)
session.add(specialty23)
session.add(specialty24)
session.add(specialty25)
session.add(specialty26)
session.add(specialty27)
session.add(specialty28)
session.add(specialty29)
"""
session.commit()
session.close()

""" USERS """
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    role = Column(String) #patient, doctor, nurse, company
    registration_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, email, password, role):
        self.id = str(uuid.uuid4().hex[:6].upper())
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.role = role

    def __repr__(self):
        return f"({self.id}, {self.email}, {self.role})"


session = SessionLocal()
"""
user = User("example@example.com", "password123", "patient")
user1 = User("example@example.com", "shikyuku345", "doctor")
user2 = User( "example@example.com", "password123", "hospital")
user3 = User("example@example.com", "password123", "nurse")
user4 = User( "example@example.com", "password123", "pharmacy")
user5 = User( "example@example.com", "password123", "patient")

session.add(user)
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.add(user5)
"""
session.commit()
session.close()

""" VACCINATION """
class Vaccination(Base):
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer, )
    vaccine_name = Column(String)
    administered_by = Column(String)
    administered_at = Column(TIMESTAMP(timezone=True))
    next_dose_due = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, vaccine_name, administered_by, administered_at, next_dose_due):
        self.patient_id = patient_id
        self.vaccine_name = vaccine_name
        self.administered_by = administered_by
        self.administered_at = administered_at
        self.next_dose_due = next_dose_due


session = SessionLocal()
"""
vaccination = Vaccination(
    1, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination1 = Vaccination(
    2, "Moderna vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination2 = Vaccination(
    3, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination3 = Vaccination(4, "Astra Zeneca vaccine",
                           "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination4 = Vaccination(
    5, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination5 = Vaccination(
    6, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")

session.add(vaccination)
session.add(vaccination1)
session.add(vaccination2)
session.add(vaccination3)
session.add(vaccination4)
session.add(vaccination5)
"""
session.commit()
session.close()


""" VITAL SIGNS """
class VitalSign(Base):
    __tablename__ = "vital_signs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    heart_rate = Column(Float)
    blood_pressure_systolic = Column(Float)
    blood_pressure_diastolic = Column(Float)
    respiratory_rate = Column(Float)
    temperature = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    oxygen_saturation = Column(Float)
    recorded_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, patient_id, doctor_id, heart_rate, blood_pressure_systolic, blood_pressure_diastolic, respiratory_rate, temperature, height, weight, oxygen_saturation, recorded_at):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.heart_rate = heart_rate
        self.blood_pressure_systolic = blood_pressure_systolic
        self.blood_pressure_diastolic = blood_pressure_diastolic
        self.respiratory_rate = respiratory_rate
        self.temperature = temperature
        self.height = height
        self.weight = weight
        self.oxygen_saturation = oxygen_saturation
        self.recorded_at = recorded_at

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.heart_rate}, {self.blood_pressure_systolic}, {self.blood_pressure_diastolic}, {self.respiratory_rate}, {self.temperature}, {self.height}, {self.weight}, {self.oxygen_saturation}, {self.recorded_at})"


session = SessionLocal()
"""
vital_sign = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign1 = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign2 = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign3 = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign4 = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign5 = VitalSign(1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")


session.add(vital_sign)
session.add(vital_sign1)
session.add(vital_sign2)
session.add(vital_sign3)
session.add(vital_sign4)
session.add(vital_sign5)
"""
session.commit()
session.close()

""" WARD """
class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    capacity = Column(Integer)
    location = Column(String)
    hospital_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, name, type, capacity, location, hospital_id):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.location = location
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.type}, {self.capacity}, {self.location}, {self.hospital_id})"


session = SessionLocal()
"""
ward = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 1)
ward1 = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 2)
ward2 = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 3)
ward3 = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 4)
ward4 = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 5)
ward5 = Ward("Orthopedics", "Orthopedics", 240, "Left Wing", 6)

session.add(ward)
session.add(ward1)
session.add(ward2)
session.add(ward3)
session.add(ward4)
session.add(ward5)
"""
session.commit()
session.close()


""" WORK SCHEDULE """
class WorkSchedule(Base):
    __tablename__ = "work_schedules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctor = Column(String)
    nurse = Column(String)
    day_of_week = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, doctor, nurse, day_of_week, start_time, end_time):
        self.doctor = doctor
        self.nurse = nurse
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"({self.doctor}, {self.nurse}, {self.day_of_week}, {self.start_time}, {self.end_time})"


session = SessionLocal()
"""
work_schedule = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")
work_schedule1 = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")
work_schedule2 = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")
work_schedule3 = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")
work_schedule4 = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")
work_schedule5 = WorkSchedule("2567", "2234", "Monday, Tuesday, Wednesday", "2023-12-12 12:45:00", "2023-12-12 12:45:00")

session.add(work_schedule)
session.add(work_schedule1)
session.add(work_schedule2)
session.add(work_schedule3)
session.add(work_schedule4)
session.add(work_schedule5)
"""
session.commit()
session.close()


# results = session.query(Person).all()
# print(results)
# results = session.query(Person).filter(Person.gender == 'female')
# for r in results:
#   print(r)
