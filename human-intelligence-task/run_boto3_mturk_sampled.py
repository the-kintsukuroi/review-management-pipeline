import pandas
from boto3_mturk_aws import create_mturk_hit, get_results_mturk_hit

sampled_reviews = pandas.read_csv("sampled_reviews.csv", error_bad_lines=False, engine="python")

question_file = open("sampled_questions.xml", "r").read()
for i in range(0,5):
    xml = question_file.format(question=sampled_reviews['Reviews'][i])
    create_mturk_hit(xml)

hit_ids = ['3QQUBC640H6MFQPPVWV81KA00O4XNR','33KGGVH25X9J1JI0Q9XA4DXXXN01XO', '35YHTYFL2JVIN97DXTBD5U46IMAVFF','31HLTCK4CONO19388DHVNF4IJ1AVGE', '3QQUBC640H6MFQPPVWV81KA00O4XNR','33KGGVH25X9J1JI0Q9XA4DXXXN01XO', '35YHTYFL2JVIN97DXTBD5U46IMAVFF','31HLTCK4CONO19388DHVNF4IJ1AVGE', '3QQUBC640H6MFQPPVWV81KA00O4XNR','33KGGVH25X9J1JI0Q9XA4DXXXN01XO']
for hit_id in hit_ids:
    get_results_mturk_hit(hit_id)

'''Title = 'Offensive Review Detection',
Description = 'Read the review and identify offensive or not',
Keywords = 'labeling',
Reward = '0.15',
MaxAssignments = 3,
LifetimeInSeconds = 172800, #2days
AssignmentDurationInSeconds = 900, #15min
AutoApprovalDelayInSeconds = 14400, #4hrs'''

