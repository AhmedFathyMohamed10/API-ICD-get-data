from django.http import JsonResponse
from .utils import fetch_diseases_by_codes
import json
import os
import ijson
from multiprocessing import Pool

file_path = './response.json'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def get_diseases(request):
    # Assuming the codes are passed as a JSON array in the request body
    icd_codes = [
        '1799393163'
    ]
    
    if not icd_codes:
        return JsonResponse({"status":  "ICD-11 codes array is empty"})

    # Example function call to fetch diseases by codes (you need to implement this)
    diseases = fetch_diseases_by_codes(icd_codes)
    
  
    # Save the data to a JSON file

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(diseases, f, ensure_ascii=False, indent=4)

    return JsonResponse({"data": "success"})    



# Function to retain only specific fields
# def retain_fields(request):
#     data = [
#     {
#       "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
#       "@id": "http://id.who.int/icd/release/11/2021-05/mms/1435254666",
#       "parent": [
#           "http://id.who.int/icd/release/11/2021-05/mms"
#       ],
#       "child": [
#           "http://id.who.int/icd/release/11/2021-05/mms/588616678",
#           "http://id.who.int/icd/release/11/2021-05/mms/1904876434",
#           "http://id.who.int/icd/release/11/2021-05/mms/979278646",
#           "http://id.who.int/icd/release/11/2021-05/mms/1539889147",
#           "http://id.who.int/icd/release/11/2021-05/mms/1412960686",
#           "http://id.who.int/icd/release/11/2021-05/mms/1935092859",
#           "http://id.who.int/icd/release/11/2021-05/mms/487269828",
#           "http://id.who.int/icd/release/11/2021-05/mms/1000704511",
#           "http://id.who.int/icd/release/11/2021-05/mms/1104303944",
#           "http://id.who.int/icd/release/11/2021-05/mms/1585949804",
#           "http://id.who.int/icd/release/11/2021-05/mms/1959883044",
#           "http://id.who.int/icd/release/11/2021-05/mms/921595235",
#           "http://id.who.int/icd/release/11/2021-05/mms/1251496839",
#           "http://id.who.int/icd/release/11/2021-05/mms/1136802325",
#           "http://id.who.int/icd/release/11/2021-05/mms/145723401",
#           "http://id.who.int/icd/release/11/2021-05/mms/985510409",
#           "http://id.who.int/icd/release/11/2021-05/mms/1646490591",
#           "http://id.who.int/icd/release/11/2021-05/mms/1939815950",
#           "http://id.who.int/icd/release/11/2021-05/mms/255141529",
#           "http://id.who.int/icd/release/11/2021-05/mms/293771399",
#           "http://id.who.int/icd/release/11/2021-05/mms/1760597414",
#           "http://id.who.int/icd/release/11/2021-05/mms/458687859",
#           "http://id.who.int/icd/release/11/2021-05/mms/1435254666/unspecified"
#       ],
#       "browserUrl": "https://icd.who.int/browse/2021-05/mms/ar#1435254666",
#       "code": "01",
#       "source": "http://id.who.int/icd/entity/1435254666",
#       "classKind": "chapter",
#       "foundationChildElsewhere": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "عداوى لدى الجنين أو لدى الوليد"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/911707612",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/911707612"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "أمراض سببها البريون لدى البشر"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1965146397",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/1965146397"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التهاب الرئة"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/142052508",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/142052508"
#           }
#       ],
#       "title": {
#           "@language": "ar",
#           "@value": "بعض الأمراض المُعْدِيَة (العَدْوائيَّة) أو الطُفَيلِيَّة"
#       },
#       "definition": {
#           "@language": "ar",
#           "@value": "يتضمن هذا الفصل بعض الحالات التي تسببها الكائنات الحية المسببة للأمراض أو الكائنات الحية الدقيقة (المكروأورغانيزم)، مثل البكتيريا أو الفيروسات أو الطفيليات أو الفطريات."
#       },
#       "exclusion": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "عدوى نشأت من أداة أو غرسة أو طُعم، لم يتم تصنيفها في مكان آخر"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1612485599",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/1612485599"
#           }
#       ]
#   },
#   {
#       "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
#       "@id": "http://id.who.int/icd/release/11/2021-05/mms/588616678",
#       "parent": [
#           "http://id.who.int/icd/release/11/2021-05/mms/1435254666"
#       ],
#       "child": [
#           "http://id.who.int/icd/release/11/2021-05/mms/135352227",
#           "http://id.who.int/icd/release/11/2021-05/mms/1834648119",
#           "http://id.who.int/icd/release/11/2021-05/mms/30738976",
#           "http://id.who.int/icd/release/11/2021-05/mms/2092703582",
#           "http://id.who.int/icd/release/11/2021-05/mms/1688127370"
#       ],
#       "browserUrl": "https://icd.who.int/browse/2021-05/mms/ar#588616678",
#       "code": "",
#       "source": "http://id.who.int/icd/entity/588616678",
#       "classKind": "block",
#       "blockId": "BlockL1-1A0",
#       "codeRange": "1A00-1A40.Z",
#       "foundationChildElsewhere": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "عداوى الأمعاء الناجمة عن الفطريات"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/730271848",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/730271848"
#           }
#       ],
#       "title": {
#           "@language": "ar",
#           "@value": "التِهابات المَعِدَةِ والأَمْعاءِ أو القولون من منشأ عَدْوائِيّ"
#       }
#   },
#   {
#       "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
#       "@id": "http://id.who.int/icd/release/11/2021-05/mms/135352227",
#       "parent": [
#           "http://id.who.int/icd/release/11/2021-05/mms/588616678"
#       ],
#       "child": [
#           "http://id.who.int/icd/release/11/2021-05/mms/257068234",
#           "http://id.who.int/icd/release/11/2021-05/mms/416025325",
#           "http://id.who.int/icd/release/11/2021-05/mms/2080365623",
#           "http://id.who.int/icd/release/11/2021-05/mms/344162786",
#           "http://id.who.int/icd/release/11/2021-05/mms/250688797",
#           "http://id.who.int/icd/release/11/2021-05/mms/1000894786",
#           "http://id.who.int/icd/release/11/2021-05/mms/794462570",
#           "http://id.who.int/icd/release/11/2021-05/mms/1528414070",
#           "http://id.who.int/icd/release/11/2021-05/mms/1780040028",
#           "http://id.who.int/icd/release/11/2021-05/mms/515117475",
#           "http://id.who.int/icd/release/11/2021-05/mms/135352227/other",
#           "http://id.who.int/icd/release/11/2021-05/mms/135352227/unspecified"
#       ],
#       "browserUrl": "https://icd.who.int/browse/2021-05/mms/ar#135352227",
#       "code": "",
#       "source": "http://id.who.int/icd/entity/135352227",
#       "classKind": "block",
#       "blockId": "BlockL2-1A0",
#       "codeRange": "1A00-1A0Z",
#       "foundationChildElsewhere": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "داءُ الشُعِّيات البطنيّ"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/2143116824",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/2143116824"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التهاب المعدة والأمعاء بالليستيريات"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/974967764",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/419706488/other"
#           }
#       ],
#       "title": {
#           "@language": "ar",
#           "@value": "عَداوى مِعَويّة جرثوميَّة [بكتيريَّة]"
#       },
#       "definition": {
#           "@language": "ar",
#           "@value": "أي حالة من حالات التهاب الأمعاء تسببها عدوى منشؤها الجراثيم."
#       },
#       "exclusion": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التَسَمُّم الجرثومي المنقول بالغذاء"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1834648119",
#               "linearizationReference": "http://id.who.int/icd/release/11/2021-05/mms/1834648119"
#           }
#       ]
#   },
#   {
#       "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
#       "@id": "http://id.who.int/icd/release/11/2021-05/mms/257068234",
#       "parent": [
#           "http://id.who.int/icd/release/11/2021-05/mms/135352227"
#       ],
#       "browserUrl": "https://icd.who.int/browse/2021-05/mms/ar#257068234",
#       "code": "1A00",
#       "source": "http://id.who.int/icd/entity/257068234",
#       "classKind": "category",
#       "postcoordinationScale": [
#           {
#               "@id": "http://id.who.int/icd/release/11/2021-05/mms/257068234/postcoordinationScale/infectiousAgent",
#               "axisName": "http://id.who.int/icd/schema/infectiousAgent",
#               "requiredPostcoordination": "false",
#               "allowMultipleValues": "AllowAlways",
#               "scaleEntity": [
#                   "http://id.who.int/icd/release/11/2021-05/mms/824826401"
#               ]
#           },
#           {
#               "@id": "http://id.who.int/icd/release/11/2021-05/mms/257068234/postcoordinationScale/associatedWith",
#               "axisName": "http://id.who.int/icd/schema/associatedWith",
#               "requiredPostcoordination": "false",
#               "allowMultipleValues": "AllowAlways",
#               "scaleEntity": [
#                   "http://id.who.int/icd/release/11/2021-05/mms/1215034670",
#                   "http://id.who.int/icd/release/11/2021-05/mms/1839638766",
#                   "http://id.who.int/icd/release/11/2021-05/mms/501791005",
#                   "http://id.who.int/icd/release/11/2021-05/mms/1975056531",
#                   "http://id.who.int/icd/release/11/2021-05/mms/828922344",
#                   "http://id.who.int/icd/release/11/2021-05/mms/174465822",
#                   "http://id.who.int/icd/release/11/2021-05/mms/612672352",
#                   "http://id.who.int/icd/release/11/2021-05/mms/1882742628/other",
#                   "http://id.who.int/icd/release/11/2021-05/mms/1882742628/unspecified"
#               ]
#           }
#       ],
#       "title": {
#           "@language": "ar",
#           "@value": "الكُوليرا"
#       },
#       "inclusion": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "متلازمة الكوليرا"
#               }
#           }
#       ],
#       "fullySpecifiedName": {
#           "@language": "ar",
#           "@value": "Intestinal infection due to Vibrio cholerae [No translation available]"
#       },
#       "indexTerm": [
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكُوليرا"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الآسيويَّة"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الوبائيّة"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "متلازمة الكوليرا"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الهَيْضَة"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "Intestinal infection due to Vibrio cholerae [No translation available]"
#               }
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التهاب أمعاء ناجم عن الكوليرا الناجمة عن ضمات الكوليرا، من ذريات غير O1"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1170831944"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا غير O1"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1170831944"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا ناجمة عن ضمَّات الكوليرا O1 ، الضرب البيولوجيّ كوليرا"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1205958647"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الكلاسيكيَّة"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1205958647"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا التقليديَّة"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1205958647"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التِهابُ الأَمْعاء الناجم عن الكوليرا الناجمة عن ضمَّات الكوليرا O1 ، الضرب البيولوجيّ كوليرا"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1384028266"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التهاب الأمعاء الناجم عن الكوليرا الكلاسيكية"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1384028266"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا التقليدية"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/1384028266"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا ناجمة عن ضمَّات الكوليرا O1 ، الضرب البيولوجيّ الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/581614179"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الناجمة عن ضمَّات الكوليرا O1 ، الضرب البيولوجيّ الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/581614179"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الناجمة عن ضمَّات الكوليرا O1 ، الضرب البيولوجيّ الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/581614179"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "الكوليرا الناجمة عن ضمَّات كوليرا الطور."
#               },
#               "foundationReference": "http://id.who.int/icd/entity/581614179"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/581614179"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التِهابُ أَمْعاء ناجم عن كوليرا ناجمة عن ضمَّات الكوليرا 01 ، الضرب البيولوجيّ الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/375406584"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التِهابُ الأَمْعاء الناجم عن ضمَّات كوليرا الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/375406584"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "التِهابُ الأَمْعاء بجراثيم الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/375406584"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا الطور"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/375406584"
#           },
#           {
#               "label": {
#                   "@language": "ar",
#                   "@value": "كوليرا طُورية"
#               },
#               "foundationReference": "http://id.who.int/icd/entity/375406584"
#           }
#       ]
#   },
# ]
#     filtered_data = []
#     for item in data:
#         filtered_item = {
#             "code": item.get("code"),
#             "title": item.get("title"),
#             "definition": item.get("definition"),
#             "indexTerm": item.get("indexTerm")
            
