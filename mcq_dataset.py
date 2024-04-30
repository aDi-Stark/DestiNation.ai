import pandas as pd

# Define the data
data = {
    'Domain': ['Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Medical', 'Medical', 'Medical', 'Medical', 'Medical', 'Medical', 'Engineering', 'Engineering', 'Engineering', 'Medical', 'Medical', 'Medical'],
    'Subject': ['Computer Science', 'Computer Science', 'Computer Science', 'Electrical', 'Electrical', 'Electrical', 'Biology', 'Biology', 'Biology', 'Anatomy', 'Anatomy', 'Anatomy', 'Mechanical', 'Mechanical', 'Mechanical', 'Pharmacology', 'Pharmacology', 'Pharmacology'],
    'Question': [
        'What is the time complexity of a binary search algorithm?',
        'Which data structure uses FIFO principle?',
        'What does HTTP stand for?',
        'What is the unit of electrical resistance?',
        'Which law states that the current through a conductor between two points is directly proportional to the voltage across the two points?',
        'What is used to measure the electrical power?',
        'What is the powerhouse of the cell?',
        'What is the process by which plants make their food?',
        'Which blood cells are responsible for fighting infections?',
        'What part of the human body is the mandible?',
        'Which organ is responsible for detoxification?',
        'What is the largest organ of the human body?',
        'What is the study of fluids in motion?',
        'Which law explains the relationship between the pressure and volume of a gas at constant temperature?',
        'What is the unit of force?',
        'What is the study of drugs and their actions on the body?',
        'Which medication is used to treat bacterial infections?',
        'What is the term for a drug that relieves pain?'
    ],
    'OptionA': ['O(n)', 'Stack', 'HyperText Transfer Product', 'Ohm', 'Ohm\'s Law', 'Voltmeter', 'Ribosome', 'Photosynthesis', 'Red Blood Cells', 'Arm', 'Liver', 'Heart', 'Dynamics', 'Boyle\'s Law', 'Newton', 'Toxicology', 'Aspirin', 'Antipyretic'],
    'OptionB': ['O(log n)', 'Queue', 'HyperText Transfer Protocol', 'Volt', 'Faraday\'s Law', 'Ammeter', 'Mitochondria', 'Respiration', 'White Blood Cells', 'Leg', 'Kidney', 'Skin', 'Fluid Mechanics', 'Charles\'s Law', 'Joule', 'Pharmacology', 'Ibuprofen', 'Analgesic'],
    'OptionC': ['O(n^2)', 'Array', 'Hyper Transfer Protocol', 'Ampere', 'Maxwell\'s Law', 'Wattmeter', 'Nucleus', 'Transpiration', 'Platelets', 'Jaw', 'Heart', 'Liver', 'Thermodynamics', 'Avogadro\'s Law', 'Watt', 'Pathology', 'Amoxicillin', 'Antihistamine'],
    'OptionD': ['O(n log n)', 'LinkedList', 'HighText Transfer Protocol', 'Watt', 'Gauss\'s Law', 'Resistor', 'Chloroplast', 'Fermentation', 'Plasma Cells', 'Skull', 'Lungs', 'Kidney', 'Kinematics', 'Gay-Lussac\'s Law', 'Pascal', 'Biology', 'Acetaminophen', 'Antibiotic'],
    'CorrectOption': ['B', 'B', 'B', 'A', 'A', 'C', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'A', 'B', 'C', 'B']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'mcq_questions.csv'
df.to_csv(csv_file_path, index=False)

print(f'Dataset saved to {csv_file_path}')
