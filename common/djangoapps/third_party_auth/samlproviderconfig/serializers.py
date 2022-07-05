"""
Serializer for SAMLProviderConfig
"""

from rest_framework import serializers

from common.djangoapps.third_party_auth.models import SAMLProviderConfig, SAMLConfiguration


class SAMLProviderConfigSerializer(serializers.ModelSerializer):  # lint-amnesty, pylint: disable=missing-class-docstring
    saml_config_id = serializers.IntegerField(required=False)

    class Meta:
        model = SAMLProviderConfig
        fields = '__all__'

    def validate(self, data):
        """
        Validate that no provider config exists with a different slug and same entity ID
        """
        # If there are any existing provider configs that match the payload's entity ID, don't match the slug and
        # are not archived, raise a validation error. We do this to prevent provider configs from sharing entity ID's
        # which link a provider config to provider data (SAML certificates). An entity ID therefore, is uniquely linked
        # to a single slug/provider config (which in the case of enterprise provider slug == customer slug).
        if SAMLProviderConfig.objects.current_set().filter(
            entity_id=data['entity_id'],
            archived=False,
        ).exclude(slug=data['slug']):
            raise serializers.ValidationError(f"Entity ID: {data['entity_id']} already taken")
        return data

    def create(self, validated_data):
        """
        Overwriting create in order to get a SAMLConfiguration object from id.
        """
        if 'saml_config_id' in validated_data:
            saml_configuration = SAMLConfiguration.objects.current_set().get(id=validated_data['saml_config_id'])
            del validated_data['saml_config_id']
            validated_data['saml_configuration'] = saml_configuration
        if validated_data.get('attr_first_name'):
            validated_data['attr_username'] = validated_data['attr_first_name']
        return SAMLProviderConfig.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'saml_config_id' in validated_data:
            saml_configuration = SAMLConfiguration.objects.current_set().get(id=validated_data['saml_config_id'])
            del validated_data['saml_config_id']
            validated_data['saml_configuration'] = saml_configuration

        for modifiable_field in validated_data:
            setattr(
                instance,
                modifiable_field,
                validated_data.get(modifiable_field, getattr(instance, modifiable_field))
            )
        instance.save()
        return instance
