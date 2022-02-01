from rest_framework import serializers

from drons.models import DroneCategory, Pilot, Drone, Competition


class DroneCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCategory
        fields = ('name', 'pk')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # with HyperlinkedModelSerializer we must have url field
    url = serializers.HyperlinkedIdentityField(view_name='drones:drones-detail', lookup_field='pk')
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = ('url', 'name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp',)
        # depth = 1
        # read_only_fields = ('name',)


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = ('url', 'drone', 'distance', 'achievement_date',)
        extra_kwargs = {
            "url": {
                "view_name": "drones:competitions-detail",
                "lookup_field": "pk"
            },
            "drone": {
                "view_name": "drones:drones-detail",
                "lookup_field": "pk"
            }
        }

