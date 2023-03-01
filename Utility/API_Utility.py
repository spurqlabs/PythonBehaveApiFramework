import json
import requests


class API_Utility:
    data = json.load(open("Resources/config.json"))
    api_url = data["APIURL"]
    global response

    def Method_Call(self, table, method, endpoint):
        if method == 'GET':
            uri = self.api_url + endpoint
            response = requests.request("GET", uri)
            return response
        if method == 'POST':
            uri = self.api_url + endpoint
            payload = {
                "name": table[0][0],
                "job": table[0][1]
            }
            response = requests.request("POST", uri, data=payload)
            return response
        if method == 'PUT':
            uri = self.api_url + endpoint
            reqbody = {
                "Name": table[0][0],
                "Job": table[0][1]
            }
            response = requests.request("PUT", uri, data=reqbody)
            return response

    def Get_Status_Code(self):
        status_code = response.status_code
        return status_code

    def Verify_GET(self, table):
        for row in table:
            first_name = row['First_name']
            last_name = row['Last_name']
            email = row['Mail-id']
            return first_name, last_name, email

    def Verify_POST(self, table):
        for row in table:
            name = row['Name']
            job = row['Job']
            return name, job

    def Verify_PUT(self, table):
        for row in table:
            name = row['Name']
            job = row['Job']
            return name, job

    def Delete_Call(self, endpoint):
        uri = self.api_url + endpoint
        response = requests.request("DELETE", uri)
        return response
