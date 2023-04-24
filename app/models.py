"""OBJECT RELATIONAL MAPPER (ORM) USING SQLALCHEMY"""

from .database import Base
from sqlalchemy import Float, ForeignKey, LargeBinary, Text, func
from sqlalchemy import Column, Integer, String, Date, DateTime, Table
from sqlalchemy.sql.sqltypes import TIMESTAMP, TIME
from sqlalchemy.types import Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import sessionmaker
from .database import engine, SessionLocal



""" ADMISSION """
class Admission(Base):
    __tablename__ = 'admissions'
    id = Column(Integer, primary_key=True)
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

    def __init__(self, id, patient_id, admission_date, admission_time, discharge_date, discharge_time, reason, diagnosis, treatment, doctor_id):
        self.id = id
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

#admission = Admission(1, 1, "2023-09-12", "12:45", "2023-10-12", "19:01", "Referral", "Medical pills", "Surgery", 1)
#admission1 = Admission(2, 2, "2023-09-12", "12:45", "2023-10-12", "19:01", "Death", "Medical pills", "Surgery", 2)
#admission2 = Admission(3, 3, "2023-09-12", "12:45", "2023-10-12", "19:01", "End of Treatment", "Medical pills", "Surgery", 3)
#admission3 = Admission(4, 4, "2023-09-12", "12:45", "2023-10-12", "19:01", "Referral", "Medical pills", "Surgery", 4)
#admission4 = Admission(5, 5, "2023-09-12", "12:45", "2023-10-12", "19:01", "Transfer", "Medical pills", "Surgery", 5)
#admission5 = Admission(6, 6, "2023-09-12", "12:45", "2023-10-12", "19:01", "Transfer", "Medical pills", "Surgery", 6)
#admission6 = Admission(7, 7, "2023-09-12", "12:45", "2023-10-12", "19:01", "Transfer", "Medical pills", "Surgery", 7)
#session.add(admission)
#session.add(admission1)
#session.add(admission2)
#session.add(admission3)
#session.add(admission5)
#session.add(admission4)
#session.add(admission6)
session.commit()

""" ADVERSE REACTION """
class AdverseReaction(Base):
    __tablename__ = "adverse_reactions"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    reaction_date = Column(Date)
    reaction_time = Column(TIME(timezone=True))
    reaction_type = Column(String) #Foreign Key
    reaction_details = Column(String)
    medication_name = Column(String)
    dosage = Column(String)
    severity = Column(String)
    treatment = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, reaction_date, reaction_time, reaction_type, reaction_details, medication_name, dosage, severity, treatment):
        self.id = id
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

#adverse_reaction = AdverseReaction(1, 1, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
#adverse_reaction1 = AdverseReaction(2, 2, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
#adverse_reaction3 = AdverseReaction(4, 4, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
#adverse_reaction2 = AdverseReaction(3, 3, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
#adverse_reaction4 = AdverseReaction(5, 5, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")
#adverse_reaction5 = AdverseReaction(6, 6, "2023-09-12", "10:25", "allergic_reaction", "Milk allergy", "Medicall pills", "4 times a day", "Very Severe", "Regular pills")

#session.add(adverse_reaction)
#session.add(adverse_reaction1)
#session.add(adverse_reaction2)
#session.add(adverse_reaction3)
#session.add(adverse_reaction4)
#session.add(adverse_reaction5)
session.commit()

"""ADVERSE REACTION TYPE """
class AdverseReactionType(Base):
    __tablename__ = "adverse_reaction_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f"({self.id}), {self.name}, {self.description})"
    
Session = sessionmaker(bind=engine)

session = SessionLocal()

#adverse_reaction_type = AdverseReactionType(1, "Allergic reactions", "Any allergic reactions a patient may have experienced, including reactions to medications, food, or other allergens.")
#adverse_reaction_type1 = AdverseReactionType(2, "Adverse drug reactions (ADR)", "Any negative reaction a patient may have experienced after taking a medication, including side effects and adverse drug interactions.")
#adverse_reaction_type3 = AdverseReactionType(4, "Anaphylaxis", "A severe, potentially life-threatening allergic reaction that requires immediate medical attention.")
#adverse_reaction_type2 = AdverseReactionType(3, "Toxicity", "If a patient has been exposed to toxic substances or overdose of medication, record the resulting adverse reaction.")
#adverse_reaction_type4 = AdverseReactionType(5, "Delayed reactions", "Some reactions may occur after a delay of several hours, days or even weeks. It is important to note any such delayed reactions.")
#adverse_reaction_type5 = AdverseReactionType(6, "Drug-drug interactions", "Any negative effects caused by two or more medications interacting with each other.")
#adverse_reaction_type6 = AdverseReactionType(7, "Drug-food interactions", "Any negative effects caused by a medication interacting with food or beverages.")
#adverse_reaction_type7 = AdverseReactionType(8, "Medical device malfunction", "Adverse reactions that result from the use of medical devices, such as implant failure or pacemaker malfunction.")
#adverse_reaction_type8 = AdverseReactionType(9, "Infection", "Adverse reactions resulting from infections, such as sepsis or pneumonia.")
#adverse_reaction_type9 = AdverseReactionType(10, "Other adverse reactions", "Any other negative reactions a patient may have experienced that are not listed above.")

#session.add(adverse_reaction_type)
#session.add(adverse_reaction_type1)
#session.add(adverse_reaction_type2)
#session.add(adverse_reaction_type3)
#session.add(adverse_reaction_type4)
#session.add(adverse_reaction_type5)
#session.add(adverse_reaction_type6)
#session.add(adverse_reaction_type7)
#session.add(adverse_reaction_type8)
#session.add(adverse_reaction_type9)
session.commit()

""" ALLERGIES """
class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"({self.id}, {self.name})"
    
Session = sessionmaker(bind=engine)

session = SessionLocal()

#allergy = Allergy(1, "Milk")
#allergy1 = Allergy(2, "Egg")
#allergy2 = Allergy(3, "Peanut")
#allergy3 = Allergy(4, "Almond")
#allergy4 = Allergy(5, "Tree nut(including almonds,cashews,walnuts,and hazelnuts)")
#allergy5 = Allergy(6, "Soy")
#allergy6 = Allergy(7, "Fish")
#allergy7 = Allergy(8, "Wheat")
#allergy8 = Allergy(9, "Shellfish(including crab,lobster,and shrimp)")
#allergy9 = Allergy(10, "Sesame")
#allergy10 = Allergy(11, "Mustard")
#allergy11 = Allergy(12, "Corn")
#allergy12 = Allergy(13, "Meat(including beef,pork, and lamb)")
#allergy13= Allergy(14, "Fruit(including apples,bananas, and kiwi)")
#allergy14 = Allergy(15, "Vegetable(including tomatoes,carrots, and celery)")

#session.add(allergy)
#session.add(allergy1)
#session.add(allergy2)
#session.add(allergy3)
#session.add(allergy4)
#session.add(allergy5)
#session.add(allergy6)
#session.add(allergy7)
#session.add(allergy8)
#session.add(allergy9)
#session.add(allergy10)
#session.add(allergy11)
#session.add(allergy12)
#session.add(allergy13)
#session.add(allergy14)
#session.commit()


""" APPOINTMENT REMINDER """
class AppointmentReminder(Base):
    __tablename__ = "appointment_reminders"

    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer)#Foreign
    user_id = Column(Integer) #Foreign key to the users table(either patient or doctor)
    reminder_date = Column(Date)
    reminder_time = Column(TIME)
    reminder_type = Column(String)#email, sms, push notification
    status = Column(String) #sent, pending
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    def __init__(self, id, appointment_id, user_id, reminder_date, reminder_time, reminder_type, status):
        self.id = id
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

