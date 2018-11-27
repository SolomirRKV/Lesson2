list_grade = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,3,4,5,2,2]},
    {'school_class': '4c', 'scores': [3,2,3,5,5]},
    {'school_class': '1a', 'scores': [3,1,2,5,2]},
    {'school_class': '2a', 'scores': [3,4,1,5,5,4]},
    {'school_class': '3b', 'scores': [3,4,0,3,2]},
    {'school_class': '5a', 'scores': [3,4,1,2,2,4,4,4]},
]
avg_class_score = 0
class_score_counter = 0
avg_sch_score = 0
school_class_cntr = 0
for class_dict in list_grade:
    #print(class_dict)
    #print(class_dict['scores'])
    for now_class_score in class_dict['scores']:
        avg_class_score += now_class_score
        class_score_counter += 1
    print(f'Average score grade for {class_dict["school_class"]} is {avg_class_score/class_score_counter}')
    avg_sch_score += (avg_class_score/class_score_counter)
    school_class_cntr +=1
    
    avg_class_score = 0
    class_score_counter = 0
print(f'AVERAGE SCHOOL SCORES: {avg_sch_score/school_class_cntr}')



