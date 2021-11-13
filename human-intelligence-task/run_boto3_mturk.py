from boto3_mturk import create_mturk_hit

create_mturk_hit(xml_document_path='questions_1.xml') # 3421H3BMAD90V4G6DI1QFKOEV6I9J5 36GJS3V79YIFAE3ERO7071A1ZJDJG6
#create_mturk_hit(xml_document_path='questions_2.xml') # 3K8CQCU3LHT7QQKZLR3AMBD62RANWF
#create_mturk_hit(xml_document_path='questions_3.xml') # 3IJ95K7NE04BT4UZ6MZS08RI83LGNA
#create_mturk_hit(xml_document_path='questions_4.xml')  # 3XABXM4AK4XH3M193GFLCP5PPVX8QB

#get_results_mturk_hit(hit_id = '3BCRDCM0PGM8O5KQXWYQWPXPKSAK60')

'''Title = 'Fake Review Detection',
Description = 'Read the review and identify fake or real',
Keywords = 'labeling',
Reward = '0.15',
MaxAssignments = 3,
LifetimeInSeconds = 172800, #2days
AssignmentDurationInSeconds = 900, #15min
AutoApprovalDelayInSeconds = 14400, #4hrs'''