#appointment_reminder = AppointmentReminder(1, 2, 3, "2025-12-12", "12:45", "SMS", "Sent")
#appointment_reminder1 = AppointmentReminder(2, 2, 2, "2025-12-12", "12:45", "Email", "Pending")
#appointment_reminder3 = AppointmentReminder(4, 4, 4, "2025-12-12", "12:45", "Push notification", "Pending")
#appointment_reminder2 = AppointmentReminder(3, 3, 3, "2025-12-12", "12:45", "Email", "Sent")
#appointment_reminder4 = AppointmentReminder(5, 5, 5, "2025-12-12", "12:45", "Push notification", "Sent")


#session.add(appointment_reminder)
#session.add(appointment_reminder1)
#session.add(appointment_reminder3)
#session.add(appointment_reminder2)
#session.add(appointment_reminder4)

session.commit()

""" APPOINTMENTS """ 
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    appointment_type = Column(String)#check-up, follow-up, consultation
    appointment_date = Column(Date)
    appointment_start_time = Column(TIME)
    appointment_end_time = Column(TIME)
    description = Column(Text)
    status = Column(String) #confirmed, cancelled, rescheduled
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, patient_id, doctor_id, appointment_type, appointment_date, appointment_start_time, appointment_end_time, description, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_type = appointment_type
        self.appointment_date = appointment_date
        self.appointment_start_time = appointment_start_time
        self.appointment_end_time =appointment_end_time
        self.description = description
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.appointment_type}, {self.appointment_date}, {self.appointment_start_time}, {self.appointment_end_time}, {self.description}, {self.status})"
    
Session = sessionmaker(bind=engine)

session = SessionLocal()

#appointment = Appointment(1, 1, 1, "check-up", "2025-09-12", "03:00", "3:30", "Eye checkup", "Confirmed")
#appointment1 = Appointment(2, 2, 2, "check-up", "2025-09-12", "03:30", "4:30", "Eye checkup", "Cancelled")
#appointment2 = Appointment(3, 3, 3, "check-up", "2025-09-12", "03:00", "5:30", "Eye checkup", "Rescheduled")
#appointment3 = Appointment(4, 4, 4, "check-up", "2025-09-12", "06:00", "6:30", "Eye checkup", "Confirmed")
#appointment4 = Appointment(5, 5, 5, "check-up", "2025-09-12", "07:00", "7:30", "Eye checkup", "Cancelled")
#appointment5 = Appointment(6, 6, 6, "check-up", "2025-09-12", "08:00", "8:30", "Eye checkup", "Rescheduled")


#session.add(appointment)
#session.add(appointment1)
#session.add(appointment3)
#session.add(appointment2)
#session.add(appointment4)
#session.add(appointment5)

session.commit()

"""  BED """
class Bed(Base):
    __tablename__ = "beds"

    id = Column(Integer, primary_key=True )
    ward_id = Column(Integer)#Foreign key
    bed_no = Column(Integer)
    bed_type = Column(String)#ICU, general ward, private room
    availability = Column(Boolean)
    occupied_by = Column(Integer) #Foreing key
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, ward_id, bed_no, bed_type, availability, occupied_by):
        self.id = id
        self.ward_id = ward_id
        self.bed_no = bed_no
        self.bed_type = bed_type
        self.availability = availability
        self.occupied_by = occupied_by

    def __repr__(self):
        return f"({self.id}, {self.ward_id}, {self.bed_no}, {self.bed_type}, {self.availability}, {self.occupied_by})"


session = SessionLocal()

#bed = Bed(1, 2, 3, "ICU", True, 1)
#bed2 = Bed(3, 1, 1, "ICU", True, 3)
#bed1 = Bed(2, 1, 1, "ICU", False, 2)
#bed3 = Bed(4, 1, 1, "ICU", False, 4)
#bed4 = Bed(5, 1, 1, "ICU", True, 5)
#bed5 = Bed(6, 1, 1, "ICU", False, 6)


#session.add(bed)
#session.add(bed1)
#session.add(bed2)
#session.add(bed3)
#session.add(bed4)
#session.add(bed5)
session.commit()

""" BED ASSIGNMENT """
class BedAssignment(Base):
    __tablename__ = "bed_assignments"

    id = Column(Integer, primary_key=True)
    bed_id = Column(Integer) 
    patient_id = Column(Integer)
    assigned_by = Column(Integer)#Foreign key to the users table
    assigned_at = Column(TIMESTAMP(timezone=True))
    discharged_at = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, bed_id, patient_id, assigned_by, assigned_at, discharged_at):
        self.id = id
        self.bed_id = bed_id
        self.patient_id = patient_id
        self.assigned_by = assigned_by
        self.assigned_at = assigned_at
        self.discharged_at = discharged_at

    def __repr__(self):
        return f"({self.id}, {self.bed_id}, {self.patient_id}, {self.assigned_by}, {self.assigned_at}, {self.discharged_at})"
    
session = SessionLocal()
"""
bed_assignment = BedAssignment(1, 1, 1, 1, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment1 = BedAssignment(2, 2, 2, 2, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment2 = BedAssignment(3, 3, 3, 3, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment3 = BedAssignment(4, 4, 4, 4, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment4 = BedAssignment(5, 5, 5, 5, "2023-05-12 12:45:00", "2023-06-12 12:45:00")
bed_assignment5 = BedAssignment(6, 6, 6, 6, "2023-05-12 12:45:00", "2023-06-12 12:45:00")



session.add(bed_assignment)
session.add(bed_assignment1)
session.add(bed_assignment2)
session.add(bed_assignment3)
session.add(bed_assignment4)
session.add(bed_assignment5)
"""
session.commit()

""" BILLING """
class Billing(Base):
    __tablename__ = "billings"

    id = Column(Integer, primary_key=True, )
    patient_id = Column(Integer)
    bill_date = Column(DateTime)
    amount_due = Column(Float)
    amount_paid = Column(Float)
    payment_method = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())


    def __init__(self, id, patient_id, bill_date, amount_due, amount_paid, payment_method):
        self.id = id
        self.patient_id = patient_id
        self.bill_date = bill_date
        self.amount_due = amount_due
        self.amount_paid = amount_paid
        self.payment_method = payment_method

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.bill_date}, {self.amount_due}, {self.amount_paid}, {self.payment_method})"
    
session = SessionLocal()
"""
bill = Billing(1, 1, "2023-05-12", 2000, 800, "M-PESA")
bill2 = Billing(2, 1, "2023-05-12", 3000, 800, "Card")
bill3 = Billing(3, 1, "2023-05-12", 4000, 800, "Card")
bill4 = Billing(4, 1, "2023-05-12", 5000, 800, "M-PESA")
bill5 = Billing(5, 1, "2023-05-12", 6000, 800, "M-PESA")
bill6 = Billing(6, 1, "2023-05-12", 7000, 800, "M-PESA")

session.add(bill)
session.add(bill2)
session.add(bill3)
session.add(bill4)
session.add(bill5)
session.add(bill6)
"""
session.commit()

