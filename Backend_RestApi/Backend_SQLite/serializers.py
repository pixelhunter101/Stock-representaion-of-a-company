from rest_framework import serializers
from Backend_SQLite.models import equity,daily_returns

class EquitySerializers(serializers.ModelSerializer):
    class Meta:
        model = equity
        field = ('id',
                'name',
                'ticker',
                'description',
                'start_date',
                'end_date',
                'sector',
                'industry',
                'employees_count',
                'sic_np',
                'location',
                'exchange',
                'cik_no',
                'cusip',
                'currency_id',
                'data_source_id',
                'ckr_log',
                'similar_fund_log',
                'address',
                'company_name',
                'phone_no',
                'website',
                'is_active',
                'url_slug',
                'delisted_date',
                'delisted_reason',
                'image_name',
                'image_aspect_ratio',
                'cumulative_return_update')

class daily_returnsSerializers(serializers.ModelSerializer):
    class Meta:
        model = daily_returns
        field = ('date',	
                'returns',	
                'equity_id', 
                'open',	
                'high',	
                'low',	
                'close',	
                'adj_close')