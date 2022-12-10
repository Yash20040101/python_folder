sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
lowkey=sample_dict['C']

for i in sample_dict:
    if(lowkey>=sample_dict[i]):
        lowkey=sample_dict[i]
        j=i
print(j)
        
