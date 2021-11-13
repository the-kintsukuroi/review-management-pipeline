from boto.mturk.question import Question
import boto3
import xmltodict     # to help parse the XML answers supplied from MTurk
import csv

def create_mturk_hit(xml_documnet_path):
    sandbox = input('Do you want to Test(False) or Deploy(True)?')
    if sandbox == "True":
        MTURK_SANDBOX = 'https://mturk-requester.us-east-1.amazonaws.com'
    if sandbox == "False":
        MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
    mturk = boto3.client('mturk',
    endpoint_url = MTURK_SANDBOX
    )
    print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account")
    #question=(xml_documnet_path)
    question = open(file=xml_documnet_path,mode='r').read() # change the xml document for changing tasks
    Title = input('Enter Title for Mturk HIT:')
    Description = input('Enter description for Mturk HIT:')
    Keywords = input('Enter Keywords for Mturk HIT:')
    Reward = input(int('Enter Reward value for Mturk HIT:'))
    MaxAssignments = input(int('Enter MaxAssignments value for Mturk HIT:'))
    LifetimeInSeconds = input(int('Enter LifetimeInSeconds value for Mturk HIT:'))
    AssignmentDurationInSeconds = input(int('Enter AssignmentDurationInSeconds value for Mturk HIT:'))
    AutoApprovalDelayInSeconds = input(int('Enter AutoApprovalDelayInSeconds value for Mturk HIT:'))
    
    new_hit = mturk.create_hit(
        Title = Title,
        Description = Description,
        Keywords = Keywords,
        Reward = Reward,
        MaxAssignments = MaxAssignments,
        LifetimeInSeconds = LifetimeInSeconds,
        AssignmentDurationInSeconds = AssignmentDurationInSeconds,
        AutoApprovalDelayInSeconds = AutoApprovalDelayInSeconds,
        Question = question,
    )
    print("A new HIT has been created. You can preview it here:")
    print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId']) #change to deploy
    print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")

    # HITs to the live marketplace.
    # Use: https://worker.mturk.com/mturk/preview?groupId= for live marketplace
    # https://workersandbox.mturk.com/mturk/preview?groupId= for testing

    # MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com' for testing
    # MTURK_SANDBOX = 'https://mturk-requester.us-east-1.amazonaws.com' for live marketplace

def get_result_mturk_hit(hit_id):
    MTURK_SANDBOX = 'https://mturk-requester.us-east-1.amazonaws.com'
    mturk = boto3.client('mturk', endpoint_url = MTURK_SANDBOX)
    print("I have $" + mturk.get_account_balance()['AvailableBalance'] + " in my Sandbox account")
    worker_results= mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])
    if worker_results['NumResults'] > 0:
        for assignment in worker_results['Assignments']:
            xml_doc = xmltodict.parse(assignment['Answer'])
            print("Worker's answer was:")
            if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
                # Multiple fields in HIT layout
                for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
                    print ("For input field: ") + answer_field['QuestionIdentifier']
                    print ("Submitted answer: ") + answer_field['FreeText']
            else:
                # One field found in HIT layout
                print ("For input field: ") + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier']
                print ("Submitted answer: ") + xml_doc['QuestionFormAnswers']['Answer']['FreeText']
    
        with open('results.csv', 'w') as f:
            for key in xml_doc.keys():
                f.write("%s,%s\n"%(key,xml_doc[key]))

    else:
        print( "No results ready yet")
