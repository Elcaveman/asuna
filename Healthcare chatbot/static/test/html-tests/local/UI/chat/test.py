import json

def what_are_your_symptoms(patient_symptoms):
	print(patient_symptoms)
	"""patient_symptoms=[
      "pain chest",
      "shortness of breath",
      "dizziness",
	]"""
	symptoms_matched = 0
	potential_diagnosis = []#[{desease,percent}]
	with open('../rawdata/disease.json','r') as f:
		diseases = json.load(f)
		for patient_symptom in patient_symptoms:
			for disease in diseases:
    			if patient_symptom in diseases[disease]['symptoms']:
    				symptoms_matched+=1
    				if diseases[disease]['disease'] in potential_diagnosis:
    					i = potential_diagnosis.index(diseases[disease]['disease'
						percentages[i] +=1
					else:
						potential_diagnosis.append(diseases[disease]['disease'])
						percentages.append(1)
		for i in range(percentages):
    		percentages[i] = percentages[i]/symptoms_matched
		print(potential_diagnosis)
	return potential_diagnosis