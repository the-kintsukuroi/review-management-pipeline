# Title, Description and Keywords - Keywords improve discoverability of your HIT(Human Intelligence Task)
# Reward - what you will pay a Worker (it does not include fees paid to MTurk)
# MaxAssignments - how many Workers you want to work on this single HIT
# LifetimeInSeconds - how long you want the HIT to be available on the marketplace
# AssignmentDurationInSeconds - how much time a Worker will have to complete the HIT once they start 
# AutoApprovalDelayInSeconds - how long a Worker’s assignment will get automatically approved if you do not explicitly approve or reject it. Default is 2 days
# Question - a string of HTML or XML content you specify to define what the layout looks like

    #Q1
    '''I have $20.00 in my Sandbox account
    A new HIT has been created. You can preview it here:
    https://worker.mturk.com/mturk/preview?groupId= 3J26SAFG0V5N9Z6YDA77LRU2JTJ0I6
    HITID = 3IKMEYR0MZNK641PAUMN6CGD4N8K2J (Use to Get Results)'''

    #Q2
    '''I have $19.46 in my Sandbox account
    A new HIT has been created. You can preview it here:
    https://worker.mturk.com/mturk/preview?groupId= 3J26SAFG0V5N9Z6YDA77LRU2JTJ0I6
    HITID = 3W0XM68Y0SNDHJJTRQM91T68CHU1KJ (Use to Get Results)'''

    #Q3
    '''I have $18.92 in my Sandbox account
    A new HIT has been created. You can preview it here:
    https://worker.mturk.com/mturk/preview?groupId= 3J26SAFG0V5N9Z6YDA77LRU2JTJ0I6
    HITID = 3JTPR5MT0V4C51KCSDOL4JJPOXZK5K (Use to Get Results)'''

    #Q4
    '''I have $18.38 in my Sandbox account
    A new HIT has been created. You can preview it here:
    https://worker.mturk.com/mturk/preview?groupId= 3J26SAFG0V5N9Z6YDA77LRU2JTJ0I6
    HITID = 3BCRDCM0PGM8O5KQXWYQWPXPKSAK60 (Use to Get Results)'''

# Use the hit_id previously created
hit_id = '3W0XM68Y0SNDHJJTRQM91T68CHU1KJ'

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
        
# Copyright 2017 Amazon.com, Inc. or its affiliates

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.