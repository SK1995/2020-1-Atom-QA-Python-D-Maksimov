import requests
import json


from utils.additional_structures import Segment
from utils.exceptions import ResponseStatusCodeException
from urllib.parse import urljoin


class ApiClient:

    def __init__(self, config_api):
        self.base_url = config_api.url
        self.user_email = config_api.user_email
        self.user_password = config_api.user_password
        self.session = requests.Session()
        self.csrf_token = self.login()
        self.segments = list()

    def make_request(self, method, location, status_code=200, headers=None, params=None, data=None, json_convert=True, custom_location=False, allow_redirects=True, json=None):
        if not custom_location:
            url = urljoin(self.base_url, location)
        else:
            url = location

        response = self.session.request(method, url, headers=headers, params=params, data=data, allow_redirects=allow_redirects, json=json)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if json_convert:
            json_response = response.json()
            return json_response
        return response

    def login(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.user_email,
            'password': self.user_password,
            'continue': 'https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com',
        }

        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        response = self.make_request('POST', url, custom_location=True, json_convert=False, data=data, headers=headers, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, data=data, headers=headers, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, data=data, headers=headers, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, data=data, headers=headers, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, data=data, headers=headers, allow_redirects=False, status_code=302)

        url = 'https://target.my.com/csrf/'
        response = self.make_request('GET', url, custom_location=True, json_convert=False, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, allow_redirects=False, status_code=302)

        url = response.headers['location']
        response = self.make_request('GET', url, custom_location=True, json_convert=False, allow_redirects=False)

        return response.headers['set-cookie'].split('; ')[0].split('=')[1]

    def logout(self):
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }

        location = 'logout'

        responce = self.make_request('GET', location, headers=headers, json_convert=False)

    def create_new_segment(self, name):
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }

        json_data = {
            'name': name,
            'pass_condition': 1,
            'relations':
                [
                    {
                        'object_type': 'remarketing_player',
                        'params':
                            {
                                'type': 'positive',
                                'left': 365,
                                'right': 0
                            }
                    },
                    {
                        'object_type': 'remarketing_payer',
                        'params':
                            {
                                'type': 'positive',
                                'left': 365,
                                'right': 0
                            }
                    }
                ],
            'logicType': 'or'
        }

        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'

        response = self.make_request('POST', location, headers=headers, json=json_data)

        self.segments.append(Segment(id=response['id'], name=response['name']))

    def delete_segment(self, id):
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }

        location = 'api/v2/remarketing/segments/' + str(id) + '.json'

        response = self.make_request('DELETE', location, headers=headers, json_convert=False, status_code=204)

        i = 0
        for segment in self.segments:
            if segment.id == id:
                self.segments.pop(i)
                break
            i += 1

    def rename_segment(self, new_name, id):
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }

        json_data = {
            'name': new_name,
            'pass_condition': 1,
            'relations':
                [
                    {
                        'object_type': 'remarketing_player',
                        'params':
                            {
                                'type': 'positive',
                                'left': 365,
                                'right': 0
                            }
                    },
                    {
                        'object_type': 'remarketing_payer',
                        'params':
                            {
                                'type': 'positive',
                                'left': 365,
                                'right': 0
                            }
                    }
                ],
            'logicType': 'or'
        }

        location = 'api/v2/remarketing/segments/' + str(id) + '.json'

        response = self.make_request('POST', location, headers=headers, json=json_data, status_code=204, json_convert=False)

        for segment in self.segments:
            if segment.id == id:
                segment.name = new_name
                break

    def delete_all_segments(self):
        for segment in self.segments:
            self.delete_segment(segment.id)
