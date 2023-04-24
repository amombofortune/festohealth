from datetime import date, datetime, time
from pydantic import BaseModel
    
"""Admission"""
class AdmissionBase(BaseModel):
    id: int
    patient_id: int
    admission_date: date
    admission_time: time
    discharge_date: date
    discharge_time: time
    reason: str
    diagnosis: str
    treatment: str
    doctor_id: int

class AdmissionCreate(AdmissionBase):
    pass

class AdmissionResponse(AdmissionBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Adverse Reaction"""
class AdverseReactionBase(BaseModel):
    id: int
    patient_id: int
    reaction_date: date
    reaction_time: time
    reaction_type: str
    reaction_details: str
    medication_name: str
    dosage: str
    severity: str
    treatment: str

class AdverseReactionCreate(AdverseReactionBase):
    pass


class AdverseReactionResponse(AdverseReactionBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Adverse Reaction Type"""
class AdverseReactionTypeBase(BaseModel):
    id: int
    name: str
    description: str

class AdverseReactionTypeCreate(AdverseReactionTypeBase):
    pass


class AdverseReactionTypeResponse(AdverseReactionTypeBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Allergy"""
class AllergyBase(BaseModel):
    id: int
    name: str

class AllergyCreate(AllergyBase):
    pass

class AllergyResponse(AllergyBase):
    created_at: datetime

    class Config:
        orm_mode= True



"""Appointment Reminder"""
class AppointmentReminderBase(BaseModel):
    id: int
    appointment_id: int
    user_id: int
    reminder_date: date
    reminder_time: time
    reminder_type: str
    status: str

class AppointmentReminderCreate(AppointmentReminderBase):
    pass


class AppointmentReminderResponse(AppointmentReminderBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Appointment""" 
class AppointmentBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_type: str
    appointment_date: date
    appointment_start_time: time
    appointment_end_time: time
    description: str
    status: str

class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Bed""" 
class BedBase(BaseModel):
    id: int
    ward_id: int
    bed_no: int
    bed_type: str
    availability: bool
    occupied_by: int

class BedCreate(BedBase):
    pass


class BedResponse(BedBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Bed Assignment""" 
class BedAssignmentBase(BaseModel):
    id: int
    bed_id: int
    patient_id: int
    assigned_by: int
    assigned_at: datetime
    discharged_at: datetime

class BedAssignmentCreate(BedAssignmentBase):
    pass


class BedAssignmentResponse(BedAssignmentBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Billing"""
class BillingBase(BaseModel):
     id: int
     patient_id: int
     bill_date: date
     amount_due: float
     amount_paid: float
     payment_method: str

class BillingCreate(BillingBase):
    pass


class BillingResponse(BillingBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Care Team """
class CareTeamBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: str
    contact_number: int
    email: str
    patient_id: int
    start_date: date
    end_date: date

class CareTeamCreate(CareTeamBase):
    pass


class CareTeamResponse(CareTeamBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Chronic condition"""
class ChronicConditionBase(BaseModel):
    id: int
    patient_id: int
    condition: str
    diagnosis_date: date
    severity: str
    notes: str

class ChronicConditionCreate(ChronicConditionBase):
    pass


class ChronicConditionResponse(ChronicConditionBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Country"""
class CountryBase(BaseModel):
    id: int
    name: str
    code: str

class CountryCreate(CountryBase):
    pass


class CountryResponse(CountryBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Department"""
class DepartmentBase(BaseModel):
    id: int
    name: str
    description: str
    head_doctor_id: int

class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Diagnosis"""
class DiagnosisBase(BaseModel):
    id: int
    patient_id: int
    disease_id: int
    diagnosis: int
    date: date
    doctor_id: int
    notes: str

class DiagnosisCreate(DiagnosisBase):
    pass


class DiagnosisResponse(DiagnosisBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Diseases"""
class DiseaseBase(BaseModel):
    id: int
    name: str
    description: str
    symptoms: str
    treatment: str
    prevention: str

class DiseaseCreate(DiseaseBase):
    pass


class DiseaseResponse(DiseaseBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Doctor"""
class DoctorBase(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    phone_number: str
    specialty: str
    verified: bool
    work_schedule: str

class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Doctor Schedules"""
class DoctorScheduleBase(BaseModel):
    id: int
    doctor_id: int
    date: date
    start_time: time
    end_time: time
    patient_id: int
    status: str

class DoctorScheduleCreate(DoctorScheduleBase):
    pass

class DoctorScheduleResponse(DoctorScheduleBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Genetic Condition"""
class GeneticConditionBase(BaseModel):
    id: int
    name: str
    description: str
    patient_id: int
    inheritance_pattern: str

class GeneticConditionCreate(GeneticConditionBase):
    pass


class GeneticConditionResponse(GeneticConditionBase):
    created_at: datetime

    class Config:
        orm_mode= True

""" Hospital """
class HospitalBase(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    zip_code: str
    country_id: int
    phone_number: str
    website: str
    rating: float

class HospitalCreate(HospitalBase):
    pass


class HospitalResponse(HospitalBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Immunization"""
class ImmunizationBase(BaseModel):
    id: int
    patient_id: int
    vaccine_name: str
    dose_number: int
    date_given: date
    administering_provider: str
    expiration_date: date


class ImmunizationCreate(ImmunizationBase):
    pass


class ImmunizationResponse(ImmunizationBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Insurance claims"""
class InsuranceClaimBase(BaseModel):
    id: int
    patient_id: int
    provider_id: int
    date_of_service: date
    procedure_code: str
    diagnosis_code: str
    billed_amount: float
    insurance_paid: float
    patient_paid: float
    status: str

class InsuranceClaimCreate(InsuranceClaimBase):
    pass


class InsuranceClaimResponse(InsuranceClaimBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Insurance provider"""
class InsuranceProviderBase(BaseModel):
    id: int
    name: str
    type: str
    address: str
    country_id: int
    phone_number: int
    email: str
    website: str

class InsuranceProviderCreate(InsuranceProviderBase):
    pass


class InsuranceProviderResponse(InsuranceProviderBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Insurance information"""
class InsuranceInformationBase(BaseModel):
    id: int
    patient_id: int
    provider_name: str
    policy_number: int
    group_number: int
    plan_name: str
    plan_type: str
    effective_date: date
    expiration_date: date

class InsuranceInformationCreate(InsuranceInformationBase):
    pass


class InsuranceInformationResponse(InsuranceInformationBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Lab test"""
class LabTestBase(BaseModel):
    id: int
    test_name: str
    test_description: str
    test_type: str
    test_cost: float

class LabTestCreate(LabTestBase):
    pass


class LabTestResponse(LabTestBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Lab test Order"""
class LabTestOrderBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    test_id: int
    order_date: date

class LabTestOrderCreate(LabTestOrderBase):
    pass


class LabTestOrderResponse(LabTestOrderBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Lab Test Result"""
class LabTestResultBase(BaseModel):
    id: int
    order_id: int
    result_date: date
    result_value: float
    result_units: str

class LabTestResultCreate(LabTestResultBase):
    pass


class LabTestResultResponse(LabTestResultBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Lab Test Interpretation"""
class LabTestInterpretationBase(BaseModel):
    id: int
    result_id: int
    text: str

class LabTestInterpretationCreate(LabTestInterpretationBase):
    pass


class LabTestInterpretationResponse(LabTestInterpretationBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Medication Alerts"""
class MedicationAlertBase(BaseModel):
    id: int
    patient_id: int
    medication_id: int
    dosage: str
    frequency: str
    alert_date: date
    alert_text: str
    status: str

class MedicationAlertCreate(MedicationAlertBase):
    pass


class MedicationAlertResponse(MedicationAlertBase):
    created_at: datetime

    class Config:
        orm_mode= True
   
"""Medical conditions"""
class MedicalConditionBase(BaseModel):
    id: int
    patient_id: int
    name: str
    description: str
    diagnosis_date: date
    treatment: str

class MedicalConditionCreate(MedicalConditionBase):
    pass


class MedicalConditionResponse(MedicalConditionBase):
    created_at: datetime

    class Config:
        orm_mode= True
     

"""Medical devices"""
class MedicalDeviceBase(BaseModel):
    id: int
    name: str
    manufacturer: str
    model: str
    serial_number: str
    hospital_id: int
    department_id: int
    last_maintenance: date
    next_maintenace: date #maintenance

class MedicalDeviceCreate(MedicalDeviceBase):
    pass


class MedicalDeviceResponse(MedicalDeviceBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Medical images"""
class MedicalImageBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    image_type: str
    image_date: date

class MedicalImageCreate(MedicalImageBase):
    pass


class MedicalImageResponse(MedicalImageBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Medical notes"""
class MedicalNoteBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: date
    content: str

class MedicalNoteCreate(MedicalNoteBase):
    pass


class MedicalNoteResponse(MedicalNoteBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Medical procedures"""
class MedicalProcedureBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    name: str
    date: date
    notes: str

class MedicalProcedureCreate(MedicalProcedureBase):
    pass


class MedicalProcedureResponse(MedicalProcedureBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Medical staff"""
class MedicalStaffBase(BaseModel):
    id: int
    name: str
    gender: str
    dob: date
    address: str
    city: str
    state: str
    zip_code: str
    country_id: int
    phone_number: int
    email: str
    job_title: str
    department_id: int
    date_hired: date

class MedicalStaffCreate(MedicalStaffBase):
    pass


class MedicalStaffResponse(MedicalStaffBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Medication"""
class MedicationBase(BaseModel):
    id: int
    name: str
    description: str
    route_of_administration: str
    dosage: str
    unit: str
    frequency: str
    patient_id: int
    doctor_id: int

class MedicationCreate(MedicationBase):
    pass


class MedicationResponse(MedicationBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Patient consent"""
class PatientConsentBase(BaseModel):
    id: int
    patient_id: int
    consent_type: str
    consent_date: date
    expiration_date: date

class PatientConsentCreate(PatientConsentBase):
    pass


class PatientConsentResponse(PatientConsentBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Patient feedback"""
class PatientFeedbackBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: date
    text: str
    rating: int

class PatientFeedbackCreate(PatientFeedbackBase):
    pass


class PatientFeedbackResponse(PatientFeedbackBase):
    #created_at: datetime

    class Config:
        orm_mode= True


"""Patient visit"""
class PatientVisitBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_id: int
    visit_date: date
    chief_complaint: str
    diagnosis_id: int
    notes: str

class PatientVisitCreate(PatientVisitBase):
    pass


class PatientVisitResponse(PatientVisitBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Patient """
class PatientBase(BaseModel):
    id: int
    firstname: str
    lastname: str
    date_of_birth: date
    gender: str
    phone_number: int
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country_id: int
    emergency_contact_name: str
    emergency_contact_phone: str
    insurance_provider_id: int


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Prescription""" 
class PrescriptionBase(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Referrals"""
class ReferralBase(BaseModel):
    id: int
    referring_patient_id: int
    referred_patient_id: int
    referring_doctor_id: int
    referred_doctor_id: int
    referred_hospital_id: int
    referral_date: date
    referral_reason: str
    status: str


class ReferralCreate(ReferralBase):
    pass


class ReferralResponse(ReferralBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""User""" 
class UserBase(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    date_of_birth: date
    email: str
    phone_number: int
    address: str
    city: str
    state: str
    zip_code: str
    country_id: int
    user_type: str

class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    created_at: datetime

    class Config:
        orm_mode= True

"""Vaccinations """
class VaccinationBase(BaseModel):
    id: int
    patient_id: int
    vaccine_name: str
    administered_by: str
    administered_at: datetime
    next_dose_due: date


class VaccinationCreate(VaccinationBase):
    pass


class VaccinationResponse(VaccinationBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Vital signs """
class VitalSignBase(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    heart_rate: float
    blood_pressure_systolic: float
    blood_pressure_diastolic: float
    respiratory_rate: float
    temperature: float
    height: float
    weight: float
    oxygen_saturation: int
    recorded_at: datetime


class VitalSignCreate(VitalSignBase):
    pass


class VitalSignResponse(VitalSignBase):
    created_at: datetime

    class Config:
        orm_mode= True


"""Ward """
class WardBase(BaseModel):
    id: int
    name: str
    type: str
    capacity: int
    location: str
    hospital_id: int

class WardCreate(WardBase):
    pass


class WardResponse(WardBase):
    created_at: datetime

    class Config:
        orm_mode= True


        