""" CARE TEAM """
class CareTeam(Base):
    __tablename__ = "care_team"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)
    contact_number = Column(Integer)
    email = Column(String)
    patient_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())


    def __init__(self, id, first_name, last_name, role, contact_number, email, patient_id, start_date, end_date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.contact_number = contact_number
        self.email =email
        self.patient_id = patient_id
        self.start_date = start_date
        self.end_date = end_date


    def __repr__(self):
        return f"({self.id}, {self.first_name}, {self.last_name}, {self.role}, {self.contact_number}, {self.email}, {self.patient_id}, {self.start_date}, {self.end_date})"

session = SessionLocal()
"""
care_team = CareTeam(1, "Jennifer", "Ogunto", "Nurse", "726400500", "jogunto@gmail.com", 1, "2023-09-09", "2023-09-24")
care_team1 = CareTeam(2, "Samson", "Onyango", "Doctor", "726400500", "jogunto@gmail.com", 2, "2023-09-12", "2023-09-21")
care_team2 = CareTeam(3, "Anna", "Oketch", "Nurse", "726400500", "jogunto@gmail.com", 3, "2023-09-12", "2023-09-21")
care_team3 = CareTeam(4, "Salma", "Nyokabi", "Nurse", "726400500", "jogunto@gmail.com", 4, "2023-09-12", "2023-09-21")
care_team4 = CareTeam(5, "Ruth", "Kimani", "Nurse", "726400500", "jogunto@gmail.com", 5, "2023-09-12", "2023-09-21")
care_team5 = CareTeam(6, "Job", "Mukhwana", "Nurse", "726400500", "jogunto@gmail.com", 6, "2023-09-12", "2023-09-21")

session.add(care_team)
session.add(care_team1)
session.add(care_team2)
session.add(care_team3)
session.add(care_team4)
session.add(care_team5)
"""
session.commit()

""" CHRONIC CONDITION """ #main 
class ChronicCondition(Base):
    __tablename__ = "chronic_conditions"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    condition = Column(String)
    diagnosis_date = Column(Date)
    severity = Column(String)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, condition, diagnosis_date, severity, notes):
        self.id = id
        self.patient_id = patient_id
        self.condition = condition
        self.diagnosis_date = diagnosis_date
        self.severity = severity
        self.notes = notes
    
    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.condition}, {self.diagnosis_date}, {self.severity}, {self.notes})"
    
session = SessionLocal()
"""
chronic_condition = ChronicCondition(1, 1, "Diabetes", "2021-09-19", "Severe", "Okay")
chronic_condition1 = ChronicCondition(2, 2, "Asthma", "2023-09-09", "Not Severe", "Doing well")
chronic_condition2 = ChronicCondition(3, 3, "Athritis", "2023-09-09", "Not Severe", "Doing well")
chronic_condition3 = ChronicCondition(4, 4, "Cancer", "2023-09-09", "Not Severe", "Doing well")
chronic_condition4 = ChronicCondition(5, 5, "HIV/AIDS", "2023-09-09", "Not Severe", "Doing well")
chronic_condition5 = ChronicCondition(6, 6, "Parkinson's disease", "2023-09-09", "Not Severe", "Doing well")

session.add(chronic_condition)
session.add(chronic_condition1)
session.add(chronic_condition2)
session.add(chronic_condition3)
session.add(chronic_condition4)
session.add(chronic_condition5)
"""
session.commit()

""" COUNTRY """ # main
class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
     

    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.code})"
    
session = SessionLocal()
"""
country = Country(1, "Kenya", "254")
country1 = Country(2, "Uganda", "254")
country2 = Country(3, "Tanzania", "254")
country3 = Country(4, "Rwanda", "254")
country4 = Country(5, "Burundi", "254")
country5 = Country(6, "DRC", "254")


session.add(country)
session.add(country1)
session.add(country2)
session.add(country3)
session.add(country4)
session.add(country5)
"""
session.commit()


""" DEPARTMENT """
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String, )
    description = Column(Text)
    head_doctor_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __init__(self, id, name, description, head_doctor_id):
        self.id = id
        self.name = name
        self.description = description
        self.head_doctor_id = head_doctor_id

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.head_doctor_id})"
    
session = SessionLocal()
"""
department = Department(1, "Reception", "In charge of welcoming patients in the hospital", 1)
department1 = Department(2, "Theatre", "In charge of surgery", 1)
department2 = Department(3, "Reception", "In charge of welcoming patients in the hospital", 1)
department3 = Department(4, "Theatre", "In charge of surgery", 1)
department4 = Department(5, "Reception", "In charge of welcoming patients in the hospital", 1)
department5 = Department(6, "Theatre", "In charge of surgery", 1)


session.add(department)
session.add(department1)
session.add(department2)
session.add(department3)
session.add(department4)
session.add(department5)
"""
session.commit()

""" DIAGNOSIS """
class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    disease_id = Column(Integer)
    diagnosis = Column(Integer)
    date = Column(Date)
    doctor_id = Column(Integer)
    notes = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())


    def __init__(self, id, patient_id, disease_id, diagnosis, date, doctor_id, notes):
        self.id = id
        self.patient_id = patient_id
        self.disease_id = disease_id
        self.diagnosis = diagnosis
        self.date = date
        self.doctor_id = doctor_id
        self.notes = notes

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.disease_id}, {self.diagnosis}, {self.date}, {self.doctor_id}, {self.notes})"
    
session = SessionLocal()
"""
diagnosis = Diagnosis(1, 1, 1, 1, "2023-12-12", 1, "Doing well")
diagnosis1 = Diagnosis(2, 2, 2, 2, "2023-12-12", 2, "Doing well")
diagnosis2 = Diagnosis(3, 3, 3, 3, "2023-12-12", 3, "Doing well")
diagnosis3 = Diagnosis(4, 4, 4, 4, "2023-12-12", 4, "Doing well")
diagnosis4 = Diagnosis(5, 5, 5, 5, "2023-12-12", 5, "Doing well")
diagnosis5 = Diagnosis(6, 6, 6, 6, "2023-12-12", 6, "Doing well")



session.add(diagnosis)
session.add(diagnosis1)
session.add(diagnosis2)
session.add(diagnosis3)
session.add(diagnosis4)
session.add(diagnosis5)
"""
session.commit()


""" DISEASES """
class Disease(Base):
    __tablename__ = 'diseases'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    symptoms = Column(Text)
    treatment = Column(Text)
    prevention = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, name, description, symptoms, treatment, prevention):
        self.id = id
        self.name = name
        self.description = description
        self.symptoms = symptoms
        self.treatment = treatment
        self.prevention = prevention

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.symptoms}, {self.treatment}, {self.prevention})"
    
session = SessionLocal()
"""
disease = Disease(1, "Cholera", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease1 = Disease(2, "HIV/AIDS", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease2 = Disease(3, "Hepatitis B", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease3 = Disease(4, "Malaria", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease4 = Disease(5, "Typhoid", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")
disease5 = Disease(6, "Polio", "Description", "Diarrhoea, Coughing", "Injection", "Drinking clean water")


session.add(disease)
session.add(disease1)
session.add(disease2)
session.add(disease3)
session.add(disease4)
session.add(disease5)
"""
session.commit()

""" DOCTOR """
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    specialty = Column(String)
    verified = Column(Boolean)
    work_schedule = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, firstname, lastname, email, phone_number, specialty, verified, work_schedule):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone_number = phone_number
        self.specialty = specialty
        self.verified = verified
        self.work_schedule = work_schedule

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.email}, {self.phone_number}, {self.specialty}, {self.verified}, {self.work_schedule})"

session = SessionLocal()
"""
doctor = Doctor(1, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")
doctor1 = Doctor(2, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")
doctor2 = Doctor(3, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")
doctor3 = Doctor(4, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")
doctor4 = Doctor(5, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")
doctor5 = Doctor(6, "Susan", "Koech", "susankoech@gmail.com", "725490873", "Neurosurgeon", True, "Mon, Tue, Wed")



session.add(doctor)
session.add(doctor1)
session.add(doctor2)
session.add(doctor3)
session.add(doctor4)
session.add(doctor5)
"""
session.commit()

