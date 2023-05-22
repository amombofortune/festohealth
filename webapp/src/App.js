import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Trial from "./components/trial/Trial";
import AppointmentForm from "./components/appointment/AppointmentForm";
import AppointmentTable from "./components/appointment/AppointmentTable";
import Appointment from "./components/appointment/Appointment";
import Admission from "./components/admission/Admission";
import AdverseReaction from "./components/adverse_reaction/AdverseReaction";
import AdverseReactionType from "./components/adverse_reaction_type/AdverseReactionType";
import Allergy from "./components/allergy/Allergy";
import Bed from "./components/bed/Bed";
import Billing from "./components/billing/Billing";
import ChronicCondition from "./components/chronic_condition/ChronicCondition";
import Country from "./components/country/Country";
import Department from "./components/department/Department";
import Diagnosis from "./components/diagnosis/Diagnosis";
import Disease from "./components/disease/Disease";
import Doctor from "./components/doctor/Doctor";
import GeneticCondition from "./components/genetic_condition/GeneticCondition";
import Hospital from "./components/hospital/Hospital";
import Immunization from "./components/immunization/Immunization";
import InsuranceClaim from "./components/insurance_claim/InsuranceClaim";
import InsuranceProvider from "./components/insurance_provider/InsuranceProvider";
import LabResult from "./components/lab_result/LabResult";
import LabTest from "./components/lab_test/LabTest";
import MedicalCondition from "./components/medical_condition/MedicalCondition";
import MedicalDevice from "./components/medical_devices/MedicalDevice";
import MedicalImage from "./components/medical_image/MedicalImage";
import MedicalNote from "./components/medical_note/MedicalNote";
import MedicalProcedure from "./components/medical_procedure/MedicalProcedure";
import Medication from "./components/medication/Medication";
import MedicationAlert from "./components/medication_alert/MedicationAlert";
import PatientConsent from "./components/patient_consent/PatientConsent";
import Patient from "./components/patient/Patient";
import PatientFeedback from "./components/patient_feedback/PatientFeedback";
import PatientVisit from "./components/patient_visit/PatientVisit";
import Prescription from "./components/prescription/Prescription";
import Referral from "./components/referral/Referral";
import Vaccination from "./components/vaccination/Vaccination";
import VitalSign from "./components/vital_sign/VitalSign";
import Ward from "./components/ward/Ward";
import Login from "./components/login/Login";
import Registration from "./components/registration/Registration";

//Dashboard
import Home from "./pages/home/Home";
import List from "./pages/list/List";
//import Login from "./pages/login/Login";
import New from "./pages/new/New";
import Single from "./pages/single/Single";
import SideBar from "./components/sidebar/SideBar";
import NavBar from "./components/navbar/Navbar";
import { productInputs, userInputs } from "./formSource";
import Complete from "./components/trial/Complete";
import AppointmentEdit from "./components/appointment/AppointmentEdit";
import Nurse from "./components/nurse/Nurse";

function App() {
  return (
    <div className="app">
      <BrowserRouter>
        <Routes>
          <Route path="/admission" element={<Admission />} />
          <Route path="/adverse_reaction" element={<AdverseReaction />} />
          <Route
            path="/adverse_reaction_type"
            element={<AdverseReactionType />}
          />
          <Route path="/allergy" element={<Allergy />} />
          <Route path="/bed" element={<Bed />} />
          <Route path="/billing" element={<Billing />} />
          <Route path="/chronic_condition" element={<ChronicCondition />} />
          <Route path="/diagnosis" element={<Diagnosis />} />
          <Route path="/disease" element={<Disease />} />
          <Route path="/country" element={<Country />} />
          <Route path="/department" element={<Department />} />
          <Route path="/doctor" element={<Doctor />} />
          <Route path="/genetic_condition" element={<GeneticCondition />} />
          <Route path="/hospital" element={<Hospital />} />
          <Route path="/immunization" element={<Immunization />} />
          <Route path="/insurance_claim" element={<InsuranceClaim />} />
          <Route path="/insurance_provider" element={<InsuranceProvider />} />
          <Route path="/lab_result" element={<LabResult />} />
          <Route path="/lab_test" element={<LabTest />} />
          <Route path="/medical_condition" element={<MedicalCondition />} />
          <Route path="/medical_device" element={<MedicalDevice />} />
          <Route path="/medical_image" element={<MedicalImage />} />
          <Route path="/medical_note" element={<MedicalNote />} />
          <Route path="/medical_procedure" element={<MedicalProcedure />} />
          <Route path="/medication" element={<Medication />} />
          <Route path="/medication_alert" element={<MedicationAlert />} />
          <Route path="/nurse" element={<Nurse />} />
          <Route path="/patient_consent" element={<PatientConsent />} />
          <Route path="/patient" element={<Patient />} />
          <Route path="/patient_feedback" element={<PatientFeedback />} />
          <Route path="/patient_visit" element={<PatientVisit />} />
          <Route path="/prescription" element={<Prescription />} />
          <Route path="/referral" element={<Referral />} />
          <Route path="/vaccination" element={<Vaccination />} />
          <Route path="/vital_sign" element={<VitalSign />} />
          <Route path="/ward" element={<Ward />} />
          <Route path="/trial" element={<Trial />} />

          <Route path="/appointment" element={<Appointment />} />
          <Route path="/appointmentedit" element={<AppointmentEdit />} />
          <Route path="/appointmentform" element={<AppointmentForm />} />
          <Route path="/appointmenttable" element={<AppointmentTable />} />
          <Route path="/complete" element={<Complete />} />
          <Route path="/login" element={<Login />} />
          <Route path="/registration" element={<Registration />} />

          {"Dashboard"}
          <Route path="/">
            <Route index element={<Home />} />
            <Route path="login" element={<Login />} />
            <Route path="users">
              <Route index element={<List />} />
              <Route path=":userId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={userInputs} title="Add New User" />}
              />
            </Route>
            <Route path="products">
              <Route index element={<List />} />
              <Route path=":productId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={productInputs} title="Add New Product" />}
              />
            </Route>
            <Route path="/sidebar" element={<SideBar />} />
            <Route path="/navbar" element={<NavBar />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
