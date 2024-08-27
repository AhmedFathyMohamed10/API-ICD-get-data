import requests
import concurrent.futures


def fetch_disease_data(code, headers, url_template):
    url = f"{url_template}{code}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None


def fetch_diseases_by_codes(icd_codes):
    diseases = []
    api_key = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MjQ0MTY0MTIsImV4cCI6MTcyNDQyMDAxMiwiaXNzIjoiaHR0cHM6Ly9pY2RhY2Nlc3NtYW5hZ2VtZW50Lndoby5pbnQiLCJhdWQiOlsiaHR0cHM6Ly9pY2RhY2Nlc3NtYW5hZ2VtZW50Lndoby5pbnQvcmVzb3VyY2VzIiwiaWNkYXBpIl0sImNsaWVudF9pZCI6ImE5MDRlN2E1LTJmZjAtNGZmYS05MTU1LTA0OWNjNWNhZmRmYl8zOWEzZjVlNi01ZTk1LTRlYzktOWU1OC1iNDNiM2IxOGEzMTgiLCJzY29wZSI6WyJpY2RhcGlfYWNjZXNzIl19.w1eSG7jdV6u1aLyNekfSSOXTq998-Dp-fp1h5GQuswbMXE5kIYwzGAiKQ0jDbtKgaCZVSFKw_JUd2rB2fku5mwtqjxPwukTNNOhMEZdBSLlJ6Ruu1D8zbLWq86Gym1abAz8HL17-5j5NCkE6FoBUCxKNzKOvgHROvllWW_k4wv3vec-WN3Luowa2wIZ_vELbMJ5N_sjiBJ1VEJdJ3j5YUHN14G8S4wJAfcT9Tit9YU0GSlqkORbwMxGBuTwPfkjthZu42fgho05xp7dju79zVoETP87JtF5cOGTu9VL_Iibv4rDPEfcg6wYcw-VvgX1LITCyHIRTZpaEakNMlDSZcw'
    url_template = "https://id.who.int/icd/release/11/2021-05/mms/"
    headers = {
        "Accept": "application/json",
        "API-Version": "v2",
        "Accept-Language": "en",
        "Authorization": f"Bearer {api_key}"
    }
    

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Create a list of futures
        futures = [executor.submit(fetch_disease_data, code, headers, url_template) for code in icd_codes]

        # As each future completes, append the result to the diseases list
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                diseases.append(result)

    return diseases













# # def fetch_icd11_diseases():
# #     base_url = "https://id.who.int/icd/release/11/mms"
# #     api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE3MTY3OTEzMzEsImV4cCI6MTcxNjc5NDkzMSwiaXNzIjoiaHR0cHM6Ly9pY2RhY2Nlc3NtYW5hZ2VtZW50Lndoby5pbnQiLCJhdWQiOlsiaHR0cHM6Ly9pY2RhY2Nlc3NtYW5hZ2VtZW50Lndoby5pbnQvcmVzb3VyY2VzIiwiaWNkYXBpIl0sImNsaWVudF9pZCI6ImJkODRjYTc0LTUzMGEtNDdlNi1iN2FhLTI1YzA3MWI4YmY5ZV9iNjgxOTFiMS1mYjE2LTQyNTYtOGRkMS0xMGQ1YjQ1MDM0MjIiLCJzY29wZSI6WyJpY2RhcGlfYWNjZXNzIl19.VFyuj98dWTs4WQPbm9XzmfttEUhB30-K1HKGxTpKKkcww7PbjJrG84Bd9azNrISStrp-E_jp_JeOJamkECCYGTHZ_947xLfOyOdeFPvWqhtFx_STG87oxztIrcKhydbCUAkvzlzsbRjLohaWSLEuLXKPVlbn6igPnPpUhZpYvokJ01jYmQHwvrDv6LILpGjdtXqtpG30Zo02p2E6wfB3MxI0iJH5go-VL17jlROBe2jLNb1GFmd_bJtZCv-x1xvFpTQbZAPKyGVP389eyHH5er0ZwFoY1gdc875-JiZ93k_U72rnoXC0SGBo35hoD9shCLUNtvFK7xgWE4Spxah89g"  # Replace with your actual API key
# #     headers = {
# #         "Accept": "application/json",
# #         "API-Version": "v2" ,
# #         "Accept-Language": "ar" ,
# #         "Authorization": f"Bearer {api_key}"
# #     }