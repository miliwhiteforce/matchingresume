import django
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from .models import Candidates
from . import serializers
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from rest_framework.parsers import MultiPartParser
cv = CountVectorizer()
from urllib.request import urlopen
import ssl
import json

class TotalMatch(APIView):
    parser_classes = [MultiPartParser] 
    def get(self,request,pk,text):
        url = "https://happiestresume.com/api/job-description/{text}/{pk}".format(text=text,pk=pk)
        context = ssl._create_unverified_context()
        response = urlopen(url,context=context)
        data_json = json.loads(response.read())
        result = []
        candidate_data = Candidates.objects.all() # here
        candidate_serializer = serializers.CandidatesSerializer(candidate_data, many=True)
        candidate_edu_serializer = serializers.CandidatesEduSerializer(candidate_data, many=True)
        candidate_skill_serializer = serializers.CandidatesSkillSerializer(candidate_data, many=True)
        candidate_exp_serializer = serializers.CandidatesExpSerializer(candidate_data, many=True)
        candidate_title_serializer = serializers.CandidatesTitleSerializer(candidate_data,many=True)
        candidate_location_serializer = serializers.CandidatesLocationSerializer(candidate_data,many=True)
        candidate_industry_serializer = serializers.CandidatesindustrySerializer(candidate_data,many=True)
        candidate_data_serializer = serializers.CandidatesDataSerializer(candidate_data,many=True)
        show_record = candidate_data_serializer.data
        candidate_record = candidate_serializer.data 
        edu_record = candidate_edu_serializer.data 
        skill_record = candidate_skill_serializer.data
        exp_record = candidate_exp_serializer.data
        title_record = candidate_title_serializer.data
        location_record = candidate_location_serializer.data
        industry_record = candidate_industry_serializer.data
        jd_data = data_json
        jd_edu = data_json["data"]["education_required"]
        jd_skill = data_json["data"]["skills_required"],data_json["data"]["job_description"]
        jd_exp = data_json['data']['experience_year_from'],data_json['data']['experience_year_to']
        jd_position = data_json["data"]["position"]
        jd_location = data_json["data"]["job_location"]
        jd_industry = data_json["data"]["industry_type"]
        for i in range(3000):#len(candidate_data)
            candidate = show_record[i]
            candidate_resume = str((candidate_record)[i])
            edu_resume = str((edu_record)[i])
            skill_resume = str((skill_record)[i])
            exp_resume = str((exp_record)[i])
            title_resume = str((title_record)[i])
            location_resume = str((location_record)[i])
            industry_resume = str((industry_record)[i])
            a = edu_record[i]["id"] # here
            jd = str(jd_data)
            edu = str(jd_edu)
            skill = str(jd_skill)
            exp = str(jd_exp)
            position_name = str(jd_position)
            location = str(jd_location)
            industry = str(jd_industry)
            data_list = [candidate_resume, jd]
            edu_list = [edu_resume, edu]
            skill_list = [skill_resume,skill]
            exp_list = [exp_resume,exp]
            position_list = [title_resume,position_name]
            location_list = [location_resume,location]
            industry_list = [industry_resume,industry]
            count_data = cv.fit_transform(data_list)
            count_edu = cv.fit_transform(edu_list)
            count_skill = cv.fit_transform(skill_list)
            count_exp = cv.fit_transform(exp_list)
            count_position = cv.fit_transform(position_list)
            count_location = cv.fit_transform(location_list)
            count_industry = cv.fit_transform(industry_list)
            matchPercentage = cosine_similarity(count_data)[0][1] * 100
            matchPercentage = round(matchPercentage) # round to two decimal
            matchEduPercentage = cosine_similarity(count_edu)[0][1] * 100
            matchEduPercentage = round(matchEduPercentage) # round to two decimal

            matchSkillPercentage = cosine_similarity(count_skill)[0][1] * 100
            matchSkillPercentage = round(matchSkillPercentage) # round to two decimal
            matchExpPercentage = cosine_similarity(count_exp)[0][1] * 100
            matchExpPercentage = round(matchExpPercentage) # round to two decimal
            matchPositionPercentage = cosine_similarity(count_position)[0][1] * 100
            matchPositionPercentage = round(matchPositionPercentage) # round to two decimal
            matchlocationPercentage = cosine_similarity(count_location)[0][1] * 100
            matchlocationPercentage = round(matchlocationPercentage) # round to two decimal
            matchindustryPercentage = cosine_similarity(count_industry)[0][1] * 100
            matchindustryPercentage = round(matchindustryPercentage) # round to two decimal
            if matchPercentage >=50:
               result.append({"candidate_id":a,"total":matchPercentage,"skill":matchSkillPercentage,"edu":matchEduPercentage, "exp":matchExpPercentage, "position":matchPositionPercentage, "location":matchlocationPercentage, "industry":matchindustryPercentage, "data":candidate})
            serializer = {"Result":result}
        return JsonResponse(serializer)




        
    
