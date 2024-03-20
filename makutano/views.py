from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import date
from .models import *

class HomepageView(TemplateView):
    template_name = 'plots_list.html'

def get_properties(instance):
    # Fetch related data from other tables and include them in the properties
    owner = instance.owner_set.first()
    ownership = instance.ownership_set.first()
    admin_planning = instance.administrationplanning_set.first()
    infrastructure = instance.infrastructure_set.first()

    # Convert date fields to string representation
    owner_date_of_birth = owner.date_of_birth.strftime('%Y-%m-%d') if owner and owner.date_of_birth else None
    
    return {
        'plot_number': instance.plot_number,
        'parcel_area': instance.parcel_area,
        'allocation_number': instance.allocation_number,
        # Include properties from related tables
        'owner_name': owner.name if owner else None,
        'owner_id_number': owner.id_number if owner else None,
        'owner_date_of_birth': owner_date_of_birth,  # Use converted date string
        'owner_gender': owner.gender if owner else None,
        'owner_marital_status': owner.marital_status if owner else None,
        'owner_no_of_children': owner.no_of_children if owner else None,
        'owner_telephone_number': owner.telephone_number if owner else None,
        'owner_postal_address': owner.postal_address if owner else None,
        'owner_kra_pin': owner.kra_pin if owner else None,
        'ownership_mode_of_acquisition': ownership.mode_of_acquisition if ownership else None,
        'ownership_ownership_type': ownership.ownership_type if ownership else None,
        'ownership_lease_duration_from': ownership.lease_duration_from.strftime('%Y-%m-%d') if ownership and ownership.lease_duration_from else None,
        'ownership_lease_duration_to': ownership.lease_duration_to.strftime('%Y-%m-%d') if ownership and ownership.lease_duration_to else None,
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

import json  # Add this import statement

def Plots_data(request):
    plots_data = serialize('geojson', Plots.objects.all())
    serialized_data = json.loads(plots_data)  
    
    for feature in serialized_data['features']:
       
        feature_id = int(feature['id'])
        
        
        properties = get_properties(Plots.objects.get(pk=feature_id))
        
       
        feature['properties'].update(properties)
    
    
    modified_plots_data = json.dumps(serialized_data)
    
    return HttpResponse(modified_plots_data, content_type='application/json')

