#
# Copyright 2011 Scott Turnbull
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django import forms

from westeros.houses.models import Realm

class CreateRealm(forms.Form):
    """
    Lets users either choose or allow Realm to be randomly generated.
    """
    # REALM Selection requires a little Help
    # Help Text
    ht = "Select a realm for this house or allow the realm to be randomly selected."
    # Build our choices for Realms
    realm_choices = (0, '*Generate Randomly*')
    realm_choices.extend([(realm.id, realm.name) for realm in Realm.objects.all()])
    # Create the choice field
    realm = forms.ChoiceField(choices=tuple(realm_choices), help_text=ht)