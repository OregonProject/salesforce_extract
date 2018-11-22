""" Config.py file used to set Salesforce and SFTP variables """

# Dictionary of Salesforce credentials
salesforce = {
	"username": "",
	"password": "",
	"token": ""
}

# Dictionary of SFTP credentials
sftp = {
	"host": "",
	"username": "",
	"password": "",
	"hostkeys": "",
	"port": "22"
}

"""# Dictionary of Surefire API credentials
surefire_api ={
	"url": "https://apigateway.tomnx.com/sf3api/ip/uploader/jobs",
	"apikey": "",
	"clientkey": "",
	"mappingtag": "",
}"""

# Record Type Id's
record_type = {
	"contact_referral": "'Mortgage Partner'",
	"account_consumer": "'Consumer Customer'",
	"account_prospect": "'Consumer Prospect'",
	"opportunity_mortgage": "'Mortgage'",
	"opportunity_mortgage_origination": "'Mortgage Origination'",
	"lead_mortgage": "'Mortgage'",
	"bank_account_mortgage_origination": "'Mortgage Origination'",
	"bank_account_loan_account": "'Loan Account'",
}

# CSV headers
csv_header = ["Source","Contact Type","Loan Officer Email","ExternalId","First Name","Last Name","Email","Birthdate","Home Phone",
"Mobile Phone","Work Phone","Mailing Address 1","Mailing City","Mailing State","Mailing Zip","Contact Created Date","Loss Reason","ProductId",
"Loan Created Date","Product Name","Loan Purpose","Loan Type","Product Type",
"Loan Amount","Lien Position","Property Address","Interest Rate","Term","Mortgage_Status","Mortgage Date","App Received","Submitted to Underwriting", \
"Initial/Conditional Approval","Clear to Close","Funded Date","Denied","Withdrawn"]

# Index map for the milestones
milestone_index = {
	"Application Registration":30,
	"In Processing":30,
	"To Processing":30,
	"Submitted To Underwriting":31,
	"Received In Underwriting":31,
	"Approved With Conditions":32,
	"Final Approval Clear To Close":33,
	"Funded":34,
	"Denied":35,
	"Withdrawn":36,
	"Withdrawal Of Approved Loan":36
	}

# Index map for the milestones
milestone_mapping = {
   "Application Registration":"App Received",
   "In Processing":"App Received",
   "To Processing":"App Received",
   "Submitted To Underwriting":"Submitted to Underwriting",
   "Received In Underwriting":"Submitted to Underwriting",
   "Approved With Conditions":"Initial/Conditional Approval",
   "Final Approval Clear To Close":"Clear to Close",
   "Funded":"Funded",
   "Denied":"Denied",
   "Withdrawn":"Withdrawn",
   "Withdrawal Of Approved Loan":"Withdrawn",
   "Withdrawn By Applicant":"Withdrawn",
   "Cancelled For Incompleteness":"Denied",
   "Rescinded Loan":"Withdrawn",
   "Audit Denied":"Denied",
   "Funding Cancel":"Withdrawn",
   "Funding Voided":"Withdrawn"
   }
   
# List of milestone keys for filtering reference
milestone_keys = [
	"Application Registration",
	"In Processing",
	"To Processing",
	"Submitted To Underwriting",
	"Received In Underwriting",
	"Approved With Conditions",
	"Final Approval Clear To Close",
	"Funded",
	"Denied",
	"Withdrawn",
	"Withdrawal Of Approved Loan",
	"Withdrawn By Applicant",
	"Cancelled For Incompleteness",
	"Rescinded Loan",
	"Audit Denied",
	"Funding Cancel",
	"Funding Voided"
	]