#         }
#         filtered_data.append(filtered_item)
#     return JsonResponse({"data": filtered_data})    
# Apply the function

def process_item(item):
    return {
        "code": item.get("code"),
        "title": item.get("title"),
        "definition": item.get("definition"),
        "indexTerm": item.get("indexTerm")
    }

def stream_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        objects = ijson.items(f, 'item')
        for obj in objects:
            yield process_item(obj)


# Function to retain fields and save to a new file (serial processing)
def retain_fields(file_path, output_path):
    filtered_data = list(stream_json(file_path))
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump({"data": filtered_data}, output_file, ensure_ascii=False, indent=4)
    return JsonResponse({"message": "Processing completed successfully."})

# Function to retain fields and save to a new file (parallel processing)
def retain_fields_parallel(file_path, output_path):
    with Pool() as pool:
        with open(file_path, 'r', encoding='utf-8') as f:
            objects = ijson.items(f, 'item')
            filtered_data = pool.map(process_item, objects)

    # Write the filtered data to the new JSON file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump({"data": filtered_data}, output_file, ensure_ascii=False, indent=4)
    
    return JsonResponse({"message": "Processing completed successfully."})

file_path = os.path.join(BASE_DIR, 'test.json')
output_path = os.path.join(BASE_DIR, 'icd-results.json')
response = retain_fields_parallel(file_path, output_path)


# import pandas as pd
# Function to retain only specific fields
# def retain_fields(data):
#     filtered_data = []
#     for item in data:
#         filtered_item = {
#             "code": item.get("code"),
#             "title": item.get("title"),
#             "definition": item.get("definition")
#         }
#         filtered_data.append(filtered_item)
#     return filtered_data

# # Apply the function
# filtered_data = retain_fields(data)

# # Convert the filtered data to a DataFrame
# df = pd.DataFrame(filtered_data)

# # Save the DataFrame to an Excel file
# file_path = 'filtered_data.xlsx'
# df.to_excel(file_path, index=False)
