const encounter1 = {
    encounter_id: 100001,
    patient_nbr: 20001,
    age: "[50-60)",
    time_in_hospital: 4,
    number_inpatient: 1,
    number_emergency: 0,
    number_outpatient: 2,
    num_medications: 12,
    num_lab_procedures: 35,
    discharge_disposition_id: 1,
    admission_type_id: 1,
};
const encounter2 = {
    encounter_id: 100002,
    patient_nbr: 20002,
    age: "[60-70)",
    time_in_hospital: 7,
    number_inpatient: 2,
    number_emergency: 1,
    number_outpatient: 0,
    num_medications: 18,
    num_lab_procedures: 42,
    discharge_disposition_id: 3,
    admission_type_id: 2,
};
const encounter3 = {
    encounter_id: 100003,
    patient_nbr: 20003,
    age: "[40-50)",
    time_in_hospital: 2,
    number_inpatient: 0,
    number_emergency: 1,
    number_outpatient: 3,
    num_medications: 8,
    num_lab_procedures: 20,
    discharge_disposition_id: 1,
    admission_type_id: 3,
};
export const Encounters = [
    encounter1,
    encounter2,
    encounter3,
];
console.log(Encounters);
