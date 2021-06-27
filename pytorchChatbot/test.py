import json

def what_are_your_symptoms(patient_symptoms):
	print(patient_symptoms)
	"""patient_symptoms=[
      "pain chest",
      "shortness of breath",
      "dizziness",
	]"""

	potential_diagnosis = []#[[desease,percent]]
	proba = []#these two are parrallel lists
	with open('disease.json','r') as f:
		diseases = json.load(f)
		for patient_symptom in patient_symptoms:
			for disease in diseases:
				if patient_symptom in diseases[disease]['symptoms']:
					total_symp = len(diseases[disease]['symptoms'])
					print("symptoms",diseases[disease]['symptoms'])
					if diseases[disease]['disease'] in potential_diagnosis:
						i = potential_diagnosis.index(diseases[disease]['disease'])
						proba[i] += 1/total_symp
					else:
						potential_diagnosis.append(diseases[disease]['disease'])
						proba.append(1/total_symp)
		
		if proba == []:
			j = 0
			potential_diagnosis.append(["you are maybe exausted",])
			mx = "?"
		else:
			mx_ = max(proba)
			mx = "{:.4f}".format(mx_)
			j = proba.index(mx_)
		#print(potential_diagnosis)
	return {"illness":potential_diagnosis[j][0],"probability":mx}
