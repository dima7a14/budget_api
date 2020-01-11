from rest_framework import serializers

from api.users.models import User
from api.families.models import Family


class BaseFamilySerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'owner_id',
        )
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner_id']
        model = Family
        depth = 1


class MemberSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(write_only=True, required=True))

    class Meta:
        fields = ('ids',)

    def create(self, validated_data):
        ids = validated_data.pop("ids", [])

        return User.objects.filter(id__in=ids)

    def update(self, instance, validated_data):
        return instance


class CreateFamilySerializer(BaseFamilySerializer):
    member_ids = serializers.ListField(child=serializers.IntegerField(write_only=True, required=True), write_only=True)

    class Meta(BaseFamilySerializer.Meta):
        fields = (*BaseFamilySerializer.Meta.fields, 'member_ids')

    def create(self, validated_data):
        owner = validated_data.pop("owner")
        member_ids = validated_data.pop("member_ids")

        validated_data["owner"] = owner

        members = filter(lambda m: m is not None, map(lambda m: User.objects.filter(id__exact=m).first(), member_ids))

        family = Family.objects.create(**validated_data)

        family.save()
        family.members.add(*list({*members, owner}))

        return family