"""DOCTOR SCHEDULES """ #- here
class DoctorSchedule(Base):
    __tablename__ = "doctor_schedules"
    
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    date = Column(Date)
    start_time = Column(TIME)
    end_time = Column(TIME)
    patient_id = Column(Integer)
    status = Column(String)#confirmed cancelled rescheduled
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    #updated_at

    def __init__(self, id, doctor_id, date, start_time, end_time, patient_id, status):
        self.id = id
        self.doctor_id = doctor_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.patient_id = patient_id
        self.status = status


    def __repr__(self):
        return f"({self.id}, {self.doctor_id}, {self.date}, {self.start_time}, {self.end_time}, {self.patient_id}, {self.status})"


session = SessionLocal()
"""
doctor_schedule = DoctorSchedule(1, 1, "2023-09-12", "09:45", "11:45", 1, "Confirmed")
doctor_schedule1 = DoctorSchedule(2, 2, "2023-09-12", "19:45", "11:45", 1, "Pending")
doctor_schedule2 = DoctorSchedule(3, 3, "2023-09-12", "20:45", "11:45", 1, "Confirmed")
doctor_schedule3 = DoctorSchedule(4, 4, "2023-09-12", "21:45", "11:45", 1, "Confirmed")
doctor_schedule4 = DoctorSchedule(5, 5, "2023-09-12", "22:45", "11:45", 1, "Pending")
doctor_schedule5 = DoctorSchedule(6, 6, "2023-09-12", "23:45", "11:45", 1, "Confirmed")

session.add(doctor_schedule)
session.add(doctor_schedule1)
session.add(doctor_schedule2)
session.add(doctor_schedule3)
session.add(doctor_schedule4)
session.add(doctor_schedule5)
"""
session.commit()

""" GENETIC CONDITION """
class GeneticCondition(Base):
    __tablename__ = "genetic_conditions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    patient_id = Column(Integer)
    inheritance_pattern = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, name, description, patient_id, inheritance_pattern):
        self.id = id
        self.name = name
        self.description = description
        self.patient_id = patient_id
        self.inheritance_pattern = inheritance_pattern

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.description}, {self.patient_id}, {self.inheritance_pattern})"
    
session = SessionLocal()
"""
genetic_condition = GeneticCondition(1, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition1 = GeneticCondition(2, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition2 = GeneticCondition(3, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition3 = GeneticCondition(4, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition4 = GeneticCondition(5, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")
genetic_condition5 = GeneticCondition(6, "Sickle Cell Anaemia", "Blood Disease", 1, "X-Chromosome")

session.add(genetic_condition)
session.add(genetic_condition1)
session.add(genetic_condition2)
session.add(genetic_condition3)
session.add(genetic_condition4)
session.add(genetic_condition5)
"""
session.commit()


""" HOSPITAL """
class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(10))
    country_id = Column(String)
    phone_number = Column(String(20))
    website = Column(String(255))
    rating = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, name, address, city, state, zip_code, country_id, phone_number, website, rating):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country_id = country_id
        self.phone_number = phone_number
        self.website = website
        self.rating = rating

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country_id}, {self.phone_number}, {self.website}, {self.rating})"
    
session = SessionLocal()
"""
hospital = Hospital(1, "Nairobi Hospital", "Upper Hill", "Nairobi", "Nairobi", "00100", 1, "725348900", "www.nairobihospital.com", 5.0)
hospital1 = Hospital(2, "Karen Hospital", "Karen", "Nairobi", "Nairobi", "00100", 1, "725348900", "www.karenhospital.com", 5.0)
hospital2 = Hospital(3, "Kenyatta Hospital", "Kenyatta", "Nairobi", "Nairobi", "00100", 1, "725348900", "www.nairobihospital.com", 5.0)
hospital3 = Hospital(4, "Eldoret Teaching and Referral Hospital", "Upper Hill", "Nairobi", "Nairobi", "00100", 1, "725348900", "www.nairobihospital.com", 5.0)
hospital4 = Hospital(5, "Pwani Hospital", "Pwani", "Pwani", "Nairobi", "00100", 1, "725348900", "www.nairobihospital.com", 5.0)
hospital5 = Hospital(6, "Kakamega Teaching and Referral Hospital", "Upper Hill", "Nairobi", "Nairobi", "00100", 1, "725348900", "www.nairobihospital.com", 5.0)


session.add(hospital)
session.add(hospital1)
session.add(hospital2)
session.add(hospital3)
session.add(hospital4)
session.add(hospital5)
"""
session.commit()


""" IMMUNIZATION """
class Immunization(Base):
    __tablename__ = "immunizations"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    vaccine_name = Column(String(50))
    dose_number = Column(Integer)
    date_given = Column(Date)
    administering_provider = Column(String)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    #update_at

    def __init__(self, id, patient_id, vaccine_name, dose_number, date_given, administering_provider, expiration_date):
        self.id = id
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
immunization = Immunization(1, 1, "Pfizer vaccine", 2, "2023-12-17", "Kikuyu Hospital", "2025-09-16")
immunization1 = Immunization(2, 2, "Pfizer vaccine", 1, "2023-12-17", "Nairobi Hospital", "2025-09-16")
immunization2 = Immunization(3, 3, "Pfizer vaccine", 2, "2023-12-17", "Eldoret Teaching and Referral Hospital", "2025-09-16")
immunization3 = Immunization(4, 4, "Pfizer vaccine", 1, "2023-12-17", "Pumwani Hospital", "2025-09-16")
immunization4 = Immunization(5, 5, "Pfizer vaccine", 2, "2023-12-17", "Pwani Hospital", "2025-09-16")
immunization5 = Immunization(6, 6, "Pfizer vaccine", 1, "2023-12-17", "Kikuyu Hospital", "2025-09-16")


session.add(immunization)
session.add(immunization1)
session.add(immunization2)
session.add(immunization3)
session.add(immunization4)
session.add(immunization5)
"""
session.commit()


""" INSURANCE CLAIMS"""
class InsuranceClaim(Base):
    __tablename__ = "insurance_claims"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    provider_id = Column(Integer)
    date_of_service = Column(Date)
    procedure_code = Column(String)
    diagnosis_code = Column(String)
    billed_amount = Column(Float)
    insurance_paid = Column(Float)
    patient_paid = Column(Float)
    status = Column(String)# pending denied paids
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, patient_id, provider_id, date_of_service, procedure_code, diagnosis_code, billed_amount, insurance_paid, patient_paid, status):
        self.id = id
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
insurance_claim = InsuranceClaim(1, 1, 1, "2023-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Paid")
insurance_claim1 = InsuranceClaim(2, 2, 2, "2024-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Denied")
insurance_claim2 = InsuranceClaim(3, 3, 3, "2025-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Pending")
insurance_claim3 = InsuranceClaim(4, 4, 4, "2026-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Paid")
insurance_claim4 = InsuranceClaim(5, 5, 5, "2027-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Pending")
insurance_claim5 = InsuranceClaim(6, 6, 6, "2028-12-17", 1, 1, 1300.00, 300.00, 1000.00, "Paid")


session.add(insurance_claim)
session.add(insurance_claim1)
session.add(insurance_claim2)
session.add(insurance_claim3)
session.add(insurance_claim4)
session.add(insurance_claim5)
"""
session.commit()

""" INSURANCE PROVIDER """
class InsuranceProvider(Base):
    __tablename__ = "insurance_providers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String)
    address = Column(String(100))
    country_id = Column(Integer)
    phone_number = Column(String(20))
    email = Column(String)
    website = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    def __init__(self, id, name, type, address, country_id, phone_number, email, website):
        self.id = id
        self.name = name
        self.type = type
        self.address = address
        self.country_id = country_id
        self.phone_number = phone_number
        self.email = email
        self.website = website

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.type}, {self.address}, {self.country_id}, {self.phone_number}, {self.email}, {self.website})"
    

