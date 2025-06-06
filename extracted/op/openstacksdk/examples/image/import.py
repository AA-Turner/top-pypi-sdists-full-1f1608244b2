# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from examples.connect import EXAMPLE_IMAGE_NAME

"""
Create resources with the Image service.

For a full guide see
https://docs.openstack.org/openstacksdk/latest/user/guides/image.html
"""


def import_image(conn):
    print("Import Image:")

    # Url where glance can download the image
    uri = (
        'https://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img'
    )

    # Build the image attributes and import the image.
    image_attrs = {
        'name': EXAMPLE_IMAGE_NAME,
        'disk_format': 'qcow2',
        'container_format': 'bare',
        'visibility': 'public',
    }
    image = conn.image.create_image(**image_attrs)
    conn.image.import_image(image, method="web-download", uri=uri)
