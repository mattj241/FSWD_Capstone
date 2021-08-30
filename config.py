import os

def init_env_vars():
    os.environ['DB_USER'] = 'postgres'
    os.environ['DB_PASSWORD'] = 'marshall'
    # os.environ['TEST_DB_NAME'] = 'car_rental_test'
    os.environ['DB_NAME'] = 'car_rental'
    os.environ['MANAGER_TOKEN'] = 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFOZDFNWk5pWWs2WUIzWjZscGJVRCJ9.eyJpc3MiOiJodHRwczovL21hdHRqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDQwNzQzMjQ4NDE0MTE0NzkzNyIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjMwMjk3ODExLCJleHAiOjE2MzAzODQyMTEsImF6cCI6Ik5hd2xXVG1FQlhubG15RmJwNDVOQ3ZBT0o0a2Y0Q3pJIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6Y3VzdG9tZXIiLCJhZGQ6ZW1wbG95ZWUiLCJhZGQ6bWFuYWdlciIsImFkZDpyZXNlcnZhdGlvbiIsImFkZDp2ZWhpY2xlIiwiZGVsZXRlOnZlaGljbGUiLCJnZXQ6Y3VzdG9tZXIiLCJnZXQ6ZW1wbG95ZWUiLCJnZXQ6bWFuYWdlciIsImdldDpyZXNlcnZhdGlvbiIsInVwZGF0ZTpjdXN0b21lciIsInVwZGF0ZTplbXBsb3llZSIsInVwZGF0ZTptYW5hZ2VyIiwidXBkYXRlOnJlc2VydmF0aW9uIiwidXBkYXRlOnZlaGljbGUiXX0.W2vq7cyO17aqk4B5RE6TIWxIZJszy6HV_JdgjFClWbYbki98MFu9-IgVjk6VyBQdjf5JX67N1g7_lRlhoiY8PNB89ayUL_kLK9X_FkUA3cjexFoLR2xRsnJtpnMgvnc0Kj1V2ZxiLIXvzwmU6Pv2fItyEXd2hcxTLUFMsUM5_0UnpVS6ZnKlXWL6pmlrLaKADcSS80j5ixCxMnxCX3bb_uDi5QvjwnlhYBqAuZi-gB_gn5ZVDxbfo0UzQOiI_j2OCpomCBGdpqFyjVVJIRpQK1VnEFzAlK2IyOzdutqbXlS9aD3ntxg0oo5CBiXJJBxLMt5USs1dSXwZs425somc7g'
    os.environ['EMPLOYEE_TOKEN'] = 'Bearer ' + ' eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFOZDFNWk5pWWs2WUIzWjZscGJVRCJ9.eyJpc3MiOiJodHRwczovL21hdHRqLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MGU5YzhlMDQ4NGVhNjAwNzA1OWY0MjYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYzMDI5Nzc2OCwiZXhwIjoxNjMwMzg0MTY4LCJhenAiOiJOYXdsV1RtRUJYbmxteUZicDQ1TkN2QU9KNGtmNEN6SSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmN1c3RvbWVyIiwiYWRkOnJlc2VydmF0aW9uIiwiZ2V0OmN1c3RvbWVyIiwiZ2V0OmVtcGxveWVlIiwiZ2V0Om1hbmFnZXIiLCJnZXQ6cmVzZXJ2YXRpb24iLCJ1cGRhdGU6Y3VzdG9tZXIiLCJ1cGRhdGU6ZW1wbG95ZWUiLCJ1cGRhdGU6cmVzZXJ2YXRpb24iXX0.bx3nj4DpciD4xrETV4qRRTPKiZZPYm-8CZkRoSqOHHOYB2YhwquemMVKTxcGx2xk-HNrLABIrmUqtW_euTo3Kpis9GH-bVm4vx_ISyjIZsKGmuRi0_WLBhw06KFFxUfXcj2XFBlr9NZZD6yUSSh0oCp-Ewm7KSZIVWjbzDBd8ifCpUq8pa54DCA8I1v-92YDpnMSF8DUql1d6u-qJvF9Ls0RXf9vOTr5JsdrFjswnehz4LODOurmYg3Hd5Bou6c3Ask84WRof4MYQfERU59DBMe-LsthghGjzy4QjrCdylzYGB5DtJTbTl1K3ZV_2VVi9URVzeghISUdf0j35Avt3A'
