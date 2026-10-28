# import-diabetes-130-us-hospitals-for-years-1999-2008

Imports the UCI Diabetes 130-US Hospitals (1999–2008) dataset and its ID mappings into FL-Net.

This folder contains the **“Diabetes 130-US Hospitals for Years 1999–2008”** dataset from the UCI Machine Learning Repository.
The data covers ten years of clinical care for patients with diabetes at **130 U.S. hospitals and integrated delivery networks**. Each row is a single inpatient encounter (hospital admission) where diabetes was recorded as a diagnosis.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

The primary use case is to model **early hospital readmission** (within 30 days after discharge), but the dataset also supports a wide range of predictive and exploratory tasks.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

---

## 1. Dataset summary

- **Source:** UCI Machine Learning Repository – *“Diabetes 130-US Hospitals for Years 1999–2008”*  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Subject area:** Health and medicine (hospital care for diabetes)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Instances:** ~101,766 encounters (rows)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Features:** 47 feature columns (plus ID and target columns, depending on how you load the data)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Tasks:** Classification (e.g. readmission prediction), clustering (e.g. patient subgroups)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Data types:** Categorical and integer  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **Missing values:** Yes (several fields are either missing or encoded with placeholders)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

Each instance satisfies:  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

1. Inpatient encounter (hospital admission).
2. Diabetes recorded as a diagnosis.
3. Length of stay between 1 and 14 days.
4. At least one lab test performed.
5. At least one medication administered.

---

## 2. Files in this folder

- **`diabetic_data.csv`**
  Main dataset with one row per encounter. Contains:
  - Patient identifiers (encounter and patient IDs)
  - Demographics (race, gender, age group, weight)
  - Admission information (type, source, discharge disposition)
  - Hospital utilization (time in hospital, counts of previous encounters)
  - Diagnoses (ICD-9 codes in multiple fields)
  - Laboratory and medication-related features (e.g. HbA1c result, diabetes medications)
  - Outcome / target variables (including readmission within 30 days)

- **`IDS_mapping.csv`**
  Lookup table mapping integer-coded IDs (e.g. `admission_type_id`, `discharge_disposition_id`, `admission_source_id`) to human-readable categories (e.g. “Emergency”, “Elective”, “Discharged to home”).

> If you obtained the data via another source, file names may differ slightly – adjust this README accordingly.

---

## 3. Features (high-level overview)

The exact variable list is documented on the UCI page and in the accompanying paper.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
Broadly, the columns fall into these groups:

1. **Identifiers**
   - `encounter_id`, `patient_nbr`: technical IDs (not suitable as predictors).

2. **Demographics**
   - `race`, `gender`, `age`, `weight`.
   - Note: these are **sensitive attributes** and should be handled carefully in downstream analyses.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

3. **Admission / discharge info**
   - `admission_type_id`, `admission_source_id`, `discharge_disposition_id`.
   - Coded as integers; use `IDS_mapping.csv` to decode.

4. **Hospital stay & utilization**
   - `time_in_hospital`: length of stay in days.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)
   - Counts of outpatient, emergency, and inpatient visits in the prior year.
   - Number of lab procedures, number of medications, number of diagnoses.

5. **Diagnoses**
   - Up to three diagnosis codes per encounter (ICD-9 style).

6. **Lab results**
   - e.g. HbA1c and maximum serum glucose, usually in coarse categories (e.g. “>200”, “>300” rather than raw values).

7. **Medications**
   - Binary/ordinal indicators for multiple diabetes-related drugs and whether treatment changed during the stay.

8. **Target / outcome**
   - Readmission within 30 days after discharge (commonly used as the main prediction target in the literature).
   - Additional hospital outcome aspects can also be modelled (e.g. length of stay, multiple readmissions, etc.).

For detailed variable definitions, see the *Variables Table* on the UCI page and Table 1 of the introductory paper by Strack et al.  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

---

## 4. Typical machine learning use cases

- **Binary / multiclass classification**
  - Predict early readmission (≤30 days) vs. later/no readmission.
  - Predict high-risk vs. low-risk patients based on utilization profiles.

- **Clustering / subgroup discovery**
  - Identify clinically meaningful patient clusters (e.g. by comorbidities, treatment regimens, or readmission patterns).  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

- **Outcome & resource modelling**
  - Explore relationships between HbA1c testing, medication changes, and readmission rates (as in the original paper).
  - Model length of stay or number of prior visits as outcomes.

---

## 5. Preprocessing notes

When working with this dataset, you will typically need to:

1. **Handle missing values**
   - Several fields contain missing values (sometimes represented by special tokens such as `"?"`).  [UCI dataset](https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us%2Bhospitals%2Bfor%2Byears%2B1999-2008)

2. **Decode ID fields**
   - Join `diabetic_data.csv` with `IDS_mapping.csv` to obtain readable admission/discharge categories.

3. **Encode categorical variables**
   - Most features are categorical; use one-hot encoding, target encoding, or embeddings depending on the model.

4. **Define a clear target**
   - Decide on the exact definition of “readmitted” (e.g. `<30 days` vs. `NO / >30 days`) and create a label accordingly, to match your research question.

5. **Consider patient-level vs. encounter-level analysis**
   - The same `patient_nbr` can appear multiple times (multiple encounters). Think about whether you:
     - Train at **encounter level** (most common), or
     - Aggregate encounters to **patient level**, or
     - Split train/validation/test such that encounters from the same patient do not leak across splits.

6. **Ethical & fairness considerations**
   - Demographic fields (race, age, gender) are available; evaluate and report potential biases if you use them to make predictions.

---

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs in .env before connecting.
python main.py
```

The Docker base image provides the FL-Net API; `requirements.txt` lists only additional runtime dependencies.

Build the container with `docker build -t tool-import-diabetes-130-us-hospitals-for-years-1999-2008 .`.
