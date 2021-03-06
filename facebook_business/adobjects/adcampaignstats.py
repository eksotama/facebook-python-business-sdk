# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCampaignStats(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCampaignStats = True
        super(AdCampaignStats, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        actions = 'actions'
        adgroup_id = 'adgroup_id'
        campaign_id = 'campaign_id'
        campaign_ids = 'campaign_ids'
        clicks = 'clicks'
        end_time = 'end_time'
        id = 'id'
        impressions = 'impressions'
        inline_actions = 'inline_actions'
        io_number = 'io_number'
        is_completed = 'is_completed'
        line_number = 'line_number'
        newsfeed_position = 'newsfeed_position'
        social_clicks = 'social_clicks'
        social_impressions = 'social_impressions'
        social_spent = 'social_spent'
        social_unique_clicks = 'social_unique_clicks'
        social_unique_impressions = 'social_unique_impressions'
        spent = 'spent'
        start_time = 'start_time'
        topline_id = 'topline_id'
        unique_clicks = 'unique_clicks'
        unique_impressions = 'unique_impressions'

    class ActionAttributionDaysAfterClick:
        value_0 = '0'
        value_1 = '1'
        value_7 = '7'
        value_14 = '14'
        value_28 = '28'

    class ActionAttributionDaysAfterImp:
        value_0 = '0'
        value_1 = '1'
        value_7 = '7'
        value_14 = '14'
        value_28 = '28'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdCampaignStats,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'account_id': 'string',
        'actions': 'Object',
        'adgroup_id': 'string',
        'campaign_id': 'string',
        'campaign_ids': 'list<string>',
        'clicks': 'unsigned int',
        'end_time': 'Object',
        'id': 'string',
        'impressions': 'string',
        'inline_actions': 'map',
        'io_number': 'unsigned int',
        'is_completed': 'bool',
        'line_number': 'unsigned int',
        'newsfeed_position': 'Object',
        'social_clicks': 'unsigned int',
        'social_impressions': 'string',
        'social_spent': 'unsigned int',
        'social_unique_clicks': 'unsigned int',
        'social_unique_impressions': 'string',
        'spent': 'int',
        'start_time': 'Object',
        'topline_id': 'string',
        'unique_clicks': 'unsigned int',
        'unique_impressions': 'string',
    }

    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ActionAttributionDaysAfterClick'] = AdCampaignStats.ActionAttributionDaysAfterClick.__dict__.values()
        field_enum_info['ActionAttributionDaysAfterImp'] = AdCampaignStats.ActionAttributionDaysAfterImp.__dict__.values()
        return field_enum_info
