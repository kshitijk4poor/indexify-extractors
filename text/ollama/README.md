# Ollama Extractor

This is a Ollama based Extractor that supports multiple Ollama models. The extractor uses Llama3 by default, with ability to use other Ollamas as well and works on the Content of previous extractor as message, however we can manually overwrite prompt and message. We support any open source Ollama models from Hugging Face if you want to run locally.

### Example:
##### input:
```
prompt = """Extract information according to this schema and return json in this format {"Invoice No.": "", "Date": "", "Account Number": "", "Owner": "", "Property": "", "Address": "", "Registration Key": "", "Last Month Balance": "", "Current Amount Due": "", "Due Date": ""}:
    Axis\nSTATEMENTInvoice No. "Invoice No."\nDate: 4/19/2024\nAccount Number:\nOwner:\nProperty:"Account Number"\n"Owner"\n"Property"\n"Owner"\n"Property"\n"Address"SUMMARY OF ACCOUNT\nLast Month Balance:\nCurrent Amount Due:"Last Month Balance"\n"Current Amount Due"\nAccount details on back.\nProfessionally\nprepared by:\nSTATEMENT MESSAGE\nWelcome to Action Property Management! We are excited to be\nserving your community. Our Community Care team is more than\nhappy to assist you with any billing questions you may have. For\ncontact options, please visit www.actionlife.com/contact. Visit the\nAction Property Management web page at: www.actionlife.com.BILLING QUESTIONS\nScan the QR code to\ncontact our\nCommunity Care\nteam.\nactionlife.com/contact\nCommunityCare@actionlife.com\nRegister your Resident\nPortal account now!\nRegistration Key/ID:\n"Registration Key"\nresident.actionlife.com\nTo learn more about issues facing HOAs, say "Hey Siri, search the web for The Uncommon Area by Action Property Management."\nMake checks payable to:\nAxisAccount Number: "Account Number"\nOwner: "Owner"\nPLEASE REMIT PAYMENT TO:\n** AUTOPAY SCHEDULED **\n** NO REMITTANCE NECESSARY **CURRENT AMOUNT DUE\n"Current Amount Due"\nDUE DATE\n"Due Date"\n0049 00008330 0000922000203826 7 00065303 00000000 9"""

article = Content.from_text('Axis\nSTATEMENTInvoice No. 20240501-336593\nDate: 4/19/2024\nAccount Number:\nOwner:\nProperty:922000203826\nJohn Doe\n200 Park Avenue, Manhattan\nJohn Doe\n200 Park Avenue Manhattan\nNew York 10166SUMMARY OF ACCOUNT\nLast Month Balance:\nCurrent Amount Due:$653.03\n$653.03\nAccount details on back.\nProfessionally\nprepared by:\nSTATEMENT MESSAGE\nWelcome to Action Property Management! We are excited to be\nserving your community. Our Community Care team is more than\nhappy to assist you with any billing questions you may have. For\ncontact options, please visit www.actionlife.com/contact. Visit the\nAction Property Management web page at: www.actionlife.com.BILLING QUESTIONS\nScan the QR code to\ncontact our\nCommunity Care\nteam.\nactionlife.com/contact\nCommunityCare@actionlife.com\nRegister your Resident\nPortal account now!\nRegistration Key/ID:\nFLOWR2U\nresident.actionlife.com\nTo learn more about issues facing HOAs, say "Hey Siri, search the web for The Uncommon Area by Action Property Management."\nMake checks payable to:\nAxisAccount Number: 922000203826\nOwner: John Doe\nPLEASE REMIT PAYMENT TO:\n** AUTOPAY SCHEDULED **\n** NO REMITTANCE NECESSARY **CURRENT AMOUNT DUE\n$653.03\nDUE DATE\n5/1/2024\n0049 00008330 0000922000203826 7 00065303 00000000 9')

input_params = InputParams(system_prompt=prompt)

extractor = OllamaExtractor()
results = extractor.extract(article, params=input_params)
```

##### output:
```
[Content(content_type='text/plain', data=b'{\n    "Invoice No.": "20240501-336593",\n    "Date": "4/19/2024",\n    "Account Number": "922000203826",\n    "Owner": "John Doe",\n    "Property": "200 Park Avenue, Manhattan",\n    "Address": "200 Park Avenue Manhattan, New York 10166",\n    "Registration Key": "FLOWR2U",\n    "Last Month Balance": "$653.03",\n    "Current Amount Due": "$653.03",\n    "Due Date": "5/1/2024"\n}', features=[Feature(feature_type='metadata', name='text', value={'model': 'gpt-3.5-turbo-0125', 'completion_tokens': 120, 'prompt_tokens': 724}, comment=None)], labels={})]
```