session = SessionLocal()
"""
insurance_provider = InsuranceProvider(1, "Britam Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider1 = InsuranceProvider(2, "Resolution Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider2 = InsuranceProvider(3, "NHIF Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider3 = InsuranceProvider(4, "Britam Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider4 = InsuranceProvider(5, "Britam Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")
insurance_provider5 = InsuranceProvider(6, "Britam Insurance", "Health Insurance", "P.O Box 980", 1, "780900900", "britam@gmail.com", "www.britam.co.ke")



session.add(insurance_provider)
session.add(insurance_provider1)
session.add(insurance_provider2)
session.add(insurance_provider3)
session.add(insurance_provider4)
session.add(insurance_provider5)
"""
session.commit()

""" INSURANCE INFORMATION """
class InsuranceInformation(Base):
    __tablename__ = "insurance_information"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    provider_name = Column(String)
    policy_number = Column(Integer)
    group_number = Column(Integer)
    plan_name = Column(String)
    plan_type = Column(String)
    effective_date = Column(Date)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, provider_name, policy_number, group_number, plan_name, plan_type, effective_date, expiration_date):
        self.id = id
        self.patient_id = patient_id
        self.provider_name = provider_name
        self.policy_number = policy_number
        self.group_number = group_number
        self.plan_name = plan_name
        self.plan_type = plan_type
        self.effective_date = effective_date
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.provider_name}, {self.policy_number}, {self.group_number}, {self.plan_name}, {self.plan_type}, {self.effective_date}, {self.expiration_date})"
    
session = SessionLocal()
"""
insurance_information = InsuranceInformation(1, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")
insurance_information1 = InsuranceInformation(2, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")
insurance_information2 = InsuranceInformation(3, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")
insurance_information3 = InsuranceInformation(4, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")
insurance_information4 = InsuranceInformation(5, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")
insurance_information5 = InsuranceInformation(6, 1, "Britam Insurance", 98003, 900, "Eye", "Full plan", "2023-12-12", "2023-12-24")


session.add(insurance_information)
session.add(insurance_information1)
session.add(insurance_information2)
session.add(insurance_information3)
session.add(insurance_information4)
session.add(insurance_information5)
"""
session.commit()
    
     
""" LAB TESTS """
class LabTest(Base):
    __tablename__ = "lab_tests"

    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    test_description = Column(String)
    test_type = Column(String) #blood test urine test
    test_cost = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, test_name, test_description, test_type, test_cost):
        self.id = id
        self.test_name = test_name
        self.test_description = test_description
        self.test_type = test_type
        self.test_cost = test_cost

    def __repr__(self):
        return f"({self.id}, {self.test_name}, {self.test_description}, {self.test_type}, {self.test_cost})"
    
session = SessionLocal()
"""
lab_test = LabTest(1, "Blood test", "Haemoglobin blood test", "Blood test", 900.00)
lab_test1 = LabTest(2, "Urine test", "Urine test", "Urine test", 1900.00)
lab_test2 = LabTest(3, "Blood test", "Haemoglobin blood test", "Blood test", 2900.00)
lab_test3 = LabTest(4, "Urine test", "Urine test", "Urine test", 3900.00)
lab_test4 = LabTest(5, "Blood test", "Haemoglobin blood test", "Blood test", 4900.00)
lab_test5 = LabTest(6, "Urine test", "Urine test", "Urine test", 5900.00)


session.add(lab_test)
session.add(lab_test1)
session.add(lab_test2)
session.add(lab_test3)
session.add(lab_test4)
session.add(lab_test5)
"""
session.commit()

""" LAB TEST ORDER """
class LabTestOrder(Base):
    __tablename__ = "lab_test_orders"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    test_id = Column(Integer)
    order_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    #updated_at

    def __init__(self, id, patient_id, doctor_id, test_id, order_date):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.test_id = test_id
        self.order_date = order_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.test_id}, {self.order_date})"
    
session = SessionLocal()
"""
test_order = LabTestOrder(1, 1, 1, 1, "2023-09-12")
test_order1 = LabTestOrder(2, 2, 2, 2, "2023-09-12")
test_order2 = LabTestOrder(3, 3, 3, 3, "2023-09-12")
test_order3 = LabTestOrder(4, 4, 4, 4, "2023-09-12")
test_order4 = LabTestOrder(5, 5, 5, 5, "2023-09-12")
test_order5 = LabTestOrder(6, 6, 6, 6, "2023-09-12")


session.add(test_order)
session.add(test_order1)
session.add(test_order2)
session.add(test_order3)
session.add(test_order4)
session.add(test_order5)
"""
session.commit()

""" LAB TEST RESULTS """
class LabTestResult(Base):
    __tablename__ = "lab_test_results"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    result_date = Column(Date)
    result_value = Column(Float)
    result_units = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    #updated_at


    def __init__(self, id, order_id, result_date, result_value, result_units):
        self.id = id
        self.order_id = order_id
        self.result_date = result_date
        self.result_value = result_value
        self.result_units = result_units

    def __repr__(self):
        return f"({self.id}, {self.order_id}, {self.result_date}, {self.result_value}, {self.result_units})"

session = SessionLocal()
"""
test_result = LabTestResult(1, 1, "2019-09-29", "30.45", "milligrams")
test_result1 = LabTestResult(2, 2, "2019-09-29", "30.45", "milligrams")
test_result2 = LabTestResult(3, 3, "2019-09-29", "30.45", "milligrams")
test_result3 = LabTestResult(4, 4, "2019-09-29", "30.45", "milligrams")
test_result4 = LabTestResult(5, 5, "2019-09-29", "30.45", "milligrams")
test_result5 = LabTestResult(6, 6, "2019-09-29", "30.45", "milligrams")



session.add(test_result)
session.add(test_result1)
session.add(test_result2)
session.add(test_result3)
session.add(test_result4)
session.add(test_result5)
"""
session.commit()

""" LAB TEST INTERPRETATIONS """
class LabTestInterpretation(Base):
    __tablename__ = "lab_test_interpretations"

    id = Column(Integer, primary_key=True)
    result_id = Column(Integer)
    text = Column(Text)


    def __init__(self, id, result_id, text):
        self.id = id
        self.result_id = result_id
        self.text = text

    def __repr__(self):
        return f"({self.id}, {self.result_id}, {self.text})"
    
session = SessionLocal()
"""
test_interpretation = LabTestInterpretation(1, 1, "The results show that the patient has blood cancer")
test_interpretation1 = LabTestInterpretation(2, 2, "The results show that the patient has blood cancer")
test_interpretation2 = LabTestInterpretation(3, 3, "The results show that the patient has blood cancer")
test_interpretation3 = LabTestInterpretation(4, 4, "The results show that the patient has blood cancer")
test_interpretation4 = LabTestInterpretation(5, 5, "The results show that the patient has blood cancer")
test_interpretation5 = LabTestInterpretation(6, 6, "The results show that the patient has blood cancer")

session.add(test_interpretation)
session.add(test_interpretation1)
session.add(test_interpretation2)
session.add(test_interpretation3)
session.add(test_interpretation4)
session.add(test_interpretation5)
"""
session.commit()
    

