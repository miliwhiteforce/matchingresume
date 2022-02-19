from rest_framework import serializers
from . import models

class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = '__all__'

class CandidatesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('name','mobile','email','experience','current_title','current_location','canddiate_state','candidate_country','pref_location','current_ctc','industry','total_exp','skills','highestqualification')


class CandidatesIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id')

class CandidatesSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','skills')

class CandidatesEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','highestqualification')

class CandidatesExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','experience','total_exp')

class CandidatesTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','current_title')

class CandidatesLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','current_location','pref_location')


class CandidatesindustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidates
        fields = ('id','industry')