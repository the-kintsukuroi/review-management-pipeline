import pandas
from boto3_mturk_aws import create_mturk_hit

sampled_reviews = pandas.read_csv("sampled_reviews.csv", error_bad_lines=False, engine="python")
print(sampled_reviews)

#create_mturk_hit(xml_document_path='questions_1.xml')
#get_results_mturk_hit(hit_id = '3BCRDCM0PGM8O5KQXWYQWPXPKSAK60')
def create_question_xml():
    question_file = open("sampled_questions.xml", "r").read()
    xml = question_file.format(question=sampled_reviews['Reviews'][0])
    return xml

xml = create_question_xml()
#create_mturk_hit(xml)

'''Title = 'Offensive Review Detection',
Description = 'Read the review and identify offensive or not',
Keywords = 'labeling',
Reward = '0.15',
MaxAssignments = 3,
LifetimeInSeconds = 172800, #2days
AssignmentDurationInSeconds = 900, #15min
AutoApprovalDelayInSeconds = 14400, #4hrs'''