""" MEDICATION ALERTS """
class MedicationAlert(Base):
    __tablename__ = "medication_alerts"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    medication_id = Column(Integer)
    dosage = Column(Text)
    frequency = Column(Text)
    alert_date = Column(Date)
    alert_text = Column(Text)
    status = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, patient_id, medication_id, dosage, frequency, alert_date, alert_text, status):
        self.id = id
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
medication_alert = MedicationAlert(1, 1, 1, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert1 = MedicationAlert(2, 2, 2, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Pending")
medication_alert2 = MedicationAlert(3, 3, 3, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert3 = MedicationAlert(4, 4, 4, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Failed")
medication_alert4 = MedicationAlert(5, 5, 5, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")
medication_alert5 = MedicationAlert(6, 6, 6, "Malaria pills", "Twice a day", "2025-03-13", "Don't forget to take your pills", "Sent")

session.add(medication_alert)
session.add(medication_alert1)
session.add(medication_alert2)
session.add(medication_alert3)
session.add(medication_alert4)
session.add(medication_alert5)
"""
session.commit()

""" MEDICAL CONDITION """
class MedicalCondition(Base):
    __tablename__ = "medical_conditions"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, )
    name = Column(String(50))
    description = Column(Text)
    diagnosis_date = Column(Date)
    treatment = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, name, description, diagnosis_date, treatment):
        self.id = id
        self.patient_id = patient_id
        self.name = name
        self.description = description
        self.diagnosis_date = diagnosis_date
        self.treatment = treatment

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.name}, {self.description}, {self.diagnosis_date}, {self.treatment})"
    
session = SessionLocal()
"""
medication_condition = MedicalCondition(1, 1, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition1 = MedicalCondition(2, 2, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition2 = MedicalCondition(3, 3, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition3 = MedicalCondition(4, 4, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition4 = MedicalCondition(5, 5, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")
medication_condition5 = MedicalCondition(6, 6, "Diabetes", "Disease caused by sugar", "2025-03-13", "Insulin")

session.add(medication_condition)
session.add(medication_condition1)
session.add(medication_condition2)
session.add(medication_condition3)
session.add(medication_condition4)
session.add(medication_condition5)
"""
session.commit()

""" MEDICAL DEVICES """
class MedicalDevice(Base):
    __tablename__ = "medical_devices"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    model = Column(String)
    serial_number = Column(String)
    hospital_id = Column(Integer)
    department_id = Column(Integer)
    last_maintenance = Column(Date)
    next_maintenace = Column(Date) #maintenance
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, name, manufacturer, model, serial_number, hospital_id, department_id, last_maintenance, next_maintenance):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.hospital_id = hospital_id
        self.department_id = department_id
        self.last_maintenance = last_maintenance
        self.next_maintenace = next_maintenance

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.manufacturer}, {self.model}, {self.serial_number}, {self.hospital_id}, {self.department_id}, {self.last_maintenance}, {self.next_maintenace})"
    

session = SessionLocal()
"""
medical_device = MedicalDevice(1, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 1, 1, "2021-07-16", "2022-07-16")
medical_device1 = MedicalDevice(2, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 2, 2, "2021-07-16", "2022-07-16")
medical_device2 = MedicalDevice(3, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 3, 3, "2021-07-16", "2022-07-16")
medical_device3 = MedicalDevice(4, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 4, 4, "2021-07-16", "2022-07-16")
medical_device4 = MedicalDevice(5, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 5, 5, "2021-07-16", "2022-07-16")
medical_device5 = MedicalDevice(6, "Printer", "HP", "HP-900GHES", "239-GTJD-249", 6, 6, "2021-07-16", "2022-07-16")

session.add(medical_device)
session.add(medical_device1)
session.add(medical_device2)
session.add(medical_device3)
session.add(medical_device4)
session.add(medical_device5)
"""
session.commit()



""" MEDICAL IMAGES """
class MedicalImage(Base):
    __tablename__ = "medical_images"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    image_type = Column(String)
    image_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 

    def __init__(self, id, patient_id, doctor_id, image_type, image_date):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.image_type = image_type
        self.image_date = image_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.image_type}, {self.image_date})"
    
session = SessionLocal()
"""
medical_image = MedicalImage(1, 1, 1, "X-Ray", "2024-04-14")
medical_image1 = MedicalImage(2, 2, 2, "X-Ray", "2024-04-14")
medical_image2 = MedicalImage(3, 3, 3, "X-Ray", "2024-04-14")
medical_image3 = MedicalImage(4, 4, 4, "X-Ray", "2024-04-14")
medical_image4 = MedicalImage(5, 5, 5, "X-Ray", "2024-04-14")
medical_image5 = MedicalImage(6, 6, 6, "X-Ray", "2024-04-14")

session.add(medical_image)
session.add(medical_image1)
session.add(medical_image2)
session.add(medical_image3)
session.add(medical_image4)
session.add(medical_image5)
"""
session.commit()


"""MEDICAL NOTES """
class MedicalNote(Base):
    __tablename__ = "medical_notes"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    date = Column(Date)
    content = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()')) 
    #updated_at

    def __init__(self, id, patient_id, doctor_id, date, content):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.content = content

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.date}, {self.content})"
    
session = SessionLocal()
"""
medical_note = MedicalNote(1, 1, 1, "2024-04-14", "Needs monitoring")
medical_note1 = MedicalNote(2, 2, 2, "2024-04-14", "Needs monitoring")
medical_note2 = MedicalNote(3, 3, 3, "2024-04-14", "Needs monitoring")
medical_note3 = MedicalNote(4, 4, 4, "2024-04-14", "Needs monitoring")
medical_note4 = MedicalNote(5, 5, 5, "2024-04-14", "Needs monitoring")
medical_note5 = MedicalNote(6, 6, 6, "2024-04-14", "Needs monitoring")


session.add(medical_note)
session.add(medical_note1)
session.add(medical_note2)
session.add(medical_note3)
session.add(medical_note4)
session.add(medical_note5)
"""
session.commit()

""" MEDICAL PROCEDURES"""

class MedicalProcedure(Base):
    __tablename__ = "medical_procedures"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    name = Column(String)
    date = Column(Date)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, doctor_id, name, date, notes):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.name = name
        self.date = date
        self.notes = notes

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.name}, {self.date}, {self.notes})"
    
session = SessionLocal()
"""
medical_procedure = MedicalProcedure(1, 1, 1, "Colon surgery", "2017-08-01", "Successful")
medical_procedure1 = MedicalProcedure(2, 2, 2, "Colon surgery", "2017-08-01", "Successful")
medical_procedure2 = MedicalProcedure(3, 3, 3, "Colon surgery", "2017-08-01", "Successful")
medical_procedure3 = MedicalProcedure(4, 4, 4, "Colon surgery", "2017-08-01", "Successful")
medical_procedure4 = MedicalProcedure(5, 5, 5, "Colon surgery", "2017-08-01", "Successful")
medical_procedure5 = MedicalProcedure(6, 6, 6, "Colon surgery", "2017-08-01", "Successful")

session.add(medical_procedure)
session.add(medical_procedure1)
session.add(medical_procedure2)
session.add(medical_procedure3)
session.add(medical_procedure4)
session.add(medical_procedure5)
"""
session.commit()

""" MEDICAL STAFF """
class MedicalStaff(Base):
    __tablename__ = "medical_staff"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    dob = Column(Date)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(10))
    country_id = Column(String)
    phone_number = Column(Integer)
    email = Column(String)
    job_title = Column(String)
    department_id = Column(Integer)
    date_hired = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, name, gender, dob, address, city, state, zip_code, country_id, phone_number, email, job_title, department_id, date_hired):
        self.id = id
        self.name = name
        self.gender = gender
        self.dob = dob
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country_id = country_id
        self.phone_number = phone_number
        self.email = email
        self.job_title = job_title
        self.department_id = department_id
        self.date_hired = date_hired

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.gender}, {self.dob}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country_id}, {self.phone_number}, {self.email}, {self.job_title}, {self.department_id}, {self.date_hired})"
    
session = SessionLocal()
"""
medical_staff = MedicalStaff(1, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")
medical_staff1 = MedicalStaff(2, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")
medical_staff2 = MedicalStaff(3, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")
medical_staff3 = MedicalStaff(4, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")
medical_staff4 = MedicalStaff(5, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")
medical_staff5 = MedicalStaff(6, "Anna Oketch", "female", "2017-08-01", "P.O Box 2456", "Kisumu", "Kolanya", "00100", 1, "745600300", "soketch@gmail.com", "Nurse", 1, "2024-09-09")


session.add(medical_staff)
session.add(medical_staff1)
session.add(medical_staff2)
session.add(medical_staff3)
session.add(medical_staff4)
session.add(medical_staff5)
"""
session.commit()


""" MEDICATION """
class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, )
    name = Column(String)
    description = Column(String)
    route_of_administration = Column(String) #oral topical intravenous
    dosage = Column(String)
    unit = Column(String)
    frequency = Column(String)#twice daily once weekly
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, name, description, route_of_administration, dosage, unit, frequency, patient_id, doctor_id):
        self.id = id
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
medication = Medication(1, "Malaria", "Caused by mosquitos", "oral", "4", "milligram", "Twice daily", 1, 1)
medication1 = Medication(2, "Malaria", "Caused by mosquitos", "oral", "5", "milligram", "Twice daily", 2, 2)
medication2= Medication(3, "Malaria", "Caused by mosquitos", "oral", "6", "milligram", "Twice daily", 3, 3)
medication3 = Medication(4, "Malaria", "Caused by mosquitos", "oral", "7", "milligram", "Twice daily", 4, 4)
medication4 = Medication(5, "Malaria", "Caused by mosquitos", "oral", "8", "milligram", "Twice daily", 5, 5)
medication5 = Medication(6, "Malaria", "Caused by mosquitos", "oral", "9", "milligram", "Twice daily", 6, 6)


session.add(medication)
session.add(medication1)
session.add(medication2)
session.add(medication3)
session.add(medication4)
session.add(medication5)
"""
session.commit()


""" PATIENT CONSENT"""
class PatientConsent(Base):
    __tablename__ = "patient_consents"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    consent_type = Column(String)#treatment release of medical information
    consent_date = Column(Date)
    expiration_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, consent_type, consent_date, expiration_date):
        self.id = id
        self.patient_id = patient_id
        self.consent_type = consent_type
        self.consent_date = consent_date
        self.expiration_date = expiration_date

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.consent_type}, {self.consent_date}, {self.expiration_date})"
    
session = SessionLocal()
"""
patient_consent = PatientConsent(1, 1, "Treatment", "2015-08-15", "2019-09-18")
patient_consent1 = PatientConsent(2, 2, "Treatment", "2015-08-15", "2019-09-18")
patient_consent2 = PatientConsent(3, 3, "Treatment", "2015-08-15", "2019-09-18")
patient_consent3 = PatientConsent(4, 4, "Treatment", "2015-08-15", "2019-09-18")
patient_consent4 = PatientConsent(5, 5, "Treatment", "2015-08-15", "2019-09-18")
patient_consent5 = PatientConsent(6, 6, "Treatment", "2015-08-15", "2019-09-18")

session.add(patient_consent)
session.add(patient_consent1)
session.add(patient_consent2)
session.add(patient_consent3)
session.add(patient_consent4)
session.add(patient_consent5)
"""
session.commit()

""" PATIENT FEEDBACK """
class PatientFeedback(Base):
    __tablename__ = "patient_feedback"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    date = Column(Date)
    text = Column(Text)
    rating = Column(Integer)

    def __init__(self, id, patient_id, doctor_id, date, text, rating):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.text = text
        self.rating = rating

    def __repr__(self):
        return f"({self.id}, {self.patient_id}, {self.doctor_id}, {self.date}, {self.text}, {self.rating})"
    
session = SessionLocal()
"""
patient_feedback = PatientFeedback(1, 1, 1, "2015-08-15", "Good doctor. Highly recommend", 5)
patient_feedback1 = PatientFeedback(2, 2, 2, "2015-08-15", "Good doctor. Highly recommend", 1)
patient_feedback2 = PatientFeedback(3, 3, 3, "2015-08-15", "Good doctor. Highly recommend", 2)
patient_feedback3 = PatientFeedback(4, 4, 4, "2015-08-15", "Good doctor. Highly recommend", 3)
patient_feedback4 = PatientFeedback(5, 5, 5, "2015-08-15", "Good doctor. Highly recommend", 4)
patient_feedback5 = PatientFeedback(6, 6, 6, "2015-08-15", "Good doctor. Highly recommend", 5)

session.add(patient_feedback)
session.add(patient_feedback1)
session.add(patient_feedback2)
session.add(patient_feedback3)
session.add(patient_feedback4)
session.add(patient_feedback5)
"""
session.commit()

""" PATIENT VISIT """
class PatientVisit(Base):
    __tablename__ = "patient_visits"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer)
    doctor_id = Column(Integer)
    appointment_id = Column(Integer)
    visit_date = Column(Date)
    chief_complaint = Column(Text)
    diagnosis_id = Column(Integer)
    notes = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, patient_id, doctor_id, appointment_id, visit_date, chief_complaint, diagnosis_id, notes):
        self.id = id
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
patient_visit = PatientVisit(1, 1, 1, 1, "2015-08-15", "Fever and nausea", 1, "Patient doing okay")
patient_visit1 = PatientVisit(2, 2, 2, 2, "2015-08-15", "Fever and nausea", 2, "Patient doing okay")
patient_visit2 = PatientVisit(3, 3, 3, 3, "2015-08-15", "Fever and nausea", 3, "Patient doing okay")
patient_visit3 = PatientVisit(4, 4, 4, 4, "2015-08-15", "Fever and nausea", 4, "Patient doing okay")
patient_visit4 = PatientVisit(5, 5, 5, 5, "2015-08-15", "Fever and nausea", 5, "Patient doing okay")
patient_visit5 = PatientVisit(6, 6, 6, 6, "2015-08-15", "Fever and nausea", 6, "Patient doing okay")

session.add(patient_visit)
session.add(patient_visit1)
session.add(patient_visit2)
session.add(patient_visit3)
session.add(patient_visit4)
session.add(patient_visit5)
"""
session.commit()

""" PATIENT """
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String, )
    phone_number = Column(Integer)
    email = Column(String)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(10))
    country_id = Column(String)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String(20))
    insurance_provider_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, firstname, lastname, date_of_birth, gender, phone_number, email, address, city, state, zip_code, country_id, emergency_contact_name, emergency_contact_phone, insurance_provider_id):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country_id = country_id
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.insurance_provider_id = insurance_provider_id

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.date_of_birth}, {self.gender}, {self.phone_number}, {self.email}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country_id}, {self.emergency_contact_name}, {self.emergency_contact_phone}, {self.insurance_provider_id})"
    
session = SessionLocal()
"""
patient = Patient(1, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 1)
patient1 = Patient(2, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 2)
patient2 = Patient(3, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 3)
patient3 = Patient(4, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 4)
patient4 = Patient(5, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 5)
patient5 = Patient(6, "fortune", "amombo", "2015-08-15", "male", "745369800", "amombofortune77@gmail.com", "P.O Box 980", "Nairobi", "Kileleshwa", "00100", 1, "Dennis Okutoyi", "735400400", 6)

session.add(patient)
session.add(patient1)
session.add(patient2)
session.add(patient3)
session.add(patient4)
session.add(patient5)
"""
session.commit()

"""PRESCRIPTION """
class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    patient_id = Column(Integer)
    medication = Column(String)
    dosage = Column(String)
    instructions = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    #updated_at

    def __init__(self, id, doctor_id, patient_id, medication, dosage, instructions):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions


    def __repr__(self):
        return f"({self.id}, {self.doctor_id}, {self.patient_id}, {self.medication}, {self.dosage}, {self.instructions})"
    

session = SessionLocal()
"""
prescription = Prescription(1, 1, 1, "malaria", "10", "Twice a day")
prescription1 = Prescription(2, 2, 2, "malaria", "10", "Twice a day")
prescription2 = Prescription(3, 3, 3, "malaria", "10", "Twice a day")
prescription3 = Prescription(4, 4, 4, "malaria", "10", "Twice a day")
prescription4 = Prescription(5, 5, 5, "malaria", "10", "Twice a day")
prescription5 = Prescription(6, 6, 6, "malaria", "10", "Twice a day")

session.add(prescription)
session.add(prescription1)
session.add(prescription2)
session.add(prescription3)
session.add(prescription4)
session.add(prescription5)
"""
session.commit()


""" REFERRALS """
class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True)
    referring_patient_id = Column(Integer)
    referred_patient_id = Column(Integer)
    referring_doctor_id = Column(Integer)
    referred_doctor_id = Column(Integer)
    referred_hospital_id = Column(Integer)
    referral_date = Column(Date)
    referral_reason = Column(Text)
    status = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    def __init__(self, id, referring_patient_id, referred_patient_id, referring_doctor_id, referred_doctor_id, referred_hospital_id, referral_date, referral_reason, status):
        self.id = id
        self.referring_patient_id = referring_patient_id
        self.referred_patient_id = referred_patient_id
        self.referring_doctor_id = referring_doctor_id
        self.referred_doctor_id = referred_doctor_id
        self.referred_hospital_id = referred_hospital_id
        self.referral_date = referral_date
        self.referral_reason = referral_reason
        self.status = status

    def __repr__(self):
        return f"({self.id}, {self.referring_patient_id}, {self.referred_patient_id}, {self.referring_doctor_id}, {self.referred_doctor_id}, {self.referred_hospital_id}, {self.referral_date}, {self.referral_reason}, {self.status})"
    
session = SessionLocal()
"""
referral = Referral(1, 1, 1, 1, 1, 1, "2024-09-18", "Good services", "Done")
referral1 = Referral(2, 2, 2, 2, 2, 2, "2024-09-18", "Good services", "Pending")
referral2 = Referral(3, 3, 3, 3, 3, 3, "2024-09-18", "Good services", "Done")
referral3 = Referral(4, 4, 4, 4, 4, 4, "2024-09-18", "Good services", "Pending")
referral4 = Referral(5, 5, 5, 5, 5, 5, "2024-09-18", "Good services", "Done")
referral5 = Referral(6, 6, 6, 6, 6, 6, "2024-09-18", "Good services", "Done")


session.add(referral)
session.add(referral1)
session.add(referral2)
session.add(referral3)
session.add(referral4)
session.add(referral5)
"""
session.commit()

""" USERS """ 
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String)
    phone_number = Column(Integer)
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip_code = Column(String(10))
    country_id = Column(String)
    user_type = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    def __init__(self, id, username, password, first_name, last_name, date_of_birth, email, phone_number, address, city, state, zip_code, country_id, user_type):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country_id = country_id
        self.user_type = user_type


    def __repr__(self):
        return f"({self.id}, {self.username}, {self.password}, {self.first_name}, {self.last_name}, {self.date_of_birth}, {self.email}, {self.phone_number}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.country_id}, {self.user_type})"
    
session = SessionLocal()
"""
user = Users(1, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 1, "Admin")
user1 = Users(2, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 2, "Admin")
user2 = Users(3, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 3, "Admin")
user3 = Users(4, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 4, "Admin")
user4 = Users(5, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 5, "Admin")
user5 = Users(6, "fortuneamombo", "password", "fortune", "amombo", "2024-09-18", "amombofortune@gmail.com", "746500700", "B29 7ND", "Birmingham", "West Midlands", "00100", 6, "Admin")

session.add(user)
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.add(user5)
"""
session.commit()


""" VACCINATION """
class Vaccination(Base):
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, )
    vaccine_name = Column(String)
    administered_by = Column(String)
    administered_at = Column(TIMESTAMP(timezone=True))
    next_dose_due = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    def __init__(self, id, patient_id, vaccine_name, administered_by, administered_at, next_dose_due):
        self.id = id
        self.patient_id = patient_id
        self.vaccine_name = vaccine_name
        self.administered_by = administered_by
        self.administered_at = administered_at
        self.next_dose_due = next_dose_due


session = SessionLocal()
"""
vaccination = Vaccination(1, 1, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination1 = Vaccination(2, 2, "Moderna vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination2 = Vaccination(3, 3, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination3 = Vaccination(4, 4, "Astra Zeneca vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination4 = Vaccination(5, 5, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")
vaccination5 = Vaccination(6, 6, "Pfizer vaccine", "Dr. Sikhwele", "2024-09-18", "2024-10-18")

session.add(vaccination)
session.add(vaccination1)
session.add(vaccination2)
session.add(vaccination3)
session.add(vaccination4)
session.add(vaccination5)
"""
session.commit()


""" VITAL SIGNS """
class VitalSign(Base):
    __tablename__ = "vital_signs"

    id = Column(Integer, primary_key=True)
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


    def __init__(self, id, patient_id, doctor_id, heart_rate, blood_pressure_systolic, blood_pressure_diastolic, respiratory_rate, temperature, height, weight, oxygen_saturation,recorded_at):
        self.id = id
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
vital_sign = VitalSign(1, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign1 = VitalSign(2, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign2 = VitalSign(3, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign3 = VitalSign(4, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign4 = VitalSign(5, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")
vital_sign5 = VitalSign(6, 1, 1, 24, 56, 56, 102, 34, 170, 75, 390, "2023-09-09")


session.add(vital_sign)
session.add(vital_sign1)
session.add(vital_sign2)
session.add(vital_sign3)
session.add(vital_sign4)
session.add(vital_sign5)
"""
session.commit()

""" WARD """
class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    capacity = Column(Integer)
    location = Column(String)
    hospital_id = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


    def __init__(self, id, name, type, capacity, location, hospital_id):
        self.id = id
        self.name = name
        self.type = type
        self.capacity = capacity
        self.location = location
        self.hospital_id = hospital_id

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.type}, {self.capacity}, {self.location}, {self.hospital_id})"
    
session = SessionLocal()
"""
ward = Ward(1, "Orthopedics", "Orthopedics", 240, "Left Wing", 1)
ward1 = Ward(2, "Orthopedics", "Orthopedics", 240, "Left Wing", 2)
ward2 = Ward(3, "Orthopedics", "Orthopedics", 240, "Left Wing", 3)
ward3 = Ward(4, "Orthopedics", "Orthopedics", 240, "Left Wing", 4)
ward4 = Ward(5, "Orthopedics", "Orthopedics", 240, "Left Wing", 5)
ward5 = Ward(6, "Orthopedics", "Orthopedics", 240, "Left Wing", 6)

session.add(ward)
session.add(ward1)
session.add(ward2)
session.add(ward3)
session.add(ward4)
session.add(ward5)
"""
session.commit()


#results = session.query(Person).all()
#print(results)
#results = session.query(Person).filter(Person.gender == 'female')
#for r in results:
 #   print(r)


    



