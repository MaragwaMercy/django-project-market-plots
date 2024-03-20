from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Plots, Owner, Ownership, AdministrationPlanning, Infrastructure

class PlotsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Plots
        geo_field = 'geom'  # Specify the geometry field
        fields = ('gid', 'plot_number', 'parcel_area', 'allocation_number')  # Exclude the geometry field from fields

    def get_properties(self, instance, fields):
        # Fetch related data from other tables and include them in the properties
        owner = instance.owner_set.first()
        ownership = instance.ownership_set.first()
        admin_planning = instance.administrationplanning_set.first()
        infrastructure = instance.infrastructure_set.first()

        return {
            'plot_number': instance.plot_number,
            'parcel_area': instance.parcel_area,
            'allocation_number': instance.allocation_number,
            # Include properties from related tables
            'owner_name': owner.name if owner else None,
            'owner_id_number': owner.id_number if owner else None,
            'owner_date_of_birth': owner.date_of_birth if owner else None,
            'owner_gender': owner.gender if owner else None,
            'owner_marital_status': owner.marital_status if owner else None,
            'owner_no_of_children': owner.no_of_children if owner else None,
            'owner_telephone_number': owner.telephone_number if owner else None,
            'owner_postal_address': owner.postal_address if owner else None,
            'owner_kra_pin': owner.kra_pin if owner else None,
            'ownership_mode_of_acquisition': ownership.mode_of_acquisition if ownership else None,
            'ownership_ownership_type': ownership.ownership_type if ownership else None,
            'ownership_lease_duration_from': ownership.lease_duration_from if ownership else None,
            'ownership_lease_duration_to': ownership.lease_duration_to if ownership else None,
            'ownership_pay_landrates': ownership.pay_landrates if ownership else None,
            'ownership_proof_of_ownership': ownership.proof_of_ownership if ownership else None,
            'ownership_type_of_document': ownership.type_of_document if ownership else None,
            'admin_planning_is_land_surveyed': admin_planning.is_land_surveyed if admin_planning else None,
            'admin_planning_parcel_under_use': admin_planning.parcel_under_use if admin_planning else None,
            'admin_planning_type_of_use': admin_planning.type_of_use if admin_planning else None,
            'infrastructure_water_supply': infrastructure.water_supply if infrastructure else None,
            'infrastructure_electricalpower': infrastructure.electricalpower if infrastructure else None,
            # Add more properties as needed
        }
