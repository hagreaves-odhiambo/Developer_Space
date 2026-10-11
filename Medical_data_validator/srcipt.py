import re

medical_records = [
    {
        'patient_id': 'P1300',
        'age': 44,
        'gender': 'Male',
        'diagnosis': 'Tuberculosis',
        'medications': ['Injection'],
        'last_visit_id': 'V5341',
    },
    {
        'patient_id': 'p4502',
        'age': 63,
        'gender': 'female',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v5342',
    },
    {
        'patient_id': 'P3457',
        'age': 30,
        'gender': 'male',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v4343',
    },
    {
        'patient_id': 'p4503',
        'age': 69,
        'gender': 'Female',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V4344',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            value = dictionary[key]
            print(f" Unexpected format '{key}: {value}' at position {index}.")
            

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)